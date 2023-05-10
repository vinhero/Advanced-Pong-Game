import pygame
import sqlite3
#from view import View
#from ..GameObjects.Player import Player


class Model:
    def __init__(self):
        #self.view = View()
        self.match = False
        self.GameObjects = dict()

    def initMatch(self):
        #self.GameObjects = dict(player1=Player())
        self.runMatch()

    def runMatch(self):
        self.match = True
        # while self.match:
        #     pass

    def saveMatchResult(self):
        
        def insert_data(name1, score1, name2, score2):
            c.execute("INSERT INTO spieler_scores (player, score1, player, score2) VALUES (?, ?, ?, ?)",
                    (name1, score1, name2, score2))
            conn.commit()
            print("Daten wurden erfolgreich in die Tabelle eingefügt!")
        
        conn = sqlite3.connect('spieler_scores.db')

        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS spieler_scores
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player1 TEXT,
                    score1 INTEGER,
                    player2 TEXT,
                    score2 INTEGER)''')

        insert_data("Spieler A", 10, "Spieler B", 20)

        conn.close()