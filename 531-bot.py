import discord 
import random
client = discord.Client()

# 1RM variables
press_1RM = 115
deadlift_1RM = 310
bench_1RM = 200
squat_1RM = 245



press_accessories_upperchest = ['incline bench','60 degree handstand-pushup','low-to-high cable fly','jammer press machine','pike pushup']
press_accessories_triceps = ['dips','close grip bench','bodyweight skullcrusher','close grip pushup','overhead extension']

deadlift_accessories_calves = ['seated calf press', 'standing calf press machine', 'band push', 'isometric stretched hold','explosive step up']
deadlift_accessories_hamstrings = ['good mornings','romanian deadlift','hamstring curl','reverse sled pull','kettlebell swing']

bench_accessories_notreardelt = ['lat raise','front raise','upright row','handstand hold','leaning cable lat raise']
bench_accessories_reardelt = ['rear dumbbell flye','reverse pec deck','face pull','rear delt cable crossover','dumbbell external rotation']

squat_accessories_quads = ['single-leg trx handle squat','trx band single-leg lunge','machine hack squat','barbell hack squat','box jump']
squat_accessories_calves = deadlift_accessories_calves

press_alternative = []
deadlift_alternative = []
bench_alternative = []
squat_alternative = []

#function that rounds to nearest 5!
def myround(x, base=5):
    return base * round(x/base)

#functions for workouts!
def weekOne(workout):
    setsList = []
    
    setsList.append(myround(workout * .6))
    setsList.append(myround(workout * .7))
    setsList.append(myround(workout * .8))
    return setsList

def weekTwo(workout):
    setsList = []
    
    setsList.append(myround(workout * .65))
    setsList.append(myround(workout * .75))
    setsList.append(myround(workout * .85))
    return setsList

def weekThree(workout):
    setsList = []
    
    setsList.append(myround(workout * .7))
    setsList.append(myround(workout * .8))
    setsList.append(myround(workout * .9))
    return setsList

def weekFour(workout):
    setsList = []
    
    setsList.append(myround(workout * .4))
    setsList.append(myround(workout * .5))
    setsList.append(myround(workout * .6))
    return setsList

fiveThreeOne = ['zoop',5,3,1]

#bot stuff!
@client.event
async def on_ready():
    general_channel = client.get_channel(763972697801621565)
    print('Connected Successfully')

@client.event
async def on_message(message):
    general_channel = client.get_channel(763972697801621565)

    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await general_channel.send('hi')

    if message.content.startswith('$week '):
        workout_message = message.content.split('$week ',1)[1] 

        if workout_message.startswith('1'):
            workout_message = message.content.split('1 ',1)[1]   
            if workout_message == "press":      
                for i, weight in enumerate(weekOne(press_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5  x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            if workout_message == "deadlift":      
                for i, weight in enumerate(weekOne(deadlift_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(deadlift_accessories_calves)) + ' 5 x 10')
                await general_channel.send(str(random.choice(deadlift_accessories_hamstrings)) + ' 5 x 10')

            if workout_message == "bench":      
                for i, weight in enumerate(weekOne(bench_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(bench_accessories_notreardelt)) + ' 5 x 10')
                await general_channel.send(str(random.choice(bench_accessories_reardelt)) + ' 5 x 10')

            if workout_message == "squat":      
                for i, weight in enumerate(weekOne(squat_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(squat_accessories_quads)) + ' 5 x 10')
                await general_channel.send(str(random.choice(squat_accessories_calves)) + ' 5 x 10')


        if workout_message.startswith('2'):      
            workout_message = message.content.split('2 ',1)[1]    
            if workout_message == "press":      
                for i, weight in enumerate(weekTwo(press_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 3')

                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5 x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            if workout_message == "deadlift":      
                for i, weight in enumerate(weekTwo(deadlift_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 3')

                await general_channel.send(str(random.choice(deadlift_accessories_calves)) + ' 5 x 10')
                await general_channel.send(str(random.choice(deadlift_accessories_hamstrings)) + ' 5 x 10')

            if workout_message == "bench":      
                for i, weight in enumerate(weekTwo(bench_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 3')

                await general_channel.send(str(random.choice(bench_accessories_notreardelt)) + ' 5 x 10')
                await general_channel.send(str(random.choice(bench_accessories_reardelt)) + ' 5 x 10')

            if workout_message == "squat":      
                for i, weight in enumerate(weekTwo(squat_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 3')

                await general_channel.send(str(random.choice(squat_accessories_quads)) + ' 5 x 10')
                await general_channel.send(str(random.choice(squat_accessories_calves)) + ' 5 x 10')


        if workout_message.startswith('3'):   
            workout_message = message.content.split('3 ',1)[1]   
            if workout_message == "press":           
                for i, weight in enumerate(weekThree(press_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x ' + str(fiveThreeOne[i + 1]))

                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5 x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')

            if workout_message == "deadlift":      
                for i, weight in enumerate(weekThree(deadlift_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x ' + str(fiveThreeOne[i + 1]))

                await general_channel.send(str(random.choice(deadlift_accessories_calves)) + ' 5 x 10')
                await general_channel.send(str(random.choice(deadlift_accessories_hamstrings)) + ' 5 x 10')

            if workout_message == "bench":      
                for i, weight in enumerate(weekThree(bench_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x ' + str(fiveThreeOne[i + 1]))

                await general_channel.send(str(random.choice(bench_accessories_notreardelt)) + ' 5 x 10')
                await general_channel.send(str(random.choice(bench_accessories_reardelt)) + ' 5 x 10')

            if workout_message == "squat":      
                for i, weight in enumerate(weekThree(squat_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x ' + str(fiveThreeOne[i + 1]))

                await general_channel.send(str(random.choice(squat_accessories_quads)) + ' 5 x 10')
                await general_channel.send(str(random.choice(squat_accessories_calves)) + ' 5 x 10')


        if workout_message.startswith('4'):     
            workout_message = message.content.split('4 ',1)[1]    
            if workout_message == "press":
                for i, weight in enumerate(weekFour(press_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(press_accessories_upperchest)) + ' 5 x 10')
                await general_channel.send(str(random.choice(press_accessories_triceps)) + ' 5 x 10')
                
            if workout_message == "deadlift":      
                for i, weight in enumerate(weekFour(deadlift_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(deadlift_accessories_calves)) + ' 5 x 10')
                await general_channel.send(str(random.choice(deadlift_accessories_hamstrings)) + ' 5 x 10')

            if workout_message == "bench":      
                for i, weight in enumerate(weekFour(bench_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(bench_accessories_notreardelt)) + ' 5 x 10')
                await general_channel.send(str(random.choice(bench_accessories_reardelt)) + ' 5 x 10')

            if workout_message == "squat":    
                for i, weight in enumerate(weekFour(squat_1RM)):
                    await general_channel.send(f"Set #{i + 1}: " + str(weight) + ' x 5')

                await general_channel.send(str(random.choice(squat_accessories_quads)) + ' 5 x 10')
                await general_channel.send(str(random.choice(squat_accessories_calves)) + ' 5 x 10')

client.run('NzYzOTY0MDc2OTA4ODcxNjkx.X3_W_Q.nhGpmniKDGoENyNIYpEmetMw3Xs')