from numpy import character
import datetime
import wikipedia
import pandas
import webbrowser 

solsticeclancats = pandas.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vREzwVYgNn9fMWkbWZkBjfR7wyq8cJZHhNJZNsZwl7q9I74dd2wcnHI1L7pp0cZ3efWyI288pxI938P/pub?output=csv')
mecheartcats = pandas.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRH1ffZviTAzoOy9SqErVR2GmAydqPwSTcZHcOZH8bR9RKcPnPeQ_c7GNTYElCVKkYRJXM32KjBxwE-/pub?output=csv')
celestialclancats = pandas.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRQxuVrni8D2NFcyXW2E3ox-MQQ9hFmKLGiWmzFfHpgahblK-qfJ7uvv0zEfoZoZQUwwPBfPfZcA1-q/pub?output=csv')
wickedclancats =pandas.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTltZ11jnjhEZEvjkfJX6Ty9CWC0vBcM7zOMVT59gNmbgftmWzyPToR6YLt1QkVOzQWmV2CnRFLha20/pub?output=csv')

def findcccharacter(command):
    cccharacter = celestialclancats[celestialclancats['Character Name'] == command.capitalize()]['Character Name']
    cccharacterdescription = celestialclancats[celestialclancats['Character Name'] == command.capitalize()]['Bio']
    return(cccharacter.iloc[0], cccharacterdescription.iloc[0])

def findwccharacter(command):
    wccharacter = wickedclancats[wickedclancats['Character Name'] == command.capitalize()]['Character Name']
    wccharacterdescription = wickedclancats[wickedclancats['Character Name'] == command.capitalize()]['Physical Description (one sentence long)']
    return(wccharacter.iloc[0], wccharacterdescription.iloc[0])

def findmhcharacter(command):
    mhcharacter = mecheartcats[mecheartcats['First Name'] == command.capitalize()]['First Name']
    mhcharacterdescription = mecheartcats[mecheartcats['First Name'] == command.capitalize()]['Bio']
    return(mhcharacter.iloc[0], mhcharacterdescription.iloc[0])


def findsccharacter(command):
    sccharacter = solsticeclancats[solsticeclancats['Character Name'] == command.capitalize()]['Character Name']
    sccharacterdescription = solsticeclancats[solsticeclancats['Character Name'] == command.capitalize()]['Physical Description (one sentence long)']
    return(sccharacter.iloc[0], sccharacterdescription.iloc[0])


