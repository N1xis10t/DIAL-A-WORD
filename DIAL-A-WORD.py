# Import the dictionary
dicti = open("./google-10000-english.txt")
Dictionary = dicti.read().replace("\n", " ").split()
dicti.close()

# Define what letters the numbers can be
letters = {"1":"1",      "2":"A B C",   "3":"D E F", "4":"G H I",   "5":"J K L",
           "6":"M N O", "7":"P Q R S", "8":"T U V", "9":"W X Y Z", "0":"0"}

number = ""

# Garbage word filter
i=1
while i <= len(Dictionary)-1:
    if len(Dictionary[i]) < 3:
        del Dictionary[i]
        i-=1
    i+=1

# Enter the main loop
print("Type 'exit' to quit.")
while True:
    printnums = "\n"
    number = input("Number: ")
    if number == "exit":
        break
    modnumber = ""
    printnumber = ""

    # Start iterating through all the possible letter combinations for the number
    for i in range(0, len(letters[number[0]].split())):
        modnumber += letters[number[0]].split()[i]
        for i in range(0, len(letters[number[1]].split())):
            modnumber += letters[number[1]].split()[i]
            for i in range(0, len(letters[number[2]].split())):
                modnumber += letters[number[2]].split()[i]
                for i in range(0, len(letters[number[3]].split())):
                    modnumber += letters[number[3]].split()[i]
                    for i in range(0, len(letters[number[4]].split())):
                        modnumber += letters[number[4]].split()[i]
                        for i in range(0, len(letters[number[5]].split())):
                            modnumber += letters[number[5]].split()[i]
                            for i in range(0, len(letters[number[6]].split())):
                                modnumber += letters[number[6]].split()[i]
                                for i in range(0, len(letters[number[7]].split())):
                                    modnumber += letters[number[7]].split()[i]
                                    for i in range(0, len(letters[number[8]].split())):
                                        modnumber += letters[number[8]].split()[i]
                                        for i in range(0, len(letters[number[9]].split())):
                                            modnumber += letters[number[9]].split()[i]

                                            # Once the current iteration has been assembled, check to see if it has any English words in it
                                            for i in range(0, len(Dictionary)):
                                                if Dictionary[i].upper() in modnumber:
                                                    # If it does, and it's unique, add it to the list of numbers to be printed out
                                                    word = Dictionary[i].upper()
                                                    wordlocation = modnumber.find(word)
                                                    printnumber = ("^" + number[0:wordlocation] + "-" + word + "-" + number[wordlocation + len(word):] + "^").replace("^-", "").replace("-^", "").replace("^", "")
                                                    if not printnumber in printnums:
                                                        printnums += printnumber + "\n"

                                            # Take away the last character so a new one can be tried
                                            modnumber = modnumber[0:9]
                                        modnumber = modnumber[0:8]
                                    modnumber = modnumber[0:7]
                                modnumber = modnumber[0:6]
                            modnumber = modnumber[0:5]
                        modnumber = modnumber[0:4]
                    modnumber = modnumber[0:3]
                modnumber = modnumber[0:2]
            modnumber = modnumber[0:1]
        modnumber = ""
    
    # Print the results
    if printnums == "\n":
        print("\nNo words found\n")
    else:
        print(printnums)
