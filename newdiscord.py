import discord
import datetime
import requests
import openpyxl
import asyncio
from json import loads
import shutil
import logging
import traceback
import configparser

client = discord.Client()
game = discord.Game("쥬키 빙구")



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "Uddoong"
    name = "유뚱"
    channel = client.get_channel(682980729793413142)
    a = 0
    while True:
        headers = {'Client-ID':'r38xow70x0v6vtsf9tn6cffri8oplq'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text) ['data'][0]['type'] == 'live' and a ==0:
                await channel.send(name + "님이 방송중입니다.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)




@client.event
async def on_message(message):
    if message.content.startswith("L 안녕"):
        await message.channel.send("잘가(?)")
    if message.content.startswith("L 그래"):
        await message.channel.send("뭐가?")
    if message.content.startswith("L 넌 누구야"):
        await message.channel.send("아직까진 개발중인 Test 봇이야!")
    if message.content.startswith("L BF5 정보"):
        await message.channel.send("정보:바보")
    if message.content.startswith("L 쥬키 정보"):
        await message.channel.send("정보:멍청이")
    if message.content.startswith("L 눈이 안보여요"):
        await message.channel.send("https://youtu.be/yyGuXIzVu2I")
    if message.content.startswith("L 의 답장"):
        await message.channel.send("싫어요 안되요 하지마세요")


    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)


    if message.content.startswith('L!내정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed=discord.Embed(color=0x00ff000)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)


    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)
        role = discord.utils.get(message.guild.roles, name="D_P")
        await author.remove_roles(role)
        role = discord.utils.get(message.guild.roles, name="D_P Red")
        await author.remove_roles(role)


    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="D_P")
        await author.add_roles(role)
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)


    if message.content.startswith('경고 부여'):
        author = message.guild.get_member(int(message.content[9:27]))
        file = openpyxl.load_workbook('경고.xlsx')
        sheet = file.active
        why = str(message.content[28:])
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author):
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send(str(author) + "님은 경고 3회누적으로 서버에서 추방되었습니다.")
                else:
                    await message.channel.send(str(author) + "님은 경고를 1회 받았습니다")
                    sheet["c" + str(i)].value = why
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = why
                file.save("경고.xlsx")
                await message.channel.send(str(author) + "님은 경고를 1회 받았습니다.")
                break
            i += 1


client.run('NjgzNjI4MTI4MDk4MTg5MzEz.Xm3SgQ.G4-smRNP41-x0FbhrtIiqbHsSTs')