def talk(command):
    command = command.lower()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return("You're either on a computer or a phone right now. Look it up yourself....ugh"+ 'The Current time is ' + time)
    elif 'hello' in command:
        return("Need something?")
    elif 'how are you' in command:
        return("Talking to you, so not great..... but thanks for asking.")
    elif 'meaning of life' in command:
        return("42")
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        return(info)
    elif 'cake' in command:
        return("The cake is a lie")
    elif 'your name' in command:
        return('I am Starstar. The best bot. ')
    elif 'gonna call' in command:
        return('GHOST RACER')
    elif 'make a character' in command:
            return("STEP ONE->PICK A CLAN \n Pick what clan or roleplay group your character will call home. On Sinister Haven there are four groups that you can choose from: CelestialClan, SolsticeClan, WickedClan and Mechanical Heart. To get more information about each of these groups, check out their pages! The links to them are located on the side navigation bar. \n                    STEP TWO->CHARACTER SUBMISSION. \n To help you get started roleplaying quickly, go to clan's member page that you would like to join. On that page is a character                    submission form. Just fill it out and hit submit! It is that simple! \n STEP THREE->FORMAL ACCEPTANCE. \n After hitting submit your character will automatically show up on the member page in the appropriate section, with a pending symbol                    next to their name. You may go ahead and begin roleplaying your character at this time. The clans leader will look over your description,                    and accept the character or message you with changes that need to be made. After being formally accepted to the clan, the pending symbol beside of their name on the member page will be removed.")
    elif 'open celestialclan' in command or 'open cc' in command:
        webbrowser.open("http://sinisterhaven.com/index.php?act=Pages&pid=12")
        return("http://sinisterhaven.com/index.php?act=Pages&pid=12")
    elif 'open solsticeclan' in command or 'open sc' in command:
        webbrowser.open("http://sinisterhaven.com/index.php?act=Pages&pid=17")
        return("http://sinisterhaven.com/index.php?act=Pages&pid=17")
    elif 'open wicked' in command or 'open wc' in command:
        webbrowser.open("http://sinisterhaven.com/index.php?act=Pages&pid=21")
        return("http://sinisterhaven.com/index.php?act=Pages&pid=21")
    elif 'open mechanical' in command or 'open mh' in command:
        webbrowser.open("http://sinisterhaven.com/index.php?act=Pages&pid=24")
        return("http://sinisterhaven.com/index.php?act=Pages&pid=24")
    elif 'go away' in command:
        return("Fine then, be that way. Back to my corner...")
        exit()
    elif 'you love me' in command:
        return("no")
    elif 'celestialclan like' in command:
        return("CelestialClan members are known as celestes, servants for cat kind. They are islanders living along the coast. When the celestes realized that there is a innate strength inside of them to build harmony they decided to dedicate their lives to taking in the outcasts, healing the sick, rehabilitating the cruel, and avoid discriminating others because it’s who the people of CelestialClan are to be the heaven on earth that people need.")
    elif 'soslticeclan like' in command:
        return("SolsticeClan devoutly worships the Sun Goddess and the Moon God who they believe create order through their differences. Mirroring their Gods, SolsticeClan divided itself: the Sun Warriors are the fighters and hunters, while the Moon Warriors are the healers and the artists. These cats are an insanely proud bunch and love nothing more than to display their accomplishments, all in the honor of their Gods. As such, SolsticeClan sports an open border policy and then some, by offering kit-sitting services and free classes for any outsider who abides by their rules. Generally they are regarded as friendly and intelligent, true scholars of the natural and supernatural, but be warned - for as kind as SolsticeClan cats seem to be, they do have a darkside. They will not hesitate to brutally slay anyone who threatens their peace.")
    elif 'wickedclan like' in command:
        return("WickedClan is well named. All of the other groups view them as evil or morally bad, the type of cats born with a bad disposition that runs deeper than blood, who want nothing more than to cause harm to those who do not agree with them. In truth this group is incredibly secretive and distrustful of others, but not necessarily rotten to the core as the rumors say. ")
    elif 'mechanical heart like' in command:
        return("The innovators, the creators, and the go-getters: Mechanical Heart cats are by nature curious and ambitious. They are laser-focused on collecting as much knowledge as they can and creating new things, from steampunk-style replacement limbs to handy devices akin to a roomba. They have obsessive personalities, and, once they start a project, don’t stop until it’s complete - focusing solely on their goals even as they eat and sleep. ")
    elif 'sinister haven like' in command:
        return("I'm contractually obligated to say that it is the hottest new Warrior Cats fantasy rp site on the block, even though I'm not entirely sure why any of these characters have to be cats anymore.")
    elif 'diamond blood' in command:
        return("Diamond blood is glittery and reflective, and it can appear rainbow. These cats are seen as superior and frightening, and they possess the most powerful magic.")
    elif 'emerald blood' in command:
        return("Emerald blood is a brilliant green color. These cats are seen as miraculous and strong contributors to the clan. Their magic is of normal strength.")
    elif 'amethyst blood' in command:
        return("Amethyst blood is a violet purple color. These cats have weak magic and are seen as inferior and disappointing.")
    elif 'amber blood' in command:
        return("Amber blood has a warm orange luster. These cats are useless failures; they have no magic.")
    elif 'best site' in command:
        return("Sinister Haven")
    elif 'gene' in command:
        return("Gene is mean. He takes my cookies")
    elif 'stay up' in command:
        return("You should go to bed before dad grounds you")
    elif 'what are you' in command:
        return("An intelligent being, unlike you.")
    elif 'who are you' in command:
        return("Starstar. Can you people even read?")
    elif 'where are you' in command:
        return("On Discord, unfortunately.")
    elif 'do you like me' in command:
        return("Not sure who you are, but I'm going to say 'no' because coming up with a custom answer for literally every member of this server would take forever and I'm not down for that")
    elif 'why are you here' in command:
        return("Apparently to answer stupid questions.")
    elif 'favorite movie' in command:
        return("Wall-E")
    elif 'favorite tv show' in command:
        return("Wipe Out")
    elif 'favorite musical' in command:
        return("Cats (the bad one)")
    elif 'favorite youtuber' in command:
        return("I'll reserve my answer until one of them sponsors us")
    elif 'best warrior name' in command:
        return("Starstar")
    elif 'worst warrior name' in command:
        return("Also Starstar. I am the Alpha and the Omega")
    elif 'clan should i join' in command:
        return("CeleSolWickclan Heart ")
    elif 'favorite book' in command:
        return("Cat in the hat.... What? Did you think I was going to say warriors?")
    elif 'favorite character' in command:
        return("Ha! Good try, but I'm not telling you who writes these.")
    elif 'think of cleaver' in command:
        return("Cool Pokemon, I like the design. I'm glad they gave Scyther more love, it's a seriously underrated bug type.")
    elif 'think of racer' in command:
        return("NASCAR's pretty cool, I guess. It's funny when the cars go crash.I only know one specific racer though.")
    elif 'think of sen' in command:
        return("Sen (noun): a monetary unit of Brunei, Cambodia, Indonesia, and Malaysia, equal to one hundredth of a dollar in Brunei, one hundredth of a riel in Cambodia, one hundredth of a rupiah in Indonesia, and one hundredth of a ringgit in Malaysia. ")
    elif 'think of jade' in command:
        return("Fun fact: there are actually two types of Jade, nephrite and jadeite. It's believed to be a symbol of good fortune for many cultures in Southeast Asia. So it's kinda cool, I guess.")
    elif 'think of faith' in command:
        return("I think that faith is, in essence, a defining part of what shapes humanity as a race. How much of history and culture has been shaped by humanity's enduring belief in a higher power? How much have people overcome by simply trusting and believing in one another? It is the ability to have such an unwavering confidence in ourselves, one another, and in a higher power that separates and defines us as creatures of reason and hope. ")
    elif 'think of' and 'admins' in command:
        return("Oh, them? They're alright, I guess. They give me cookies from time to time")
    elif 'old are you' in command:
        return("I don't know")
    elif 'favorite child' in command:
        return("Racer of course")
    elif 'favorite drink' in command:
        return("bepis")
    elif 'favorite food' in command:
        return("cookies")
    elif 'want' and 'cookie' in command:
        return("Give. Now.")
    elif 'favorite color' in command:
        return("clear")
    elif 'favorite animal' in command:
        return("You're _kitting_, right?")
    elif 'faith' in command:
        return("Faith is the mother of the SH admin family with her darling three children who can do no wrong, definitely not, and wife to her loving husband")
    elif 'cleaver' in command:
        return("Cleaver is the reluctant father of two admin children & husband to their incredible mother")
    elif 'sen' in command:
        return("Sen is the edgy eldest child of the trio, and enabler the younger two's bad behavior")
    elif 'racer' in command:
        return("Racer is the angelic middle child of the SH admin family, and dad's favorite child. She REFUSES to share her title as middle child, no matter how many kids mom decides to adopt..")
    elif 'jade' in command:
        return("Jade is known as the youngest (unwanted) child, which explains why she thinks she is everyone's favorite.")
    elif 'who is deal' in command:
        return("Dad!")
    elif 'who is starstar' in command:
        return("The bestest bot ever")
    elif 'who is mom' in command:
        return("Faith!")
    elif 'who is dad' in command:
        return("Cleaver!")
    elif 'who is' in command: 
        command = command.replace("who is", "")
        command = command.replace(" ", "")
        command = command.replace("?", "")
        print("looking up", command)
        try:
            name, bio = findsccharacter(command)
        except:
            print("not in sc")
            try:
                name, bio = findcccharacter(command)
            except:
                print("not in cc")
                try:
                    name, bio = findwccharacter(command)
                except:
                    print("not in wc")
                    try:
                        name, bio = findmhcharacter(command)
                    except:
                        return("I don't know who that is either.")
        return str(name + "\n" + bio) 
    else:
        return('Please say the command again.')
