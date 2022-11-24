from tkinter import *
from tkinter import ttk
from ctypes import windll

words = {
    "triste": "sad",
    "mahalang": "sick",
    "chocho": "eat" ,
    "kada dia": "everyday" ,
    "eskuela": "school" ,
    "asagua": "wife",
    "nobia": "girlfriend" ,
    "nobiu": "boyfriend" ,
    "bintåna": "window" ,
    "sumåsaga": "live (place)",
    "mafañagu": "born",
    "faisen": "ask",
    "gi": "at",
    "gui'": "he,she,it",
    "hao": "you",
    "gaigue": "present, here",
    "tiempo": "weather, time" ,
    "pa'go": "now, today",
    "yanggen": "if, when (usually connects phrases)",
    "este": "this",
    "esta": "okay, already, see you later ",
    "hit": "we" ,
    "bumasta": "delay, interrupt" ,
    "pega": "place, put",
    "maskeseha": "even though" ,
    "sintusan": "religious" ,
    "guinaiya": "love",
    "cha'mu": "do not" ,
    "pula'/pupula": "take off/take out",
    "konne'": "catch, take" ,
    "fanhasso": "think, remember ",
    "enao": "that" ,
    "siña": "can" ,
    "kao": "means it's a question/ question marker",
    "masea": "any,either ",
    "dandan": "play music ",
    "guinifi": "dream ",
    "guini": "here ",
    "kapiya": "chapel, shrine ",
    "anai": "when" ,
    "guihi": "there" ,
    "guaha": "have, there is, there exists" ,
    "kantora": "singer" ,
    "pale'": "priest" ,
    "ma": "prefix usually with verbs",
    "kañada": "valley" ,
    "sanhiyong": "outside" ,
    "gumando": "play",
    "ya": "like",
    "para": "to (a place)",
    "homanao": "go (to a place)" ,
    "tasi": "beach" ,
    "manaitai": "to read" ,
    "para manu hao": "where are you going" ,
    "hafa tatatmanuhao": "how are you ",
    "haya": "east" ,
    "lagu": "west" ,
    "luchan": "south" ,
    "kattan": "north",
    "atmoñu": "organ (instrument)",
    "hula/hulat": "vow (wedding)",
    "håyi": "who" ,
    "håfa": "what" ,
    "gi månu": "where at ",
    "sa håfa": "why" ,
    "tai manu": "how" ,
    "simiyas": "seed",
    "chåguan": "grass",
    "odut": "ants",
    "lalangita": "lemon",
    "talanga": "ear",
    "sumi": "leak",
    "tenaki": "rust",
    "nai": "where (relative to thing)/ used in questions ,with manu and ngai'an",
    "na'i": "give",
    "na'hasso": "cause to think/ remind",
    "nahong/basta": "enough",
    "tiningo'": "know",
    "ñiha": "suffix to express third person/ plural ,possevive noun their",
    "boka": "eat" ,
    "hålom": "inside/in",
    "hålom tånu'": "jungle",
    "mulananan": "snore",
    "otro": "other/another",
    "simana": "week",
    "mes": "month",
    "sakkan": "year",
}

win=Tk()
windll.shcore.SetProcessDpiAwareness(1)
win.geometry("1280x720")
win.title('Chamorro Dictionary')
def display_text():
   global entry
   string= entry.get()
   if string in words:
    label.configure(text=words[string])
   else:
    label.configure(text="Couldn't find that word.")
label=Label(win, text="Definition", font=('Arial', 25), width=40)
label.pack(padx=5, pady=60)
entry= Entry(win, width=40)
entry.focus_set()
entry.pack(ipady=2)
ttk.Button(win, text= "Enter",width= 40, command= display_text).pack(pady=10)
win.mainloop()



