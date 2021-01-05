'''
"I pledge my honor that I have abided by the Stevens Honor System." ncolonna

Created on Nov 10, 2017

@author: Nicholas Colonna
'''
import sys

PREF_FILE = 'musicrecplus.txt'

def loadUsers(filename):
    '''Reads file to get users and artists
        Returns a dictionary file sorted by user, mapped to their preferences'''
    userDict = {}
    sortedUserDict = {}
    try:
        input_file = open(filename, 'r')
    except:
        input_file = open(filename, 'w+')
    for line in input_file:            # Get one line at a time.
        user, artists = line.split(':')
        artists = artists.split(',')
        for i in range(len(artists)):
            artists[i] = artists[i].strip()
        user = user.strip()
        artists.sort()
        userDict[user] = artists
    input_file.close() # Important - do not forget to close the file
    for user in sorted(userDict):
        sortedUserDict[user] = userDict[user]
    return sortedUserDict
    
def getUserName(userDict):
    '''prompts user to enter their name and choose if they want to be private'''
    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    userName.strip().title()
    if userName not in userDict:
        userDict[userName] = []
    return userName
    
def getPreferences(userName, userDict):
    ''' Gets a user's preferences, whether it is a new user or it was chosen from the menu. Retruns a list with preferences'''
    newPref = ""
    prefs = []
    newPref = input("Enter an artist that you like (Enter to finish):\n" )
        
    while newPref != "":
        prefs.append(newPref.strip())
        newPref = input("Enter an artist that you like (Enter to finish):\n" )
   
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userDict):
    ''' Gets recommendations for a user (currUser) based on the users in userDict and the user's preferences in pref.
        Returns a list of recommended artists.'''
    bestUser = findBestUser(currUser, prefs, userDict)
    if bestUser == None:
        return []
    else:
        recommendations = drop(prefs, userDict[bestUser])
        recommendations.sort()
        return recommendations

def findBestUser(currUser, prefs, userDict):
    ''' Find the user whose tastes are closest to the current user. Return the best user's name (a string) '''
    userlist = userDict.keys()
    users = []
    for user in userlist:
        if user[-1] != '$':
            users += [user]
            
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userDict[user])
        if score > bestScore and currUser != user:
            if userDict[user] != userDict[currUser]:   
                bestScore = score
                bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    extra = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
            extra = list2[j:]
        elif list1[i] < list2[j]:
            i += 1
            extra = list2[j:]
        else:
            list3.append(list2[j])
            j += 1
            extra = list2[j:]
    
    return list3 + extra

def numMatches(list1, list2):
    ''' return the number of elements that match between two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def getArtistDict(userDict):
    """Returns a dictionary with artist names as keys and the number of users that like them as values."""
    userlist = userDict.keys()
    users = []
    for user in userlist:
        if user[-1] != '$':
            users += [user]
    artistDict = {}
    for user in users:
        for artist in userDict[user]:
            if artist not in artistDict:
                artistDict[artist] = 1
            else:
                artistDict[artist] += 1
    return artistDict

def mostPopular(artistDict):
    """Returns a list of the most popular artists from the artist dictionary."""
    return [key for key,val in artistDict.items() if val == max(artistDict.values())]
    # Max expression from StackOverflow (http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary) 
    # to get key with max value from the dictionary. 

def mostLikes(userDict):
    """Determines the user with the most preferences"""
    userlist = userDict.keys()
    users = []
    for user in userlist:
        if user[-1] != '$':
            users += [user]
    mostLikes = 0
    mostUser = []
    for user in users:
        count = len(userDict[user])
        if count > mostLikes:
            mostLikes = count
            mostUser = [user]
        elif count == mostLikes:
            mostUser += [user]
    return mostUser

def saveUserPreferences(userName, prefs, userDict, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    file = open(fileName, "w")
    for user in userDict:
        toSave = str(user) + ":" + ",".join(userDict[user]) + \
                    "\n"
        file.write(toSave)
    file.close()   

def main():
    '''The main function for the music recommender'''
    userDict = loadUsers(PREF_FILE)
    
    userName = getUserName(userDict)
    if userDict[userName] == []:
        userDict[userName] = getPreferences(userName, userDict)
    
    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        
        choice = input().strip().title()
        
        if choice == 'E':
            prefs = getPreferences(userName,userDict)
            prefs.sort()
            userDict[userName] = prefs
        elif choice =='R':
            recs = getRecommendations(userName, userDict[userName], userDict)
            if len(recs) == 0:
                print("No recommendations available at this time")
            else:
                for artist in recs:
                    print(artist)
        elif choice == 'P':
            artistDict = getArtistDict(userDict)
            popular = mostPopular(artistDict)
            popular.sort()
            if popular == []:
                print("Sorry, no artists found")
            else:
                for artist in popular:
                    print(artist)
        elif choice == 'H':
            artistDict = getArtistDict(userDict)
            popular = mostPopular(artistDict)
            if artistDict[popular[0]] == 0 or popular == []:
                print("Sorry, no artists found")
            else:
                print(artistDict[popular[0]])
        elif choice == 'M':
            userMost = mostLikes(userDict)
            userMost.sort()
            if userMost == []:
                print("Sorry, no user found")
            for user in userMost:
                print(user)     
        elif choice == 'Q':
             saveUserPreferences(userName, userDict[userName], userDict, PREF_FILE)
             sys.exit(0)
        #else:
        #    print("Invalid Option.")
        

if __name__ == "__main__": main()