import os
from dotenv import load_dotenv
import nextcord
import pandas as pd
import math
import sklearn.metrics
import fnmatch
import random
from datetime import datetime
import nextcord


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = nextcord.Client(intents=nextcord.Intents.all())


verification = pd.read_csv('./test.csv')

deepbot_messages = [
    'beep beep ...',
    'ugh not again...',
    'Purple pe... i i mean hi',
    'jiji ya blid',
    'Hello Hello',
    'Sup losers?',
    'My favorite team! just kidding, youre all the same to me.',
    'One RMSE score request right away!',
    'Calculating your RMSE ...',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??',
    'wheres my fucking submission Lebowski??'
]

deepbot_custom_team_messages_ = {
    'hack-team-1': [],
    'hack-team-2': [],
    'hack-team-3': [],
    'hack-team-4': [],
    'hack-team-5': [],
    'hack-team-6': []
}

deepbot_congratulations = [
    'YES! UP THE LEADERBOARD',
    'tajmou tadherbou jiji',
    'CONGRATS',
    'UP UP UP!',
    'We like to see that RMSE going down!',
    'Good job losers!'
]

deepbot_online = [
    'back!',
    'Is anybody here?',
    'back babyyyy',
    'Ya boi is back!'
]


deepbot_hints=[
    'start with a baseline',
    'You can use more than one model ;)',
    'tssaref wa7dek',
    'tssaref wa7dek',
    'tssaref wa7dek',
    'tssaref wa7dek',
    'tssaref wa7dek',
    'use HUE',
    'feature engineering on the date',
    'try combining features (one specific shop combined with a specific banner)'
]

def calculate_rmse(sub_df, verif_df):
    merged = sub_df.merge(verif_df, on="campaign_id", how='inner')
    merged.to_csv('hola.csv', index=False)
    x = merged['budget_x'].tolist()
    y = merged['budget_y'].tolist()

    mse = sklearn.metrics.mean_squared_error(x, y)
    rmse = math.sqrt(mse)
    return rmse


def count_subs(dir_path):
    return len(fnmatch.filter(os.listdir(dir_path), '*.*'))


def update_stats(team, rmse):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    old_stat = pd.read_csv('./stats.csv')



    data = {'Team': [team],
             'RMSE': [rmse],
             'Time': [dt_string]}
    sub = pd.DataFrame(data)
    

    new_stat = pd.concat([old_stat, sub]).drop_duplicates(
        subset=['Team', 'RMSE'])
    new_stat.sort_values(by=['RMSE'],ascending=True,inplace=True)

    try:
        current_rank = old_stat[old_stat.Team==team].first_valid_index()
        new_rank = new_stat[old_stat.Team==team].first_valid_index()
        prog = new_rank - current_rank
    except:
        prog = 0
    new_stat.to_csv('stats.csv',index=False)
    return prog



def print_leaderboard():
    data = pd.read_csv('./stats.csv').iloc[:15,:]
    msg = 'Team\tRMSE\n'
    for index, row in data.iterrows():
        msg += f'{row["Team"]}\t{row["RMSE"]}\n'
    return msg



@client.event
async def on_ready():
    msg = random.choice(deepbot_online)
    msg  = 'Use !hint, I may be able to help ;)'
    await client.guilds[0].text_channels[0].send(msg)

@client.event
async def on_message(message):
    if message.content == '!hey':
        msg = random.choice(deepbot_messages)
        print(random.choice(deepbot_messages))
        await message.channel.send(msg)
    elif message.content =='!hint':
        await message.channel.send(random.choice(deepbot_hints))

    """if message.attachments:
        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".csv"):
            dir_path = f'./submissions/{message.channel}'
            new_file_name = f'{dir_path}/sub_{count_subs(dir_path)}.csv'
            await message.attachments[0].save(fp=new_file_name)
            sub = pd.read_csv(new_file_name)
            rmse = calculate_rmse(sub, verification)
            prog = update_stats(message.channel.name, rmse)
            await message.channel.send(f'{random.choice(deepbot_messages)}\n\n')
            if prog > 0:
                msg = f'RMSE: {rmse}\n\n{random.choice(deepbot_congratulations)}'
                await message.channel.send(msg)
            else:
                await message.channel.send(f'RMSE: {rmse}')
    elif message.content == '!leaderboard':
        msg = print_leaderboard()
        await message.channel.send(msg)
    else:
        print(message.content)"""


client.run(TOKEN)

