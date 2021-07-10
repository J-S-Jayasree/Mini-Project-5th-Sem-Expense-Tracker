from nltk.chat.util import Chat, reflections
def chatty():
    print("Hi, I'm Pybot and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave\nHow can I help you? ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
pairs = [
    [
        r"What is the process|What is the Procedure|What are the steps(.*) are involved?|done?",
        ["First of all,you need to register if you are the new user.\nThen you need to enter all expense spent by you to get a report",
         "If you are a new user please register,if you are existing user please enter valid credentials."]
    ],
    [
        r"Can you help me|Can you guide me through the process?",
        ["Sure first please register by selecting on new user button and get a graphical interpretation of the expense entered by you..\nThen the next time you visit us you "+
    "can see the previous and current month report ."]
    ],
    [
        r"\n",
        ["Sorry I didnt understand .."]
    ],
    [
        r"What can you do?(.*)",
        ["I can guide you through the process of Expense Tracking"]
    ],
    [
        r"How do you(.*)track expense?|How is it done?",
        ["You need to enter expense for current month for a new user.\nBased on the expense,you can see a graphical analyis,thereby\n"+
         "creating awareness to you.","For a new user graphical analysis of current month is shown,\n for current month existing and previous "+
                                      "month is depicted"]
    ],
    [
        r" (.*)|\n",
        ["Sorry,I didnt get you .."]
    ],

    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?"]
    ],
     [
        r"what is your name ?",
        ["My name is PyBot and I'm a chatbot "]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?"]
    ],
    [
        r"I am good|I am fine|Awesome|Great|fantastic|fine|yes fine",
        ["Good to hear that"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?"]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]

    ],
    [
        r"(.*) created ?",
        ["Jayasree created me using Python's NLTK library ","top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu']
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days."]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy "]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football"]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Allu Arjun"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

    ],
    ]