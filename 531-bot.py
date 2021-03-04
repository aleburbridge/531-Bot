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

        setsList.append(myround(self.maxweight * self.set1))
        setsList.append(myround(self.maxweight * self.set2))
        setsList.append(myround(self.maxweight * self.set3))

        return setsList

w1 = {0.65: ' x 5', 0.75: ' x 5', 0.85: ' x 5+'}
w2 = {0.7: ' x 3', 0.8: ' x 3', 0.9: ' x 3+'}
w3 = {0.75: ' x 5', 0.85: ' x 3', 0.95: ' x 1+'}
w4 = {0.4: ' x 5', 0.5: ' x 5', 0.6: ' x 5'}

dictDict = {'w1': w1, 'w2':w2, 'w3':w3, 'w4':w4}

# these numbers are the 1RM, change these each month
press = Workout('press', 100)
squat = Workout('squat', 250)
deadlift = Workout('deadlift', 315)
bench = Workout('bench', 200)
exerciseDict = {'press': press, 'squat': squat, 'deadlift': deadlift, 'bench':bench}

press_accessories_upperchest = ['incline bench','60 degree handstand-pushup','low-to-high cable fly','jammer press machine','pike pushup']
press_accessories_triceps = ['dips','close grip bench','bodyweight skullcrusher','close grip pushup','overhead extension']

deadlift_accessories_calves = ['seated calf press', 'standing calf press machine', 'band push', 'isometric stretched hold','explosive step up']
deadlift_accessories_hamstrings = ['good mornings','romanian deadlift','hamstring curl','reverse sled pull','kettlebell swing']

bench_accessories_notreardelt = ['lat raise','front raise','upright row','handstand hold','leaning cable lat raise']
bench_accessories_reardelt = ['rear dumbbell flye','reverse pec deck','face pull','rear delt cable crossover','dumbbell external rotation']

squat_accessories_quads = ['single-leg trx handle squat','trx band single-leg lunge','machine hack squat','barbell hack squat','box jump']
squat_accessories_calves = deadlift_accessories_calves

#bot stuff!
@client.event
async def on_ready():
    general_channel = client.get_channel(channelID)
    print('Connected Successfully')

@client.event
async def on_message(message):
    general_channel = client.get_channel(channelID)

    if message.content.startswith('$w'):
        workoutMessage = message.content
        messageWeek = workoutMessage[1:3]
        workoutMessage = workoutMessage.split()
        messageExercise = workoutMessage[1]
        
        floatsList = list(dictDict[messageWeek].keys())
        repsList = list(dictDict[messageWeek].values())

        exerciseDict[messageExercise].set1 = floatsList[0]
        exerciseDict[messageExercise].set2 = floatsList[1]
        exerciseDict[messageExercise].set3 = floatsList[2]
        
        setsList = (exerciseDict[messageExercise]).todaysWorkout()
        print(setsList)
        print(type(setsList))

        async def print_sets():
            if messageExercise == 'press':
                for i in range(0,3):
                    await general_channel.send(f'Set #{i + 1}: {setsList[i]} {repsList[i]}')
                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5  x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            elif messageExercise == 'deadlift':
                for i in range(0,3):
                    await general_channel.send(f'Set #{i + 1}: {setsList[i]} {repsList[i]}')
                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5  x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            elif messageExercise == 'bench':
                for i in range(0,3):
                    await general_channel.send(f'Set #{i + 1}: {setsList[i]} {repsList[i]}')
                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5  x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            elif messageExercise == 'squat':
                for i in range(0,3):
                    await general_channel.send(f'Set #{i + 1}: {setsList[i]} {repsList[i]}')
                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5  x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')
            
            else:
                print('zoop')

        await print_sets()

client.run(TOKEN)