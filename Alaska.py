
@bot.slash_command(name='alaska', description='get a picture of alaska, use 0 for a random picture')
async def test(inter:ApplicationCommandInteraction, numb:int=0):
    alaska = [["really?", "images/alaska1.jpg"], ["Well hello there", "images/alaska2.jpg"], ["Go away", "images/alaska3.jpg"], ["Tounge out tuesday", "images/alaska4.jpg"], ["Treat?", "images/alaska5.jpg"], ["Warm kitty, sleepy kitty, little ball of fur", "images/alaska6.jpg"], ["Come here often?", "images/alaska7.jpg"], ["Purr, purr, purr", "images/alaska8.jpg"], ["I will get you for this", "images/alaska9.jpg"], ["HI!", "images/alaska10.jpg"]]
    if numb == 0:
        r1 = random.randint(0, 10)
        my_filename = alaska[r1-1][1]
        with open(my_filename, "rb") as fh:
          img = disnake.File(fh, filename=my_filename)
        await inter.send(alaska[numb-1][0], file=img); 
    else:
        my_filename2 = alaska[numb-1][1]
        with open(my_filename2, "rb") as fh2:
          img2 = disnake.File(fh2, filename=my_filename2)
        await inter.send(alaska[numb-1][0], file=img2);  
