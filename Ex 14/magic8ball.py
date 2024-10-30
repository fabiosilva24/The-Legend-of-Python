# Write code below 💖

import random

ask = str(input("Question: "))
replies = ["Yes - definitely.", 
          "It is decidedly so.",
          "Without a doubt.",
          "Reply hazy, try again.",
          "Ask again later.",
          "Better not tell you now.",
          "My sources say no.",
          "Outlook not so good.",
          "Very doubtful."]
MagicBall = random.choice(replies)

print(MagicBall)