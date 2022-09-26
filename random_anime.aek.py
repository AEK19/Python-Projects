from random import choice

animes = [['dragonball', 'happy', 'classic', 'series'],
    ['naruto', 'action', 'anxious', 'series',], ['bleach', 'gothic', 'sad', 'adventure'], ['hunterxhunter', 'action', 'angry', 'series']]

print('what mood are you in?')
mood = input()

for item in animes:
    if item [1] == mood:
        print(mood + ' anime: ' + item[0])
