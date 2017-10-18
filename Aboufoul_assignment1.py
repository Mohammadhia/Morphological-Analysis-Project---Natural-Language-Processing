from collections import Counter
import re
import io
import string

############ PROBLEM 1 ###################################################################
funny = "colorless green ideas sleep furiously"

def splitBySpaces(word):
    return word.split(" ")
print(splitBySpaces(funny))

def secondLetterString(word):
    splitList = word.split(" ")
    shortenedString = ""
    for i in range(0, len(splitList)):
        shortenedString += splitList[i][1] #Gets second letter of each word
    return shortenedString
print(secondLetterString(funny))

def phraseMaker(word):
    tempPhrase = splitBySpaces(word)
    phrases = []
    for i in range(0,3):
        phrases.append(tempPhrase[i])
    return phrases
print(phraseMaker(funny))

def combineToString(word):
    sequence = phraseMaker(word)
    space = " "
    return space.join(sequence)
print(combineToString(funny))

def alphabetize(word):
    splitList = splitBySpaces(word)
    splitList.sort()
    for i in range (0, len(splitList)):
        print(splitList[i])
alphabetize(funny)
##########################################################################################

############ PROBLEM 2 ###################################################################
sampleSentence = "he went to the moon while he slept"

def wordsAndFrequency(sentence):
    splitList = splitBySpaces(sentence)
    splitList.sort() #alphabetizes list
    counts = Counter(splitList)
    for key in counts:
        print(key + ': ' + str(counts[key]))
wordsAndFrequency(sampleSentence)
##########################################################################################

############ PROBLEM 3 ###################################################################
# Answer on pdf
##########################################################################################

############ PROBLEM 4 ###################################################################
str = """  
... austen-emma.txt:hart@vmd.cso.uiuc.edu (internet) hart@uiucvmd (bitnet)
... austen-emma.txt:Internet (72600.2026@compuserve.com); TEL: (212-254-5093)
... austen-persuasion.txt:Editing by Martin Ward (Martin.Ward@uk.ac.durham)
... blake-songs.txt:Prepared by David Price, email ccx074@coventry.ac.uk
... """
regex = r'\w+[.]?\w+@\w+[\.?\w+]*'
output = re.findall(regex, str)
print(output)
##########################################################################################

############ PROBLEM 5 ###################################################################
def duplicateEliminator(file):
    linesObserved = []
    with io.FileIO("fileWithoutDuplicates.txt", "w") as newFile:
        for line in open(file, "r"):
            if line.rstrip() not in linesObserved:   #IF the line observed (excluding trailing whitespace) has not been seen before
                linesObserved.append(line.rstrip())  #Add the observed line to the list of those observed
                newFile.write(line.encode('utf-8'))         #Write it to the new file
    newFile.close()

#duplicateEliminator('hiWorld.txt')  #To test the method, this text file is only available on my computer. You can try any other text file you'd like
##########################################################################################

############ PROBLEM 6 ###################################################################
# Answer on pdf
##########################################################################################

