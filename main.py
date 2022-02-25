import discord
import os
from keep_alive import keep_alive
import requests
import re
import time
from discord.ext import tasks, commands


keep_alive()




url = 'https://br.leagueoflegends.com/pt-br/news/game-updates/'



myfile = requests.get(url)
open('myfile', 'wb').write(myfile.content)


def my_function():


  with open("myfile",'r') as f, open('output.txt','w') as fw:
      text = f.read()
      result_string = ''

      words = ["notas", "atualização"]
      text2 = text.split(".")
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      result_string += text2[itemIndex][1:]+'.'
                      break
                  else:
                      print(text2[itemIndex])
                      result_string += text2[itemIndex]
                      break
      fw.write(result_string)

my_function()

def get_version():
 
 with open("output.txt",'r') as f,  open("array.txt","r") as g, open('version.txt','w') as fw, open('patch', 'w') as pv:

  regex = r"notas-da-atualizacao-(\d+\-\d/)"

  test_str = f.read()
  version_str = g.read()

  matches = re.finditer(regex, test_str,)
  matches_2 = re.finditer(regex, version_str)

  for matchNum, match in enumerate(matches, start=0):
    
    print_url = ("Achado: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    print(print_url)
    pv.write("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    

    for matchNum, match in enumerate(matches_2, start=1):
    
      print_array = ("Achado: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
      print(print_array)
    
    
      if print_url != print_array:
        fw.write ("versão {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        print("Desatualizado!")
      else:
        print("Atualizado!")

get_version()

def my_url():


  client = discord.Client()
  with open("patch",'r') as f, open ('url.txt', 'w') as fw:
    version = f.read()
    url_patch = "https://br.leagueoflegends.com/pt-br/news/game-updates"
    final_url = f'{url_patch}/{version}'
    fw.write(final_url)



  @client.event 
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    with open("version.txt",'r') as f, open('compare.txt', 'r') as p:
      if f.read() != p.read():
        channel = client.get_channel(833146714222362674)
        await channel.send(final_url)
       

  
  
  client.run(os.getenv('TOKEN'))


my_url()


while True:  
    start_time = time.time()
    seconds = 120
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        my_function( )
        get_version()
    else:
      break