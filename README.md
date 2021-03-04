# 5/3/1 Bot
Look, I love Jim Windler's 5/3/1 weightlifting program as much as the next bootlicking gym rat, but pulling out the calculator in between every set really kills the preworkout buzz

And as handy as the [online calculators](https://blackironbeast.com/5/3/1/calculator) are, who has the time for all those input fields? 

That's where the 5/3/1 bot comes in 

## What does it do?
This bot takes your 1-rep maxes for the four main lifts and then generates sets and reps for whatever day you happen to be on

![531 table](https://i.imgur.com/ZybK3BJ.png)

As per Wendler's recommendation, this bot takes 90% of your 1-rep max and then generates the working weight based on that percentage

Since the calculations usually don't result in nice 5lb increments, the weight is automatically round up or down

## Assistance work 

## Plate Math 

# How to get started 
First, you'll need to have [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) downloaded

This can be done easily from terminal using `pip install discord`

If you don't know how to add a discord bot to a server, I recommend [this tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)

Replace the API key and Channel ID strings in the source code with your respective strings
## Usage
Type `$w{week number} {lift}` to get the bot to respond with your sets for the day

For example, if you were on **week 2** and it was **deadlift** day, you would type `$w2 deadlift`

To get your current maxes without having to open up the python file, type `1rm` 
!![1rm](https://i.imgur.com/msBwILP.png)

I believe it would be a great service to the world if nobody ever had to read anything Jim Wendler has written (especially his 5/3/1 "book"). Enjoy the bot and enjoy your gains
