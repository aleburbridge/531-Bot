import discord 
import datetime
client = discord.Client()

todays_date = datetime.datetime.now()
weekday_value = datetime.datetime.today().weekday()

#makes the datetime weekday value readable :-)
def weekday_converter(value):
    global weekday_value
    if value == 0:
        weekday_value = 'Monday'
    elif value == 1:
        weekday_value = 'Tuesday'
    elif value == 2:
        weekday_value = 'Wednesday'
    elif value == 3:
        weekday_value = 'Thursday'
    elif value == 4:
        weekday_value = 'Friday'
    elif value == 5:
        weekday_value = 'Saturday'
    elif value == 6:
        weekday_value = 'Sunday'
weekday_converter(weekday_value)
print(weekday_value)


# 1RM variables
press_1RM = 115
deadlift_1RM = 310
bench_1RM = 200
squat_1RM = 245

#functions for workouts!
def weekOne(workout):
    setsList = []
    
    setsList.append(workout * .6)
    setsList.append(workout * .7)
    setsList.append(workout * .8)
    return setsList

def weekTwo(workout):
    setsList = []
    
    setsList.append(workout * .65)
    setsList.append(workout * .75)
    setsList.append(workout * .85)
    return setsList

def weekThree(workout):
    setsList = []
    
    setsList.append(workout * .7)
    setsList.append(workout * .8)
    setsList.append(workout * .9)
    return setsList

def weekFour(workout):
    setsList = []
    
    setsList.append(workout * .4)
    setsList.append(workout * .5)
    setsList.append(workout * .6)
    return setsList



#bot stuff!
@client.event
async def on_ready():
    general_channel = client.get_channel(YOUR CHANNEL HERE)
    print('Connected Successfully')

@client.event
async def on_message(message):
    general_channel = client.get_channel(YOUR CHANNEL HERE)

    if message.content.startswith('$week '):
        workout_message = message.content.split('$week ',1)[1] 

        if workout_message.startswith('1'):
            workout_message = message.content.split('1 ',1)[1]   
            if workout_message == "ohp":      
                for item in weekOne(press_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "deadlift":      
                for item in weekOne(deadlift_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "bench":      
                for item in weekOne(bench_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            
            if workout_message == "squat":      
                for item in weekOne(squat_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1



        if workout_message.startswith('2'):      
            workout_message = message.content.split('2 ',1)[1]    
            if workout_message == "ohp":      
                for item in weekTwo(press_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "deadlift":      
                for item in weekTwo(deadlift_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "bench":      
                for item in weekTwo(bench_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            
            if workout_message == "squat":      
                for item in weekTwo(squat_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1


        if workout_message.startswith('3'):   
            workout_message = message.content.split('3 ',1)[1]   
            if workout_message == "ohp":           
                for item in weekThree(press_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            if workout_message == "deadlift":      
                for item in weekThree(deadlift_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "bench":      
                for item in weekThree(bench_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            
            if workout_message == "squat":      
                for item in weekThree(squat_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1


        if workout_message.startswith('4'):     
            workout_message = message.content.split('4 ',1)[1]    
            if workout_message == "ohp":
                for item in weekFour(press_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            if workout_message == "deadlift":      
                for item in weekThree(deadlift_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1

            if workout_message == "bench":      
                for item in weekThree(bench_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1
            
            if workout_message == "squat":    
                for item in weekThree(squat_1RM):
                    currentset = 1
                    await general_channel.send(f"Set #{currentset}: " + str(item))
                    currentset += 1


client.run(YOUR BOT TOKEN HERE)