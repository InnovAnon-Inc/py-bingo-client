#! /usr/bin/python3

from __future__ import print_function

import sys
from time import sleep
from sys import stdin, exit

from PodSixNet.Connection import connection, ConnectionListener

# This example uses Python threads to manage async input from sys.stdin.
# This is so that I can receive input from the console whilst running the server.
# Don't ever do this - it's slow and ugly. (I'm doing it for simplicity's sake)
from _thread import *

from game                 import Game
from scene.game_scene     import GameScene
from scene.draw_scene     import DrawScene
from scene.lobby_scene    import LobbyScene
from scene.end_game_scene import EndGameScene

class GameClient(object):
    def __init__(self, host, port):
        self.host   = host
        self.port   = port
        self.game   = Game()
        self.client = None
    def Loop(self):
        if self.game.isPhase2():
            if not self.client: self.client = Client(self.host, self.port, self.game)
        if self.client: self.client.Loop()
        self.game.tick()

class Client(ConnectionListener):
    def __init__(self, host, port, game):
        self.Connect((host, port))
        print("Chat client started")
        print("Ctrl-C to exit")
        # get a nickname from the user before starting
        name = str(game.active_scene.name)
        print("Enter your nickname: %s" % name)
        #connection.Send({"action": "nickname", "nickname": stdin.readline().rstrip("\n")})
        connection.Send({"action": "nickname", "nickname": name})
        # launch our threaded input loop
        #t = start_new_thread(self.InputLoop, ())
        self.game = game
    
    def Loop(self):
        connection.Pump()
        self.Pump()
    
    #def InputLoop(self):
        # horrid threaded input loop
        # continually reads from stdin and sends whatever is typed to the server
    #    while 1:
    #        connection.Send({"action": "message", "message": stdin.readline().rstrip("\n")})
    
    #######################################
    ### Network event/message callbacks ###
    #######################################
    
    def Network_players(self, data):
        print("*** players: " + ", ".join([p for p in data['players']]))
        self.game.active_scene.SwitchToScene(LobbyScene())
    
    def Network_message(self, data):
        print(data['who'] + ": " + data['message'])

    def Network_board(self, data):
        board = data['board']
        print(board)
        self.board = board
        self.history = []
        self.game.active_scene.SwitchToScene(GameScene(board, self.history))
    def Network_draw(self, data):
        draw = data['draw']
        self.history.append(draw)
        self.board = data['board']
        print("draw: " + str(draw))
        self.game.active_scene.SwitchToScene(DrawScene(draw, self.board, self.history))
    def Network_update(self, data):
        print(data['update'])
    def Network_end_game(self, data):
        winners, losers = data['winners'], data['losers']
        print(winners)
        print(losers)
        self.game.active_scene.SwitchToScene(EndGameScene(winners, losers))
    
    # built in stuff

    def Network_connected(self, data):
        print("You are now connected to the server")
    
    def Network_error(self, data):
        print('error:', data['error'][1])
        connection.Close()
    
    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        c = GameClient(host, int(port))
        fps  = 60.0
        ifps = 1 / fps
        while 1:
            c.Loop()
            sleep(ifps)
