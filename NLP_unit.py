import spacy
from word2number import w2n
nlp = spacy.load("en_core_web_sm")
string = "This rent is due on the 2nd of each month."
doc = nlp(string)

cardinals = range(1, 32)

wordOrdinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
            "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth",
            "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth",
            "twentieth", "twenty first", "twenty second", "twenty third", "twenty fourth",
            "twenty fifth", "twenty sixth", "twenty seventh", "twenty eighth",
            "twenty ninth", "thirtieth", "thirty first"]

cardinalOrdinals = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th",
            "9th", "10th", "11th", "12th", "13th", "14th", "15th",
            "16th", "17th", "18th", "19th", "20th", "21st", "22nd",
            "23rd", "24th", "25th", "26th", "27th", "28th","29th",
            "30th", "31st"]

ordinal2CardnialDict = dict(zip(wordOrdinals, cardinalOrdinals))
test2 = dict(zip(cardinals, cardinalOrdinals))
for token in doc.ents:
    if(token.label_ == "ORDINAL"):
        print(ordinal2CardnialDict[token.text])
    if(token.label_ == "CARDINAL"):
        print(test2[int(token.text)])
    print(token.text, token.label_)
