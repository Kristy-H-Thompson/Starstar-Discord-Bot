import os
import random
from enum import Enum


TOKEN = os.getenv("DISCORD_TOKEN")

def get_winner(p1):
   p2 = random.choice(["CLAW", "ROCK", "LEAF"])
   print(p1, p2)
   try:
      p1 = p1.upper()
   except:
      return "That's not right... try 'claw' 'rock' or 'leaf' <a:starstar:936991811266830426>"
   if p1 == p2:
      return ("It's a tie! " + p1.capitalize() + " vs " + p2.lower())
   elif p1 =='ROCK':
       if p2 == 'scissors':
         return ("You win! " + p1.capitalize() + " beats " + p2.lower() + " <a:starstar:936991811266830426>")
       else:
         return ("STARSTAR!!!! wins! " + p2.capitalize() + " is way better than " + p1.lower()) 
   elif p1 == 'CLAW':
      if p2 =='LEAF':
         return ("You win! " + p1.capitalize() + " beats " + p2.lower() + " <a:starstar:936991811266830426>")
      else:
         return ("STARSTAR!!!! wins! " + p2.capitalize() + " is way better than " + p1.lower()) 
   elif p1 == 'LEAF':
      if p2 == 'ROCK':
         return ("You win! " + p1.capitalize() + " beats " + p2.lower() + " <a:starstar:936991811266830426>")
      else:
         return ("STARSTAR!!!! wins! " + p2.capitalize() + " is way better than " + p1.lower()) 
   else:
      return "Invalid input! Try 'claw' 'rock' or 'leaf'"
