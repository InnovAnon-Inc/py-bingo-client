#! /usr/bin/python3

from __future__ import print_function

import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server

from client_channel import ClientChannel
from bingo          import Bingo
from q              import Q

class BingoServer(Server):
    channelClass = ClientChannel
    
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('Server launched')
        self.game = None
    
    def Connected(self, channel, addr):
        self.AddPlayer(channel)
    
    def AddPlayer(self, player):
        print("New Player" + str(player.addr))
        self.players[player] = True
        self.SendPlayers()
        print("players", [p for p in self.players])
    
    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        if self.game: self.game.DelPlayer(player)
        del self.players[player]
        self.SendPlayers()
    
    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": [p.nickname for p in self.players]})
    
    def SendToAll(self, data):
        [p.Send(data) for p in self.players]
    
    def Launch(self):
        #game  = None
        q     = None
        #T     = 0.0001
        T     = 1.5

        while True:
            self.Pump()
            sleep(T)
            if self.game:
                self.game.tick()
                #for p in self.game: p.Send({"action" : "draw", "draw" : self.game.last_draw})
                #self.SendToAll({"action" : "draw", "draw" : self.game.last_draw})
                for p, b in self.game.items(): p.Send({"action" : "draw", "draw" : self.game.last_draw, "board" : b.toString(self.game.isSelected())})
                #for p, b in self.game.items(): p.Send({"action" : "board", "board" : b.toString(self.game.isSelected())})

                if not self.game.isOver(): continue

                print("Ending Game")
                #self.SendToAll({"action" : "end_game", "end_game" : "Ending Game"})
                #for p, b in self.game.items(): p.Send({"action" : "end_game", "end_game" : "Ending Game"})
                results = self.game.getResults()
                winners = list(map(lambda p: p.nickname, results['winners']))
                losers  = list(map(lambda p: p.nickname, results['losers']))
                print(winners)
                print(losers)
                self.SendToAll({"action" : "end_game", "winners" : winners, "losers" : losers})
                self.game = None

            if not q:
                self.SendToAll({"action" : "update", "update" : "Creating Queue to wait for next Game"})
                q = Q(1, 20, 3, 60, self.players)

            q.tick(T)

            if not q.isDone():
                #self.SendToAll({"action" : "update", "update" : "Waiting for next Game"})
                continue

            self.game = Bingo(q.players)
            self.SendToAll({"action" : "update", "update" : "Starting new Game(players=%s)" % ([p.nickname for p in self.game],)})
            #for p, b in self.game.items(): p.Send({"action" : "board", "board" : str(b)})
            for p, b in self.game.items(): p.Send({"action" : "board", "board" : b.toString(self.game.isSelected())})
            print("Starting new Game(players=%s)" % (q.players,))
            q = None

# get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = BingoServer(localaddr=(host, int(port)))
        s.Launch()

