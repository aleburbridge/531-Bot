## What does it do?
This bot takes your 1-rep maxes for the four main lifts and then generates sets and reps for whatever day you happen to be on

![531 table](https://i.imgur.com/ZybK3BJ.png)

As per Wendler's recommendation, this bot takes 90% of your 1-rep max and then generates the working weight based on that percentage

Since the calculations usually don't result in nice 5lb increments, the weight is automatically round up or down to the nearest plate size

## Usage
Type `$w{week number} {lift}` to get the bot to respond with your sets for the day

For example, if you were on **week 2** and it was **deadlift** day, you would type `$w2 deadlift`

To get your current maxes without having to open up the python file, type `1rm` 
!![1rm](https://i.imgur.com/msBwILP.png)

# How to get started 
If you don't have [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) installed, navigate to the folder containing the *531-Bot* files and run `pip install -r requirements.txt`


Add the bot to your server (I recommend a personal server so your friends aren't overloaded with notifications). If you don't know how to add a discord bot to a server, check out [this tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)

Replace the API key and Channel ID in the source code and enter in your 1-rep maxes (raw numbers, the program will convert them to  their 90% values)

Run the .py file and badabing badaboom

## A final note ~
I believe the world would be a better place if nobody ever had to read anything Jim Wendler has written (especially his 5/3/1 "book"). Hopefully this tool contributes to that effort. E