############ PROBLEM 7 ###################################################################
############ Part a #############################
def assignStatements(fileName): #Insert name of file as string to use this method
    obamaStatements = ""
    romneyStatements = ""
    lehrerStatements = ""
    currentSpeaker = ""
    file = open(fileName, 'r')
    for line in file:
        if(line.startswith("Â") or line.startswith("October") or line.startswith("OCTOBER") or line.startswith("PRESIDENT") or line.startswith("JIM LEHRER") or line.startswith("SPEAKERS:")):
            continue #Skips rest of the line as it will not contain any of the 3 speakers' statements
        elif(line.startswith("LEHRER:")):
            if("OBAMA:" in line):    #THIS IS TO ADDRESS THE ONE INSTANCE IN WHICH 2 SPEAKERS ARE ON THE SAME LINE
                temp = line.split("OBAMA:",1)[0] #Holds the statements before Obama speaks
                lehrerStatements = lehrerStatements + temp.split("LEHRER:",1)[1] #Adds on Lehrer's statements
                obamaStatements = obamaStatements + line.split("OBAMA:",1)[1] #Adds on Obama's statements
                currentSpeaker = "OBAMA" #Obama is now speaking
            else:
                currentSpeaker = "LEHRER"
                lehrerStatements = lehrerStatements + line.split("LEHRER:",1)[1] #concatenates Lehrer's statements
        elif(line.startswith("OBAMA:")):
            currentSpeaker = "OBAMA"
            obamaStatements = obamaStatements + line.split("OBAMA:",1)[1] #concatenates Obama's statements
        elif(line.startswith("ROMNEY:")):
            currentSpeaker = "ROMNEY"
            romneyStatements = romneyStatements + line.split("ROMNEY:",1)[1] #concatenates Romney's statements
        elif(line.startswith("(")): #The line begins with some note about the audience's behavior (i.e. APPLAUSE, CROSSTALK, LAUGHTER)
            if("LEHRER:" in line):   #THIS IS TO ADDRESS THE ONE INSTANCE IN WHICH A SPEAKER FOLLOWS A NOTE ABOUT THE AUDIENCE
                currentSpeaker = "LEHRER"
                lehrerStatements = lehrerStatements + line.split("LEHRER:",1)[1] #Adds on Lehrer's statements
            else:
                continue #Disregards lines solely focused on the audience's actions
        elif(not line.startswith("(") or not line.startswith("OBAMA:") or not line.startswith("ROMNEY:") or not line.startswith("LEHRER:")): #for lines in which a speaker continues to speak
            if(currentSpeaker == "LEHRER"):
                lehrerStatements = lehrerStatements + line
            elif(currentSpeaker == "OBAMA"):
                obamaStatements = obamaStatements + line
            elif(currentSpeaker == "ROMNEY"):
                romneyStatements = romneyStatements + line
    file.close()
    lehrerStatements.replace("(CROSSTALK)","").replace("(APPLAUSE)","").replace("(LAUGHTER)","")    #Removing any lingering comments about audience
    obamaStatements.replace("(CROSSTALK)","").replace("(APPLAUSE)","").replace("(LAUGHTER)","")     #Removing any lingering comments about audience
    romneyStatements.replace("(CROSSTALK)","").replace("(APPLAUSE)","").replace("(LAUGHTER)","")    #Removing any lingering comments about audience
    return lehrerStatements, obamaStatements, romneyStatements
####################### End of assignStatements method ########################

lehrerFullRemarks, obamaFullRemarks, romneyFullRemarks = assignStatements("debate.txt") #Assigning statements to corresponding speakers
#print(lehrerFullRemarks)   #Very long concatenation; can uncomment print statement if you'd like to see
#print(obamaFullRemarks)    #Very long concatenation; can uncomment print statement if you'd like to see
#print(romneyFullRemarks)   #Very long concatenation; can uncomment print statement if you'd like to see

################################### Part b ############################################################
from nltk.corpus import stopwords

contractionDictionary = {
    "i\'ve": "i have",
    "you\'ve": "you have",
    "we\'ve": "we have",
    "they\'ve": "they have",
    "we\'ll": "we will",
    "i\'ll": "i will",
    "they\'ll": "they will",
    "you\'ll": "you will",
    "he\'ll": "he will",
    "she\'ll": "she will",
    "hasn\'t": "has not",
    "haven\'t": "have not",
    "doesn\'t": "does not",
    "don\'t": "do not",
    "didn\'t": "did not",
    "weren\'t": "were not",
    "wouldn\'t": "would not",
    "shouldn\'t": "should not",
    "couldn\'t": "could not",
    "won\'t": "will not",
    "can\'t": "can not",
    "isn\'t": "is not",
    "let\'s": "let us",
    "there\'s": "there is",
    "that\'s": "that is",
    "it\'s": "it is",
    "what\'s": "what is",
    "who\'s": "who is",
    "i\'m": "i am",
    "we\'re": "we are",
    "they\'re": "they are",
    "you\'re": "you are",
    "they\'d": "they would",
    "i\'d": "i would",
    "he\'s": "he has",
    "she\'s": "she has",
    "you\'d": "you would"
}
lehrerFullRemarks = lehrerFullRemarks.replace("\n", " ").strip().lower()    #Removes capitalization
lehrerFullRemarks = re.sub(r"[,.?!\"]", " ", lehrerFullRemarks)             #Removes punctuation
lehrerFullRemarks = re.sub(r"[\-]{2,}", " ", lehrerFullRemarks)             #Removes punctuation
lehrerFullRemarks = re.sub(r"\s+", " ", lehrerFullRemarks)                  #Removes extra spaces
for word in lehrerFullRemarks.split():                                      #Breaks apart contractions
    if(word in contractionDictionary):
        lehrerFullRemarks = lehrerFullRemarks.replace(word, contractionDictionary.get(word))
