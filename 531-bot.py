import discord 
import random
client = discord.Client()

TOKEN = 'YOUR TOKEN HERE'
channelID = 'YOUR CHANNEL ID HERE (int, not a string!)'

#function that rounds to nearest 5
def myround(x, base=5):
    return base * round(x/base)

class Workout:
    def __init__(self, exercise, maxweight):
        self.exercise = exercise
        self.maxweight = maxweight

    def todaysWorkout(self):
        setsList = []

        setsList.append(myround( (self.maxweight * .9) * self.set1))
        setsList.append(myround( (self.maxweight * .9) * self.set2))
        setsList.append(myround( (self.maxweight * .9) * self.set3))

        return setsList

w1 = {0.65: ' x 5', 0.75: ' x 5', 0.85: 'x 5+'}
w2 = {0.7: ' x 3', 0.8: ' x 3', 0.9: ' x3+'}
w3 = {0.75: ' x 5', 0.85: ' x 3', 0.95: ' x1+'}
w4 = {0.4: ' x 5', 0.5: ' x 5', 0.6: ' x5'}
weekDict = {'w1': w1, 'w2':w2, 'w3':w3, 'w4':w4}

# these numbers are the 1RM, change these each cycle
press = Workout('press', 100)
squat = Workout('squat', 250)
deadlift = Workout('deadlift', 315)
bench = Workout('bench', 200)
exerciseDict = {'press': press, 'squat': squat, 'deadlift': deadlift, 'bench':bench}

# bot stuff!
@client.event
async def on_ready():
    general_channel = client.get_channel(channelID)
    print('Connected Successfully')

@client.event
async def on_message(message):
    general_channel = client.get_channel(channelID)

    async def print_sets():
        for i in range(0,3):
            await general_channel.send(f'Set #{i + 1}: {setsList[i]} {repsList[i]}')

    if message.content.startswith('$w'):
        workoutMessage = message.content
        messageWeek = workoutMessage[1:3]
        workoutMessage = workoutMessage.split()
        messageExercise = workoutMessage[1]
        
        floatsList = list(weekDict[messageWeek].keys())
        repsList = list(weekDict[messageWeek].values())

        exerciseDict[messageExercise].set1 = floatsList[0]
        exerciseDict[messageExercise].set2 = floatsList[1]
        exerciseDict[messageExercise].set3 = floatsList[2]
        
        setsList = (exerciseDict[messageExercise]).todaysWorkout()

        await print_sets()

    if '1rm' in message.content:
        await general_channel.send(f'Your 1-rep maxes (not 90% value):\nPress: {press.maxweight}\nDeadlift: {deadlift.maxweight}\nBench: {bench.maxweight}\nSquat: {squat.maxweight}')

client.run(TOKEN)