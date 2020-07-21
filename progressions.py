#Some experiments regarding chord progressins

def CreateListOfProgressions():
    listOfProgressions = ["I-V-IV-iv", "iim7-V7-Imaj7"]
    tempList = []
    for element in listOfProgressions:
        individualProgression = element.split("-")
        tempList.append(individualProgression)
    return(tempList)

def buildChordTypes():
    romanNumerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
    chordTypes = []
    for rm in romanNumerals:
        chordTypes.append(rm)
        chordTypes.append(rm.lower())
        chordTypes.append(rm+"7")
        chordTypes.append(rm.lower()+"7")
        chordTypes.append(rm + "maj7")

    return chordTypes
print(buildChordTypes())
def FindScaleKeys(tonic):
    allKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    tonicIndex = allKeys.index(tonic)
    allKeys = allKeys[tonicIndex:-1] + allKeys[0: tonicIndex+1]
    scaleKeys = allKeys[0] +  allKeys[2] +  allKeys[4] +  allKeys[5] +  allKeys[7] +  allKeys[9] + allKeys[11]
    #print(scaleKeys)
    return scaleKeys

def ConvertChordsToScaleDegrees(currentProgression, tonic):
    chordTypeDict = {"Major": "", "Minor" : "m", "7": "7"} #THis dictionary pairs chord names with their scale degree symbols
    romanNumeralDict = {0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", }
    scaleKeys = FindScaleKeys(tonic)
    scaleDegreeProgression = []
    for chord in currentProgression:
        if not chord:
            scaleDegree = ""
        else:
            scaleDegree = romanNumeralDict[scaleKeys.index(chord[0])] + chordTypeDict[chord[1]]
        scaleDegreeProgression.append(scaleDegree)
    #print(scaleDegreeProgression)
    return scaleDegreeProgression

def ConvertScaleDegreesToChords(currentProgression, tonic):
    #currentProgression = ["I", "", "IV", ""] ivm7
    #tonic = "C"
    romanNumeralDict = {0: "I", 1: "II", 2: "III", 3: "IV", 4: "V", 5: "VI", 6: "VII",}
    romanNumeralDict = {v: k for k, v in romanNumeralDict.iteritems()}
    matchingStrings = ["dim", "aug", "m", "7", "VII", "vii", "VI", "vi", "V", "v", "IV", "iv", "III", "iii", "II", "ii", "I", "i"]

    scaleKeys = FindScaleKeys(tonic)
    chordInfo = []
    for chord in currentProgression:
        for str in matchingStrings:
            chordInfo.append(str)
            chord.replace(str, "")

    #print(scaleDegreeProgression)
    return scaleDegreeProgression

def MatchingIndices(currentProgression, potentialProgression):
    #This function needs to check whether or not the currentProgression appears in the potentialProgression at any point
    for i in range(len(potentialProgression) - len(currentProgression) + 1):
        for chord in currentProgression:
            if(chord != potentialProgression[currentProgression.index(chord) + i] and chord != ""):
                return False
        return True
#DEBUG MATCHINDICIES HERE---
#print(MatchingIndices(["I", "", "V", ""], ["I", "IV", "V", "vi"]))

def SuggestChords(currentProgression, tonic):
    #Find the tonic of the current chords, if we are given the tonic then that is the only one
    potentialTonics = []
    if(tonic == "unknown"):
        print("THIS CASE HAS NOT BEEN ACCOUNTED FOR YET")
        return None
        #potentialTonics = FindPotentialTonics()
    else:
        potentialTonics.append(tonic)

    scaleDegreeProgression = []
    for tonic in potentialTonics:
        scaleDegreeProgression.append(ConvertChordsToScaleDegrees(currentProgression, tonic))

    currentProgression = scaleDegreeProgression
    listOfProgressions = CreateListOfProgressions()

    potentialProgressions = []
    for element in currentProgression: #Most of the time this is just one element, its only a real loop if there is no root and more htan one potential tonic
        for progression in listOfProgressions:
            if(len(progression) >= len(element)):
                if(MatchingIndices(element, progression)):
                    potentialProgressions.append(progression)

    chordNameProgression = []
    for progression in potentialProgressions:
        chordNameProgression.append(ConvertScaleDegreesToChords(currentProgression, tonic))

    potentialProgressions = chordNameProgression

    print(potentialProgressions)
    return potentialProgressions

#DEBUG TESTING
#SuggestChords([["C", "Major"], ["G", "7"], []], "C")