lehrerFullRemarks = splitBySpaces(lehrerFullRemarks)                        #TOKENIZES THE WORDS OF LEHRER USING METHOD FROM 1a!!!
lehrerFullRemarks = [word for word in lehrerFullRemarks if word not in stopwords.words('english')]  #Removes stop words

obamaFullRemarks = obamaFullRemarks.replace("\n", " ").strip().lower()      #Removes capitalization
obamaFullRemarks = re.sub(r"[,.?!\"]", " ", obamaFullRemarks)               #Removes punctuation
obamaFullRemarks = re.sub(r"[\-]{2,}", " ", obamaFullRemarks)               #Removes punctuation
obamaFullRemarks = re.sub(r"\s+", " ", obamaFullRemarks)                    #Removes extra spaces
for word in obamaFullRemarks.split():                                       #Breaks apart contractions
    if(word in contractionDictionary):
        obamaFullRemarks = obamaFullRemarks.replace(word, contractionDictionary.get(word))
obamaFullRemarks = splitBySpaces(obamaFullRemarks)                          #TOKENIZES THE WORDS OF OBAMA USING METHOD FROM 1a!!!
obamaFullRemarks = [word for word in obamaFullRemarks if word not in stopwords.words('english')]  #Removes stop words

romneyFullRemarks = romneyFullRemarks.replace("\n", " ").strip().lower()    #Removes capitalization
romneyFullRemarks = re.sub(r"[,.?!\"]", " ", romneyFullRemarks)             #Removes punctuation
romneyFullRemarks = re.sub(r"[\-]{2,}", " ", romneyFullRemarks)             #Removes punctuation
romneyFullRemarks = re.sub(r"\s+", " ", romneyFullRemarks)                  #Removes extra spaces
for word in romneyFullRemarks.split():                                      #Breaks apart contractions
    if(word in contractionDictionary):
        romneyFullRemarks = romneyFullRemarks.replace(word, contractionDictionary.get(word))
romneyFullRemarks = splitBySpaces(romneyFullRemarks)                        #TOKENIZES THE WORDS OF ROMNEY USING METHOD FROM 1a!!!
romneyFullRemarks = [word for word in romneyFullRemarks if word not in stopwords.words('english')]  #Removes stop words

from nltk.stem.porter import *
from nltk.stem.snowball import *
from nltk.stem.lancaster import *

porter = PorterStemmer()
snowball = SnowballStemmer('english')
lancaster = LancasterStemmer()

lehrerPorterStems = [porter.stem(word) for word in lehrerFullRemarks]       #Porter, Snowball, and Lancaster stemmers applied to each speaker's full remarks
#print(lehrerPorterStems)
lehrerSnowballStems = [snowball.stem(word) for word in lehrerFullRemarks]
#print(lehrerSnowballStems)
lehrerLancasterStems = [lancaster.stem(word) for word in lehrerFullRemarks]
#print(lehrerLancasterStems)
obamaPorterStems = [porter.stem(word) for word in obamaFullRemarks]
#print(obamaPorterStems)
obamaSnowballStems = [snowball.stem(word) for word in obamaFullRemarks]
#print(obamaSnowballStems)
obamaLancasterStems = [lancaster.stem(word) for word in obamaFullRemarks]
#print(obamaLancasterStems)
romneyPorterStems = [porter.stem(word) for word in romneyFullRemarks]
#print(romneyPorterStems)
romneySnowballStems = [snowball.stem(word) for word in romneyFullRemarks]
#print(romneySnowballStems)
romneyLancasterStems = [lancaster.stem(word) for word in romneyFullRemarks]
#print(romneyLancasterStems)

