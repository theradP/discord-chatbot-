import os
from googlesearch import search
import discord
import json
from dotenv import load_dotenv
import sqlite3

# connecting to the db

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='search_history' ''')

# checking whether a database is already present or need to create a new one
if c.fetchone()[0] != 1:
    conn.execute('''CREATE TABLE search_history
             (HISTORY        TEXT    NOT NULL);''')

# loading the environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# connecting to the discord client
client = discord.Client()

# to notify us once the bot connects with discord
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# handle replies  to messages present in the problem statement
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # to reply to a user's greeting
    if message.content.startswith('hi'):
        await message.channel.send('hey')

    # to search the google for the given keyword or phrase
    if message.content.startswith('!google'):
        query = message.content.replace('!google ', '')
        c.execute('''INSERT INTO search_history(HISTORY) VALUES(?);''', (query,))
        conn.commit()
        result = search(query, tld="com", num=5, start=0, stop=5, pause=2)
        result = json.dumps(list(result)).replace('[', '').replace(']', '')
        await message.channel.send(result)

    # to check our search history for the given keyword
    if message.content.startswith('!recent'):
        query = message.content.replace('!recent ', '')
        query = '%'+query+'%'
        c.execute('''SELECT * FROM search_history WHERE HISTORY LIKE (?)''', (query,))
        result = json.dumps(c.fetchall())
        result = result.replace('[', '').replace(']', '')
        await message.channel.send(result)


client.run(TOKEN)