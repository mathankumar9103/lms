import pandas as pd
import pydash

df = pd.read_csv("t20.csv")

data = df.to_dict(orient="records")

print("")
choice = True
while choice:
    ch = int(input("enter your choice:"))

    if ch == 1:
        try:
            mat = 0
            player = {}
            for itr in data:
                if itr['Mat'] > mat:
                    mat = itr['Mat']
                    player = itr
        except Exception as e:
            print(e)
        print("More number of matches:")
        print(player)
    if ch == 2:
        try:
            player = []
            for i in data:
                if i['Runs'] != '-':
                    if int(i['Runs']) > 1000:
                        player.append(i)
        except Exception as e:
            print(e)
        print("More number of runs:")
        print(player)
    if ch == 3:
        try:
            player = []
            for i in data:
                if i['Ave'] != '-':
                    if float(i['Ave']) > 70:
                        player.append(i)
        except Exception as e:
            print(e)
        print("Average:")
        print(player)
    if ch == 4:
        try:
            strike_rate = 0
            player = { }
            for i in data:
                if i['SR'] != '-':
                    if float(i['SR']) > strike_rate:
                        strike_rate = i['SR']
                        player = i
        except Exception as e:
            print(e)
        print(player)
    if ch == 5:
        try:
            centuries = 0
            player = []
            for i in data:
                if i['100'] != '-':
                    if int(i['100']) > centuries:
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch == 6:
        try:
            half_centuries = 0
            player = []
            for i in data:
                if i['50'] != '-':
                    if int(i['50']) > half_centuries:
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch == 7:
        try:
            player = []
            for i in data:
                if i['Runs'] != '-':
                    if int(i['Runs']) == 0:
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch == 8:
        try:
            fours = 0
            player = []
            for i in data:
                if i['4s'] != '-':
                    if int(i['4s']) > fours:
                        fours = int(i['4s'])
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch == 9:
        try:
            sixes = 0
            player = []
            for i in data:
                if i['6s'] != '-':
                    if int(i['6s']) > sixes:
                        sixes = int(i['6s'])
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch ==10:
        try:
            span = 0
            for i in data:
                if i['Span'] != '-':
                    x = i['Span'].split("-")
                    S = int(x[1]) - int(x[0])
                    if S > span:
                        span = S
                        player = i
        except Exception as e:
            print(e)
        print(player)

    if ch == 11:
        try:
            innings = 0
            player = []
            for i in data:
                if i['Inns'] != '-':
                    if int(i['Inns']) > innings:
                        innings = int(i['Inns'])
                        player = i
        except Exception as e:
            print(e)
        print(player)

    if ch == 12:
        try:
            ball_faced = 0
            player = []
            for i in data:
                if i['BF'] != '-':
                    if int(i['BF']) > ball_faced:
                        ball_faced = int(i['BF'])
                        player.append(i)
        except Exception as e:
            print(e)
        print(player)

    if ch == 13:
        try:
            no = 50
            player = []
            for i in data:
                if i['NO'] != '-':
                    if int(i['NO']) >= no:
                        player.append(i['Player'])
        except Exception as e:
            print(e)
        print(player)

    if ch == 14:
        try:
            score = 150
            player = []
            for i in data:
                if i['HS'] != '-':
                    hs = i['HS']
                    if hs[-1] == '*':
                        l = (len(hs) - 1)
                        hs = hs[0:l]
                    if int(hs) >= score:
                        player.append(i['Player'])
        except Exception as e:
            print(e)
        print(player)

    if ch == 15:
        try:
            player = []
            cent = 0
            for i in data:
                if i['100'] != '-':
                    if int(i['100']) > cent:
                        player.append(i)

        except Exception as e:
            print(e)
        print(player)

    if ch == 16:
        try:
            sixes = 50
            player =[]
            for i in data:
                if i['6s'] != '-':
                    if int(i['6s']) > sixes:
                        player.append(i['Player'])
        except Exception as e:
            print(e)
        print(player)

    if ch == 17:
        try:
            fours = 70
            sixes = 33
            player = []
            for i in data:
                if i['4s'] != '-' and i['6s'] != '-':
                    if int(i['4s']) > fours and int(i['6s']) <= sixes:
                        player.append(i['Player'])
        except Exception as e:
            print(e)
        print(player)



