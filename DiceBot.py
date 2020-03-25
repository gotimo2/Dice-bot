#imports

import discord
import os
import random

#declarations
client = discord.Client()
TOKEN = ''

#actual bot
@client.event
async def on_message(message):
    global store    #declare global variables
    global mess
    mess = ''   #mess = message
    if message.content.startswith('//dr'): #is message starts with //dr  
        store = 0   #empty the sum storage
        num = message.content.lstrip('//dr') #remove //dr    
        dice = [int(i) for i in num.split() if i.isdigit()] #take every number from the message into a list
        if 1 in dice: #if the list contains a 1
            await message.channel.send('can\'t roll a 1-sided dice!') #not so politely tell user that a one-sided dice is impossible
            return  #stop because you're better off doing //dr again than having a messed up dice list
        for n in dice:  #for every entry in the dice
            out = random.randrange(1,n) #pick a random between 1 and the dice picked
            store = store + out #add the result to store for //sum
            mess = str(mess + str(out) + '  ')  #construct a message with what every dice landed on
            final = f'You rolled: {mess}' #construct a proper message from that
        await message.channel.send(final)   #send the message
    if message.content.startswith('//sum'): #check if message starts with //sum
        await message.channel.send(f'the sum of the last roll is {store}') #reply with the value in store


#echo to console when connected
@client.event
async def on_ready():
    print(f'connected to discord as {client.user}!')

#run the bot
client.run(TOKEN)