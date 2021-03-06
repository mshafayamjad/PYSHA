import datetime  # Importing the datetime for the timing modules since the date time is used to answer the questions
import wave  # Importing the wave of for the recording(This is the format for the recording which is used .wav
from random import *  # Using the random  function for the creation
import pyaudio  # importing the header file of the pyaudio
import speech_recognition as sr  # Importing the speech recognition file for the code.!!
# from .PygletMusic.Pygletimplementation import *  # Music player GUI implemented
from _Joke import *
from _NaturalLanguageProcessing import *
from _WolFrameAlphaClass import *  # For computation and intelligence engine.
from __soundcloud import *
from __speakcode import *  # For speaking the code from the web scrapping .
from _dbdata import *  # Database function for the request and all others
from _stackoverflow import *  # Stackoverflow
from _twitter import *  # imports the twitter Pysha client which has been
from _youtube import *  # imports youtube created local header file , for searching on youtube
from __github import *
from _SocialMedia import *  # importing the social media moduel for the implementation of the social medias
from _TextMode import *  # the text mode will be used for the messaging application like look, like a bot
from AssistantProperties import _chooseassitant  # importing the properties of the assistant being choosen.
import random  # importing the random module for the random Short term memory
from __shorttermmemory import *
from Chatdependencies._chat import *  # importing the _chat module

# imports the short term memory code  --> for getting the last strings backs 7 +-2
# this si the importing of the header files !
# Pre requirements : You need to Install Microsoft SDK fo Speech and all the available Tools
# Keep in mind that This is Under Heavy Construction and will be used in the later increments and

'''
// This build is heavily under progress by Muhammad Shafay Amjad, If you want to check all the dependencies,
and want to contribute to improve the particular algorithm, check Repository.
https://github.com/shafaypro/PYSHA1.0
Info Dated: 2/3/2016  , WaterFall method is being Followed

User Guideline:

Wherever you run this Project, the basic dependencies are converted in to the local machine,

--> The machine tells about her self and then wait for the user to have the specified an speech input,

The device of the microphone is connected and then it is parsed to the pyaudio where the input is then

Converted to the Audio file  Formatted as WAV, under the F.L.A.C encoding, then it is parsed to the google api,

since the api is then accessed and the chunks of the audio is converted into the string and then returned into the
string.

There are some already stored procedures for the particular messages , like if a message starts from the :::

what is the ----> Time, Date and others can tell you the the time ,date and others.
Ther are some other features also added in the header file , like haviing a random chat and working on different kind of
Loops

you can ask for the questions and the Answers regarding to the Natural language processing module .

If you want to ask for the Application running modules then
for that :
RUN or OPEN _________ the Underscore should be replaced by the application name
--> This script will also be monitroing the computer (Here it contains the data analysis and the data visualization part
This will be including the statistical analysis and well as the sentimental analysis . ! so that this may be used in the
 later
sequences of the version
--> ask for any operation ,, if other than all of the above , it will
--> You can ask the Mathematical operation as : 2+ 3 or integeration of 4 or General Knowledge.
--> Since It can also be asked the general knowledge questions like : who was the  6th president of Unitedstates


!!!!!!!!!!!!!!!!!!!!!!!EXAMPLE QUESTIONS !!!!!!!!!!!!!!!!!!!!!!!!
Who won the Election of 2016 in United states ?
Who wrote the book The lord of the Flies ?
What is the meaning of life ?
What is the meaning of Nostalgia?
bread <-- This will return the Other Requirements


--------------------------Example Programming Solution-----------------------
ask --> Stack over flow search _____________
______ replace this with your query
ask--> search youtube ____________ or youtube _________________
search youtube ___________________
______ replace this with your query
or youtube ___________________

ask--> search music _____________ or find music _______________
_________ replace this with your song name of artist or any :p

ask--> Read it out to me      or Read it out for me
# This will read all the text from the last visited page
ask --> switch to _______   : replace the _________ with Female , male , dave , hazel , zira

ask --> tweet __________________  : posts a tweet on twitter.

ask --> search  music ________________ : searched the music.

ask --> find music _______________ : finds the music from the internet.

ask --> search for ________________ : searches on google

ask --> launch ___________________ or RUN ______________ : runs the define application.

ask --> read it out for me : reads the last visited page

ask --> Search for _________: This opens up the browser for the result so that the Virtual assistant is able to read
from the
data
ask --> web __________________ : opens the particular website.
ask --> Stop,stop listening,quit : This will results in the Quiting , exiting for the virtual assistant!!

ask --> search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)

ask --> show me a comic : finds a comic from the internet and displayed the comic

ask --> tell me a joke : Finds a joke from the web and shows the joke
-ask --> what is the date / what is the time
 -
 -
 -ask --> What is the integeration of 2 x squared + 3 x + 7
 -
 -
 -ask --> which is greater in quantity 1 liter of water or 1 liter of milk
 -
 -
 -ask --> Stack over flow search _____________
 -
 -
 -______ replace this with your query
 -
 -ask--> search youtube ____________ or youtube _________________
 -
 -
 -ask--> searh youtube playlist _________ : ___ is the query of yours
 -
 -search youtube ___________________:  -______ replace this with your query
 -
 -or youtube ___________________
 -
 -ask--> search music _____________ or find music _______________ : replace ___ with your song name or artist or both
 
 -ask--> Read it out to me      or Read it out for me
 
 -# This will read all the text from the last visited page
 
 -ask --> switch to _______   : replace the _________ with Female , male , dave , hazel , zira
 
 -ask --> tweet __________________  : posts a tweet on twitter.
 -
 -ask --> search  music ________________ : searched the music.
 -
 -ask --> find music _______________ : finds the music from the internet.
 -
 ask --> play music  : plays the music
 -
 -
 ask --> Music Please : plays the music
 -
 -
 ask --> music video please : plays a music video
 -
 -
 -ask --> search for ________________ : searches on google
 -
 -
 -ask --> launch ___________________ or RUN ______________ : runs the define application.
 -
 -
 -ask --> read it out for me : reads the last visited page
 -
 -
 -ask --> Search for _________: This opens up the browser for the result so that the Virtual assistant is able to read from the
 -data
 -
 -
 -ask --> Stop,stop listening,quit : This will results in the Quiting , exiting for the virtual assistant!!
 -
 -
 -ask --> search ________ on Wikipedia : will search on wikipedia based on certain meaningful words(replaces at _____)
 -
 -
 -ask --> show me a comic : finds a comic from the internet and displayed the comic
 -
 -
 -ask --> tell me a joke : Finds a joke from the web and shows the joke
 --
 -ask --> tokenize sentence ____________________________ : will returned a tokenized sentence 
 
 -ask --> tokenize sentence ____________________________ : will returned a tokenized sen
 -
 -
 -ask --> What did i just said : returns the last query from the short term memory(termed as the top runned query --> the last most)
 -
 -ask --> What did i said you:  Returns maximum from the shrot term memory(last 7+-2 statments ) as per human brain. 
-

'''
# TODO : Working on EMAILS, MESSENGERS, OPEN CV, IMAGE RECOGNITION, NATURAL LANGUAGE PROCESSING, MACHINE LEARNING, DB
# TODO : SELF LEARNING, additonal Chat properties