################## Part c ####################################
from collections import Counter
lehrerPorterCounter = Counter(lehrerPorterStems)
lehrerPorterMostCommon = lehrerPorterCounter.most_common(10)
print("Lehrer porter 10 most common: ")
print(lehrerPorterMostCommon)
lehrerSnowballCounter = Counter(lehrerSnowballStems)
lehrerSnowballMostCommon = lehrerSnowballCounter.most_common(10)
print("Lehrer snowball 10 most common: ")
print(lehrerSnowballMostCommon)
lehrerLancasterCounter = Counter(lehrerLancasterStems)
lehrerLancasterMostCommon = lehrerLancasterCounter.most_common(10)
print("Lehrer lancaster 10 most common: ")
print(lehrerLancasterMostCommon)

obamaPorterCounter = Counter(obamaPorterStems)
obamaPorterMostCommon = obamaPorterCounter.most_common(10)
print("Obama porter 10 most common: ")
print(obamaPorterMostCommon)
obamaSnowballCounter = Counter(obamaSnowballStems)
obamaSnowballMostCommon = obamaSnowballCounter.most_common(10)
print("Obama snowball 10 most common: ")
print(obamaSnowballMostCommon)
obamaLancasterCounter = Counter(obamaLancasterStems)
obamaLancasterMostCommon = obamaLancasterCounter.most_common(10)
print("Obama lancaster 10 most common: ")
print(obamaLancasterMostCommon)

romneyPorterCounter = Counter(romneyPorterStems)
romneyPorterMostCommon = romneyPorterCounter.most_common(10)
print("Romney porter 10 most common: ")
print(romneyPorterMostCommon)
romneySnowballCounter = Counter(romneySnowballStems)
romneySnowballMostCommon = romneySnowballCounter.most_common(10)
print("Romney snowball 10 most common: ")
print(romneySnowballMostCommon)
romneyLancasterCounter = Counter(romneyLancasterStems)
romneyLancasterMostCommon = romneyLancasterCounter.most_common(10)
print("Romney lancaster 10 most common: ")
print(romneyLancasterMostCommon)


#################### Part d ##################################
def positiveWordsStems():
    file = open('positive.txt', 'r')
    listOfPositiveWords = []
    for line in file:
        listOfPositiveWords.append(line.replace("\n",""))
    positiveWordsPorterStems = [porter.stem(word) for word in listOfPositiveWords]

    return positiveWordsPorterStems
#print(positiveWordsStems())    #Can uncomment this if you'd like to see list of positive stemmed words
#################### Part e ##################################
positiveWordList = positiveWordsStems()
lehrerPositiveWordCount = 0
lehrerPositiveWordList = []
obamaPositiveWordCount = 0
obamaPositiveWordList = []
romneyPositiveWordCount = 0
romneyPositiveWordList = []

for i in range(0,len(lehrerPorterStems)):
    if(lehrerPorterStems[i] in positiveWordList):
        lehrerPositiveWordCount = lehrerPositiveWordCount + 1
        lehrerPositiveWordList.append(lehrerPorterStems[i])
for i in range(0,len(obamaPorterStems)):
    if(obamaPorterStems[i] in positiveWordList):
        obamaPositiveWordCount = obamaPositiveWordCount + 1
        obamaPositiveWordList.append(obamaPorterStems[i])
for i in range(0,len(romneyPorterStems)):
    if(romneyPorterStems[i] in positiveWordList):
        romneyPositiveWordCount = romneyPositiveWordCount + 1
        romneyPositiveWordList.append(romneyPorterStems[i])

print("Lehrer positive word usage: ")
print(lehrerPositiveWordCount)
print("Obama positive word usage: ")
print(obamaPositiveWordCount)
print("Romney positive word usage: ")
print(romneyPositiveWordCount)
print("OBAMA USED THE POSITIVE WORDS LISTED IN THE POSTIVE WORD DICTIONARY MOST OFTEN")

lehrerPositiveCounter = Counter(lehrerPositiveWordList)
obamaPositiveCounter = Counter(obamaPositiveWordList)
romneyPositiveCounter = Counter(romneyPositiveWordList)

print("Lehrer 10 most common Positive Words:")
print(lehrerPositiveCounter.most_common(10))
print("Obama 10 most common Positive Words:")
print(obamaPositiveCounter.most_common(10))
print("Romney 10 most common Positive Words:")
print(romneyPositiveCounter.most_common(10))

##########################################################################################