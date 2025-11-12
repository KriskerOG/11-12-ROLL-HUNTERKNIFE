import random
with open('participants.txt', 'r') as f:
    participants = f.readlines()
  winner = random.choice(participants)
print(“恭喜”, winner.strip(), “中奖了！”)