''' Keep in mind to have all the back up things,
For the personal computer you need to have the computer access,
And all the other things given to the Assistant so that it can work in there.
'''

# TODO : USE THE IBM WATSON TOO, To improve the Virtual Assistant
__author__ = "M Shafay Amjad"
__QA__ = "mshafayamjad@gmail.com"
__version__ = 1.0
__productname__ = "PYSHA"
# TODO : File Information needs to be implemented


# The reverse shell process is for personal use, where we will be using to ping the Updated Code, to your Home location
# Computer Code!
'''
This is the personal Computer Reverse shell!
'''


class PYSHA_CLASS:
    db = NONE
    lastlink = ""  # just to be reminded for the last link visited
    engine = pyttsx.init()  # intializing the engine here so that there are global engine speech , which can be changed
    py_chat_bot = Chatting_PYSHA(name="PYSHA", trainable=True, train_corpus=True)  # intialized the Chatting Pysha

    def __init__(self):

        print("PYSHA INITIALIZED!")
        self.createlocaldb()  # this creates the localdb for requests

    # creating the local Database

    def shortterm_check(self, limit=0):
        stm_list_recieved = stmcheck()  # calls the stm check module
        list_recieved = display_stm(stm_list_recieved)  # Filterening all the sentences and specifying the current list
        if limit == 0:
            random.shuffle(list_recieved)  # random shuffling , Using the random shuffle for the current memory
            for i in range(len(list_recieved)):
                self.text_to_speech("You said at " + str(i) + " " + list_recieved[i])
                # just printing the list for the things.
        elif limit == 1:
            self.text_to_speech(list_recieved[0])  # pass the first element inthe list which is the last said.
            # TODO : call the text to speech and speak the list in an specified order

    def createlocaldb(self):
        self.db = db_data()  # this calls the db class
        self.db.create_database()  # this creates the database for the class.

    def play_video(self):
        try:
            os.system("start  E:\\MusicVideos\\Just-So-You-Know.mp4")
        except Exception as E:
            print("check the directory exception", E)

    # TODO : more Accurate apps running
    # for going through the history

    def insert_into_request(self, request_text, responce_text):
        # this is the function responsible for the writing in the history.
        self.db.insert_into_Requests(request_text, responce_text)  # this is twrite into the reposce text

    # For running the apps
    def run_apps(self, text_input=""):
        text_input = text_input.strip()
        if text_input != "":
            if text_input == "calculator":
                os.system('calc.exe')  # Running the calculator in the Operating system
                self.text_to_speech("Calculator launched")
            elif text_input == "notepad":
                os.system('notepad.exe')  # Running the notepad using the Os module for the specified Attrirbute !
                self.text_to_speech("notepad launched")
            elif text_input == "performance monitor":
                os.system('perfmon.exe')  # Launchign the Performance monitor from the exe
                self.text_to_speech("Performance monitor has been launched")
            elif text_input == "smart screen":
                os.system('smartscreen.exe')  # Working on the smart screen and running the Exe !
                self.text_to_speech("smart screen launched ")
            elif text_input == "space agent":
                os.system('SpaceAgent.exe')  # Running the space agent for the
                self.text_to_speech("space agent has been launched")
            elif text_input == "network status":
                os.system('netstat.exe')  # you are working ehre !
                self.text_to_speech("Network status for today have been shown in the screen")
                self.text_to_speech("somethings seems to be off")
            elif text_input == "bluetooth setting":
                os.system('fsquirt.exe')  # you are working ehre !
            elif text_input == "defragment":
                os.system('Defrag.exe')  # you are working ehre !
            elif text_input == 'clean manager':
                os.system("cleanmgr.exe")
            elif text_input == "command prompt":
                os.system("cmd.exe")
            elif text_input == 'direct ex' or text_input == 'direct setting':
                os.system("dxdiag.exe")
            elif text_input == "control panel":
                os.system('control.exe')
            elif text_input == 'resource monitor':
                os.system('resmon.exe')
                # this launched the resource monitor to monitor the resource!
            elif text_input == "game panel":
                os.system('GamePanel.exe')
            elif text_input == 'graphic settings':
                os.system('Gfxv4_0.exe')  # this access the graphic cards
            elif text_input == 'dpi scaling':
                os.system('DipScaling.exe')  # this truns the dpi scalling for the partu
            elif text_input == 'disk partition':
                os.system('diskpart.exe')
            elif text_input == 'python' or text_input == "python interpreter":
                os.startfile(
                    "C:\\Program Files\\Python35\\pythonw.exe")
                # this calls the file location and then run the program of the python.
                # There you should run the pyton programming language
                # so that the language will be specified by the face of the
            elif text_input == "pycharm" or text_input == "python best interpreter":
                os.startfile("C:\\Program Files\\Python35\\Lib\\idlelib\\idle.pyw")
                # --- This runs the pycharm Compiler which can be used for the Html or the python programming
                # The Below function will be used to search on the browser and then show the desire result
            elif text_input == "movie player":
                print("started movie player!!!")
                os.startfile(
                    "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")  # window media player execution!

    # TODO : Exact Searching
    def search_browser(self, text_input):
        print('-searching on browser-')
        try:
            url = 'http://google.com/search?q=' + text_input
            # Creating or generating a google link for the particular file
            webbrowser.open(url)
            return

        except:
            self.text_to_speech(
                "I'm sorry, I couldn't reach google")
            # Calling the Function so that it can be identified that ,machine can speaks for itself
            return

    # The below function is responsible for the search on the Wikipedia

    # searching on the Wikipedia and then asking the pysha to speak the respectable result!!

    # TODO : WIkI Algorithum improvment
    def search_wiki(self, text_input):
        # suggested_string = wikipedia.suggest(text_input)  # now going for the suggestion
        try:
            wiki_page = wikipedia.page(text_input)  # this opens up the wiki page for the particular thing
            # text_to_speech(str(wiki_page.title))  # asking the machine to speak this specified word
            # summary_text = wikipedia.summary(text_input, sentences=4)  # search on the wikipedia!
            wiki_link = str(wiki_page.url)  # Converts the url of the wiki links to the url.
            wiki_images = wiki_page.images  # Gets all the images link references. as a list
            wiki_sumry = wikipedia.summary(text_input, sentences=3)

            print(wiki_sumry)
            # webbrowser.open(wiki_link)  # opens the link on the web browser and then search the specified text link
            self.text_to_speech(wiki_sumry)
            return wiki_link  # this returns the wikilink , keep in mind this is just for reading in the later onward purposes
        except:
            self.text_to_speech(
                "Sorry i couldn't connect to the wikipedia!! nor find a relevant link, there must be a connection problem")
            return

    # The below function is responsible for the running of the chat with the below function
    # This will be used to show the Frontend for the application.

    # There are two dynamic ways for storing the Frontend , since this is a Hit and run trail using the function!
    # The Human computer interaction will be updated according to the software development module!

    # TODO: Frontend HCI needs to be created !
    def frontend_hci(self, label_text):
        root = Tk()  # This created the tkinter , face.!
        root.title("PYSHA 1.0")  # Making the Title for the Py Sha 1.0 ,
        root.geometry("300x300")  # specifying the x and the y axis in the scenario
        label1 = Label(root, text=label_text, font='size,25')  # This is the label insertion for the Tkinter module
        print(label1)  # Showing in the console for the debuggin purposes
        label1.pack()  # Packing up the label1 module in the GUI
        root.after(10000, lambda: root.destroy())  # Destroying after 10 seconds
        root.mainloop()  # Executing the main loop for the Gui Till it gets exited

    # TODO : make the Chat intelligent , using the Natural language processing and AIML (artifical intelligence markup)
    #  language)
    def chat(self, input):
        insults = ["weirdo", "stupid", "weird", "dumb", "idiot", "retard", "retarded", "fat", "lazy",
                   "annoying", "moron", "simp", "big", "ugly", "sad", "wimp", "troll"]
        complements = ["nice", "happy", "good", "smart", "wonderful", "really ", "intellegent", "awesome", "beautiful"]
        ranNum = randrange(1, 4)
        # chatting features of PyDa:
        if input.startswith("do you want to "):
            if ranNum == 1:
                self.text_to_speech("Maybe later")
            if ranNum == 2:
                self.text_to_speech("I don't think that's a good idea")
            if ranNum == 3:
                self.text_to_speech("Yes! lets do it")

        if input.startswith("do you like to "):
            if ranNum == 1:
                self.text_to_speech("Sometimes I do")
            if ranNum == 2:
                self.text_to_speech("No, I hate doing that")
            if ranNum == 3:
                self.text_to_speech("Yes, I do that all the time")

        if input.startswith("i hate "):
            if "Shafay" in input[6:]:
                self.text_to_speech("What? Shafay is the coolest person ever!")
            elif ranNum > 2:
                self.text_to_speech("I think " + input[6:] + " is awesome")
            elif ranNum <= 2:
                self.text_to_speech("I don't like " + input[6:] + ' either')

        words = input.split

        if input.startswith("you are a"):
            if any(input[10:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("Thank you, I know")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you made my day!")
            elif any(input[11:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("Thank you, I know")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you made my day!")

            if any(input[10:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("I know you are but what am i?")
                if ranNum == 2:
                    self.text_to_speech("Don't troll me. bad things will happen")
                if ranNum == 3:
                    self.text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")
            elif any(input[11:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("I know you are but what am i?")
                if ranNum == 2:
                    self.text_to_speech("Don't troll me. bad things will happen")
                if ranNum == 3:
                    self.text_to_speech("sorry, i was to busy, BLOCKING OUT THE HATERS!")

            elif input[10:] or input[11:] not in insults:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")
            elif input[10:] or input[11:] not in complements:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")

        if input.startswith("are you a"):
            if any(input[10:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("yes i am")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you betcha")
            elif any(input[11:].startswith(c) for c in complements):
                if ranNum == 1:
                    self.text_to_speech("yes i am")
                if ranNum == 2:
                    self.text_to_speech("isn't it obvious?")
                if ranNum == 3:
                    self.text_to_speech("you betcha")

            if any(input[10:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("no, are you")
                if ranNum == 2:
                    self.text_to_speech("don't troll me, i eat trolls")
                if ranNum == 3:
                    self.text_to_speech("does it look like i am?")
            elif any(input[11:].startswith(i) for i in insults):
                if ranNum == 1:
                    self.text_to_speech("no, are you")
                if ranNum == 2:
                    self.text_to_speech("don't troll me, i eat trolls")
                if ranNum == 3:
                    self.text_to_speech("does it look like i am?")

            elif input[10:] or input[11:] not in insults or complements:
                if ranNum == 1:
                    self.text_to_speech("I don't know what you mean by that")
                if ranNum == 2:
                    self.text_to_speech("Your words are not in my library")
                if ranNum == 3:
                    self.text_to_speech("No comment")

    # if there is any person question regarding to the Virtual Assistant go for this

    # When there is a question regarding to the self
    # Like the questions given to the Pysha, or the personal question about her !
    # Since , The below Function is an already stored function by the developer, there are some processed required like
    # Machine learning should be implemented in here too, for the particular specific questions
    # TODO : Do some of the Complex parsing
    def Personal_PYSHA(self, text_input=""):
        if text_input == "name":
            self.text_to_speech("PYSHA")
            return
        elif text_input == "age":
            b_date = datetime.date(2016, 10, 24)  # specifing the creation date.
            c_date = datetime.date.today()
            # now subtract the date from the date of creation
            self.text_to_speech(
                (c_date - b_date))  # this prints the age of the Virtual Assistant , which returns the date.
            print((c_date - b_date))
            return
            # Here you need to add the hob
        elif text_input == "hobbies":
            self.text_to_speech("Well i have many hobbies, i will tell you some")
            hobbies = ["Playing a Game", "Collecting your History", "Watching Football"]
            for each_hobby in hobbies:  # Iterating to each of the loops
                self.text_to_speech(str(each_hobby))  # Sending the each string to the Hobbies.
                # This will send all the related hobbies to the specified Place.
        elif text_input == "gender":
            self.text_to_speech("Female")

    # this is the particular day check , that the user will be defining the day check ,since the day
    #  Follows the same day check priciple for the  particular day check<!

    # TODO NOTHING
    def day_check(self):
        current_date = datetime.datetime.now()
        self.text_to_speech("The current date is " + str(current_date.date()))
        return

    # Checking the time for the computer while the

    # IF the user asked for the particular time check , after the text processing this function is called ! ,
    # This later calls the text to speech function using the P.y.t.t.s.x. for the user to speak the particular output !
    # TODO : Nothing
    def time_check(self):
        current_time = time.strftime('%H:%M:%S')
        self.text_to_speech("The time is " + current_time)
        return

    # storing the respectable input for the user  while the computer will be able to use the resources and speak

    # TODO: add sqlite3 database and store the input in the form of the data base
    def store_userinput(self, input_check):
        self.db.insert_into_History(str(input_check))  # this stores and creates a history
        file_out = open("USERINPUT.txt", "a")
        file_out.writelines("USER SAID: \t" + input_check)
        file_out.write("\n")  # ending the line with the next line
        file_out.close()
        return
        # This function will be responsible for storing the responses so that it may able to answer in the future.pute

    # Converting the spoken string to the speech , so that the call is Visible

    # TODO : speech to Text   (Google api, Microsoft Speech recording )
    def speech_to_text(self):
        client_id = ""  # this is the google api client id
        client_secret = ""  # this is the google api client secret key
        api_key = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            CHUNK = 1024
            FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
            CHANNELS = 2  # The Cross Channels
            # RATE = 44100
            source.CHUNK = CHUNK
            source.format = FORMAT  # FORMATING THE SOURCE FILE
            # print(dir(source))
            print("Say something!")
            print(r.energy_threshold)
            r.energy_threshold -= 80
            # print(r.adjust_for_ambient_noise(source,duration=1))
            audio = r.listen(source)

            # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            # print(r.energy_threshold )
            # print(help(r.recognize_google))
            text = r.recognize_google(audio, language='en-US')
            print("You said: " + text)
            self.total_saying = text
            self.process_text_input(self.total_saying)
            return text  # returning the text which has been inputed.
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # if you want to record for the specific interval of time

    # The duration ins specified by the user, since the default value passed from the main funtion is 7 seconds,
    # since the short term memory duration is 5 +- 2 So , for the maximum iof seven seconds.!!!
    # TIps : Using the Wave , which is built by the microsoft
    def record_something(self, duration):
        # Below the Audio is accessed and then the audio is recorded and then converted in to text
        CHUNK = 1024  # Specifying the chunks for the recording
        FORMAT = pyaudio.paInt16  # the Format is picked up from the pyaudio
        CHANNELS = 2  # The Cross Channels
        RATE = 44100  # Bit rate , at which to record
        RECORD_SECONDS = duration  # Recording time duration for the computer
        WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name as a string

        p = pyaudio.PyAudio()  # creating the Object and then calling the function of the PyAudio to access the audio

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        # Creating the stream and specifing the access channels , and the rate, Input to be on.

        print("* recording, Ask me something!")  # Just a Message to tell the user that the Voice is being recorded

        frames = []  # A list of frame is created which is

        for i in range(0, int(
                                RATE / CHUNK * RECORD_SECONDS)):
            # This is the Rate(bit rate) / Chuncks to be recorded * the Seconds
            data = stream.read(CHUNK)  # Reading the dat afrom the stream
            frames.append(data)  # Adding the each data to the frame list and appending it up.

        print("* done recording")
        print("Processing the input................")

        stream.stop_stream()  # Stopping the stream so that the stream(recorder for audio is stopped )
        stream.close()  # Closing the stream of the audio
        p.terminate()  # Termination the Py AUDIO Module cause it was accesses

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # Accessing the WAV
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    #
    # Converting the text to speech using the pysha personal assistant and then specifying the input!
    '''  BELOW ARE THE FUNCTIONS FOR THE ENGINE change regarding to Text to Speech
    '''

    # Machine Speaking!
    def text_to_speech(self, text_input='HI! my name is PYSHA and i am your assistant'):
        self.engine.say(text_input)
        self.engine.runAndWait()
        self.engine.stop()
        '''Adding the changing of the voices according to the specified module
        , since the module will be changing the applications'''
        #

        return

    # TODO: Add additional Voices such as  child voice and later onward , create an algorithum so that we can have voice
    # TODO: The accent of the particular region and the people voices should also be considered
    # Creating the function for the changing of the voice of the module
    def change_person(self, name='', gender=''):
        self.engine = None  # setting the engine to NONE
        if name != '':  # make it more intelligent
            if name == 'hazel':
                self.engine = _chooseassitant.change_byname('hazel')
            elif name == 'david':
                self.engine = _chooseassitant.change_byname('david')  # changing the name to david
            elif name == 'zira':
                self.engine = _chooseassitant.change_byname('zira')  # Changing the engine to zira
            return
        elif gender != '':
            if gender == 'male':
                self.engine = _chooseassitant.change_gender('male')  # Changing the assistant by gender --> daVid
            else:
                self.engine = _chooseassitant.change_gender('female')  # female gender assistant
            return
            # TODO : Add More additonal voices and other things

    ''' Ending of the functions of the system change regarding to the engine text speech
    '''

    def volumeupdate(self, status_value=''):
        assert status_value != '', 'Value should have been not emptied'  # Debugging purpose
        if status_value != '':
            self.engine = _chooseassitant.volume_update(status_value)  # Updating the status of the engine
        else:
            print("--------Volume status---------")  # just for debugging purpose
        return  # returning

    # This function is responsible for the defining of the particular session and
    # then recording the particular input, and working on the continuous
    # Recognition of the voice.!
    # TODO: Responsible for recording the audio in the wave format
    def speech_to_text_wav(self, file_to_recognize):
        r = sr.Recognizer()

        with sr.WavFile(str(file_to_recognize)) as source:  # use "test.wav" as the audio source
            audio = r.record(source)  # extract audio data from the file

        try:
            total_saying = r.recognize_google(audio)
            # total_saying = r.recognize_sphinx()
            # if total_saying != "" or total_saying != NONE:
            #   text_to_speech("processing the audio")
            print("you said: " + total_saying)  # recognize speech using Google Speech Recognition
            # text_to_speech("You said ")
            # here i will be working on latter analysis
            total_saying = str(total_saying).lower()  # converting the total saying to the strings
            self.process_text_input(total_saying)

        except LookupError:  # speech is unintelligible
            print("Could not understand audio")
            self.text_to_speech("I Couldn't understand the audio")
        except sr.UnknownValueError:
            print("UNKNOWN!!")

    # The following function will be responsible for the text to be parsed regarding to the certain input.

    # The below function is responsible for the text processing of the Total saying
    #  since what the user i ssaying is recorded in this
    def process_text_input(self, total_saying=""):
        self.total_saying = total_saying.strip()  # Stripping the string for the extra white spaces
        total_saying = self.total_saying.lower()  # Converting a string to lower case
        self.total_saying = self.total_saying.lower()  # Debugging purpose
        if total_saying == "quit" or total_saying.lower() == "stop listening" or total_saying.lower() == "stop" or total_saying.lower() == "exit":
            self.store_userinput("quit")
            self.text_to_speech("BYE")
            os._exit(0)  # exiting the program
        else:
            # this stores the Specified Input we said Regerding to something
            # Textual_Analysis(total_saying)
            '''
                Below is the place where are your working on!!!

                '''
            if total_saying.__contains__("stop listenning both of you") or total_saying.__contains__(
                    "stop listenning Anna"):
                self.text_to_speech("ok ok I am turning myself off")
                exit(0)  # this exits the program, since we have stopped Anna from listenning
            if total_saying.startswith('search for') or total_saying.startswith('google'):
                self.text_to_speech("Opening a Browser For you.")
                self.total_saying = total_saying.replace("search for", "")
                self.total_saying = self.total_saying.replace("search", "")
                self.total_saying = self.total_saying.replace("on google", "")
                self.total_saying = self.total_saying.replace("google", "")
                self.store_userinput("Searching on Browser :" + self.total_saying)  # recording into database
                total_saying = total_saying.replace('search for',
                                                    '')  # Replacing the Search for with the total saying .
                total_saying = total_saying.replace('google', '')  # Replacing the Key word Googe with it
                self.search_browser(
                    text_input=self.total_saying)  # sending every remanining thing to the Browser to browse for
                self.text_to_speech("Browser Result have been displayed.")
            elif total_saying.startswith('social media'):
                self.store_userinput(total_saying)  # this stores the particular input.
                browse_key = total_saying.replace('social media',
                                                  '')  # Replacing the total saying variable value'd (social media with empty string)
                browse_key = browse_key.strip()  # removing the extra white spaces
                sma = SocialMedia()  # Creating the social media object
                sma.social_media_access(
                    browse_key=browse_key)  # Passing the browser key to the social media access function.

            elif (total_saying.__contains__('wikipedia') and total_saying.startswith('search')) or (
                        total_saying.__contains__('on wikipedia') and total_saying.startswith('search')):
                total_saying = total_saying  # this converts the string to the lower case
                total_saying = total_saying.replace('search', '')  # replacing the start with the empty string
                total_saying = total_saying.replace('on wikipedia', '')  # replacing the on wikiepdia with empty string
                self.text_to_speech('Searching on Wikipedia')
                retrieved_link = self.search_wiki(
                    total_saying)  # calling the wikipedia search function , for the results
                self.lastlink = retrieved_link
                print(self.lastlink)

            elif total_saying.startswith("what is the date") or total_saying == 'date':
                # Here you will be required to input the date
                self.day_check()  # This calls the day check

            elif total_saying.startswith("what is the time") or total_saying == 'time':
                self.time_check()  # this checks the current time according to the specified state

            # Create a Grammer , that represents the questions regerding to the respectable machine

            # TODO: Working on the changing of the Assistant and others.
            elif total_saying.startswith("switch to") or self.total_saying.startswith("want to ta"):
                self.total_saying = total_saying.replace("switch to", "")  # replacing the text string
                self.total_saying = self.total_saying.strip()  # stripping the white spaces
                self.db.insert_into_History("Switch to:" + self.total_saying)  # adding the string in the database
                # assert self.total_saying not in ['male', 'female', 'david', 'zira',
                # 'hazel'], "You haven't selected the correct list"  # Debugging purpose
                Assistant_string = self.total_saying
                if Assistant_string in ['male', 'female']:
                    self.change_person(gender=Assistant_string)  # Changing on the basis of gender
                    self.text_to_speech("I am here Shafay , Ask your query ")
                elif Assistant_string in ['david', 'hazel', 'zira', 'anna', 'lizy']:
                    if Assistant_string == 'anna':
                        self.change_person(name='hazel')
                    elif Assistant_string == 'lizy':
                        self.change_person(name='zira')
                        pass
                    else:
                        self.change_person(name=Assistant_string)  # Changing on the basis of name
                        self.text_to_speech("I am here Shafay , Ask your query ")
                else:
                    self.text_to_speech("Who you want to switch to")

            elif total_saying.startswith("what is your"):
                # here you need to create the question saying file so that the file is readable.
                '''
                    Write the Respectable question in this format so that, the Agent learns from the file.

                    '''
                self.total_saying = total_saying.replace("what is your",
                                                         "")
                # replacing the words so that it will be easier for the program to Check the last thing
                self.Personal_PYSHA(self.total_saying)
            # Switching to text mode .
            elif total_saying.startswith("text mode"):
                tm = TextMode()
                # this calls the text mode function, and there we can do the processing in the form of the text!
                tm.text_mode(total_saying)  # Passes the total saying to the Class Function!

            elif total_saying == "show me a comic":
                self.store_userinput("show me a comic")  # finding the comic from the web
                joke_object = Joke()  # creating an object of ht Joke class !
                self.text_to_speech("Finding a Comic the Database")
                joke_object.Image_Joke()
                # Calls the Joke class Image Joke Object to show a Joke in the form of an image

            elif total_saying == "tell me a joke" or total_saying == "tell me another joke" or total_saying == "joke please":
                print("JOKE JOKE JOKE!!!")
                self.store_userinput("tell me a joke")
                joke_object = Joke()
                self.text_to_speech("OH wait")
                joke_text = joke_object.joke_category()  # Calls any nerdy or Explicit joke about Chuck Norris.!
                # frontend_HCI(Joke_Text)  # calling the tkinter library to create the joke for the particular thing ,
                print(joke_text)
                # This is the Joke text , which will be printed in the console ,since we don't have much time ,
                # working for the Console.!
                self.text_to_speech(joke_text)  # Speaking up the joke (By machine ) PYSHA <3

            elif total_saying.startswith("open") or total_saying.startswith("run"):
                self.store_userinput(total_saying)  # This stores the Data in the Us
                # er input file so that the history is kept
                total_saying = total_saying.replace('open ', '')  # replacing the word open with the Total_saying!
                total_saying = total_saying.replace('run ', '')  # This is the replacement of the run with the
                self.run_apps(total_saying)  # This is the total saying being passed to the Running apps. !

            elif total_saying.startswith('parse sentence') or total_saying.startswith(
                    'parse this') or total_saying.startswith('tokenize this'):
                self.store_userinput(total_saying)
                total_saying = total_saying.replace('tokenize this', '')
                total_saying = total_saying.replace('parse sentence',
                                                    '')  # replacing the total saying with the parse sentence
                self.total_saying = total_saying.replace('parse this',
                                                         '')  # replacing the total saying of the parse this with none !
                np = NaturalProcessing()  # creating the object of the classes
                # -------------You are working here -------------
                tokenized_sentences_return = np.word_tokeniztion(
                    self.total_saying, sent_tokenized=False)  # this parse the Np with the tokenizing of the words
                print(tokenized_sentences_return)  # this prints the Tokenize the words
            elif total_saying.startswith("youtube") or total_saying.startswith(
                    "search on youtube") or total_saying.startswith("search youtube") or total_saying.startswith(
                "youtube search"):
                self.total_saying = total_saying.replace("search", '')
                self.total_saying = self.total_saying.replace("search on youtube", "")
                self.total_saying = self.total_saying.replace("youtube", "")
                self.total_saying = self.total_saying.replace("search youtube", "")
                self.total_saying = self.total_saying.replace("youtube search", "")
                self.text_to_speech("Searching on youtube for : " + total_saying)
                self.store_userinput("Search on Youtube :" + total_saying)
                Y = YouTubeSearch()  # Creates in the Youtube Class
                self.text_to_speech('Displaying Results')
                # TODO: make it more perfect, for searching on youtube.

                if self.total_saying.__contains__("playlist") or self.total_saying.__contains__(
                        "play list") or self.total_saying.__contains__("playlists"):
                    self.total_saying = self.total_saying.replace("playlist", '')
                    self.total_saying = self.total_saying.replace("play list", '')
                    self.text_to_speech("Finding the playlist from youtube.")
                    self.lastlink = Y.search(search_text=self.total_saying, play_list=True)  # Searched for the playlist
                    self.text_to_speech("I Guess i found some , have a look at these.")
                # If we search for a single link rather than a play list ,

                else:
                    self.lastlink = Y.search(
                        search_text=self.total_saying)  # Sends the Total Saying to the Youtube Search Function
                    self.text_to_speech('Youtube Result , Best match found')
            elif total_saying.startswith('stack over flow') or total_saying.startswith(
                    'stackoverflow') or total_saying.startswith("stack overflow") or total_saying.startswith(
                'search stack over flow') or total_saying.startswith('stack search') or total_saying.startswith(
                'search stackoverflow'):
                self.total_saying = total_saying.replace('stackoverflow', '')
                self.total_saying = self.total_saying.replace('stack overflow', '')
                self.total_saying = self.total_saying.replace('stack over flow', '')
                self.total_saying = self.total_saying.replace('search stack over flow', '')
                self.total_saying = self.total_saying.replace('stack', '')
                self.total_saying = self.total_saying.replace('stack search', '')
                self.total_saying = self.total_saying.replace('search stackoverflow', '')
                self.text_to_speech('Search on Stackoverflow' + self.total_saying)
                self.store_userinput('Search on Stackoverflow :' + self.total_saying)
                SOF = StackoverFlow()  # -- Creates the Object Stack over flow class and calls the search function
                self.lastlink = SOF.search(
                    self.total_saying)  # replacing the last link so that we can read it out later
                # self.db.insert_into_History("searching on stackoverflow : " + self.lastlink)
                self.text_to_speech("Stack over flow Results Shown")
            elif total_saying.startswith("search music") or total_saying.__contains__(
                    "search music") or total_saying.__contains__("find music") or \
                    total_saying.__contains__("search soundcloud"):
                self.total_saying = total_saying.replace('search music', "")  # replacing the search music with empty
                self.total_saying = self.total_saying.replace("search music", '')
                self.total_saying = self.total_saying.replace("search soundcloud", '')
                self.total_saying = self.total_saying.replace("find music", '')
                self.total_saying = self.total_saying.replace("music", '')
                SoundCloudSearch(self.total_saying)
            elif total_saying.startswith("play music") or total_saying.__contains__("music please"):
                self.total_saying = total_saying.replace("play music", "")
                self.total_saying = self.total_saying.replace("music please", "")  # replacing the string !
                self.text_to_speech("Playing Music")
                # MP_gui = main()
                # MP_gui.run()
                self.store_userinput("playing music")
            # last link being read
            # This calls the Web scrap class in the __speakcode.py
            # TODO : Add the links to be dynamically updated from the last scrapped page
            elif total_saying.startswith("play video"):
                self.text_to_speech("Playing Music Video for you")
                self.play_video()
                self.text_to_speech("Music Video played")
            elif total_saying.startswith("read it out to me") or total_saying.startswith("read it out for me"):
                # self.db.insert_into_History(total_saying + ":" + self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
                self.total_saying = total_saying.replace("read it out to me", "")
                self.text_to_speech("Reading the Text from the website")
                WS = WebScrap()
                WS.scrap_link(self.lastlink)
                self.store_userinput(total_saying + ":" + self.lastlink)
            elif total_saying.startswith("web"):
                self.total_saying = total_saying
                self.store_userinput("Web : opening " + self.total_saying)
                self.text_to_speech("opening the website for : ",self.total_saying)
                webbrowser.open(self.total_saying)
            elif total_saying.startswith("twitter status") or total_saying.startswith("status"):
                self.total_saying = total_saying.replace("tweet ", "")
                self.total_saying = self.total_saying.replace("status ", "")
                self.total_saying = self.total_saying.replace("twitter status ", "")
                # TODO: Replace your twitter credentials here
                ckey = '--REPLACE-HERE-'
                csecret = '--REPLACE-HERE-'
                atoken = '--REPLACE-HERE-'
                asecret = '--REPLACE-HERE-'
                TP = Twitter_PYSHA(ckey, csecret, atoken, asecret)  # create object and pass in values
                api = TP._api_auth()
                status = self.total_saying
                self.store_userinput("tweeting on twitter:" + self.total_saying)
                self.text_to_speech("tweeting on twitter :" + self.total_saying)
                api.update_status(status)  # Posts the status om the twitter.

            elif total_saying.startswith("mail") or total_saying.startswith("check email") or total_saying.startswith(
                    "check mail"):
                self.text_to_speech("")
                webbrowser.open("www.gmail.com")
                webbrowser.open("www.hotmail.com")
                webbrowser.open("www.yahoo.com")
            elif total_saying.startswith("twitter"):
                webbrowser.open("www.twitter.com")
            elif total_saying.startswith("reddit"):
                webbrowser.open("www.reddit.com")
            elif total_saying.startswith('which statements i said to you') or \
                    total_saying.startswith("what did i said you") or \
                    total_saying.startswith("what is in your shortterm memory") \
                    or total_saying.startswith("what is in your short term memory") or \
                    total_saying.startswith('what is in your ram') or total_saying.startswith("short term memory"):
                self.shortterm_check()  # this calls the current Short term memory shuffled.
            elif total_saying.__contains__("what did i just said to you") or total_saying.__contains__(
                    "what did i just said"):
                self.shortterm_check(limit=1)  # specifying the limit to 1 so that the last statements is returned
            elif total_saying.startswith('what') or total_saying.startswith("when") or total_saying.startswith(
                    "how") or total_saying.startswith("where") or total_saying.startswith(
                "solve") or total_saying.startswith("who") or total_saying.startswith(
                "whom") or total_saying.startswith("why") or total_saying.startswith("which") or \
                    total_saying.startswith("show me"):
                self.total_saying = total_saying
                self.store_userinput('Question Asked : ' + self.total_saying)
                # since this is a computation engine that will be used for the computation of the question asked .!
                WFM = WolFrameAlphaClass()
                # creating the wolframapla class that will be used for the cretion of the api assistant
                self.text_to_speech('searching database')
                WFM_backstring = WFM.search_engine(
                    self.total_saying)  # this searches the WOlframAlpha for the Search Strings
                if WFM_backstring != "":
                    # if the input returned from the Wolframalpha turns out to be null then leave it .
                    self.text_to_speech(WFM_backstring)  # this converts text to speech
            else:
                total_saying, self.total_saying = self.total_saying, total_saying
                try:
                    retrieved_output = self.py_chat_bot.retrieved_response(self.total_saying)
                    self.text_to_speech(retrieved_output)  # calls in the retrieved output
                    self.store_userinput("PYSHA Chat input: " + str(self.total_saying))
                    # Storing the input value in the db
                    self.py_chat_bot.train_text(list(self.total_saying))  # trains on the basis of the user specified
                    # input
                    self.store_userinput("PYSHA Chat output" + str(retrieved_output))
                    # Storing the recieved value in db
                except Exception as E:  # debuggin purpose
                    print("Couldn't find something , Check the bot specification :", E)


class Main_Call():
    # TODO : Make it a little more intelligent
    PYSHA_Obj = PYSHA_CLASS()

    def __init__(self):
        print("Main Class Intialized.....")

    def main(self):  # main program access
        print("-^-")
        # duration = float(input("How much time you need to record for ?"))
        # record_something(duration)  just trying to pause the thing
        client_id = ""  # this is the google api client id
        client_secret = ""  # this is the google api client secret key
        self.PYSHA_Obj.text_to_speech()  # Calls the virtual assistant to speech
        # speech_to_text()  # calling the function
        while True:
            '''-- if you want to record for 7 seconds as short term memory and have a bad microphone then'''
            # # try:
            # self.PYSHA_Obj.record_something(7)  # providing the Duration in the Record function!
            # self.PYSHA_Obj.speech_to_text_wav("output.wav")  # Converting the recorded format of WAV to speech!
            self.PYSHA_Obj.speech_to_text()
            # Calls the function automatically getting the queries. This is for live recording
            # The above the Audio has been recorded , and now the Audio needs to be converted into texts/
            # Machine Learning book + N.L.T.K. BOOK need to be studied  with Plotting and O.P.E.N.C.V.2.
            # Work with the MEGA VOICE COMMAND AFTER THE EXAM HAVE BEEN FINISHED.

# if __name__ == '__main__':
# Py = PYSHA_CLASS()
# print(Py.shortterm_check())
# Py.play_video()  for playing music video just for testing
# ---
