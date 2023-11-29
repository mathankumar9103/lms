dis = int(input())

bonus = 100

first_50 = 50 * 3
next_50 = 50 * 5
next_100 = 100 * 6

if (dis <= 50):
    score = dis * 3
elif (dis <= 100):
    remaining = dis - 50
    remaining = remaining * 5
    score = first_50 + remaining
elif (dis <= 200):
    remaining = dis - 100
    remaining = remaining * 6
    score = first_50 + next_50 + remaining
else:
    remaining = dis - 200
    remaining = remaining * 10
    score = first_50 + next_50 + next_100 + remaining

score = score + bonus
print(score)