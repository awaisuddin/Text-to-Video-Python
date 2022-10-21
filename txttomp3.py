# Import the required module
import pyttsx3

import csv
joke = ""
with open('Datasets/jokes2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        joke = str(row[1])+"     "+str(row[2])
        print(joke)
        # Create a string
        string = joke
        # Initialize the Pyttsx3 engine
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[5].id)

        engine.setProperty("rate", 168)
          
        # We can use file extension as mp3 and wav, both will work
        engine.save_to_file(string, "mp3/"+str(row[0])+".mp3")
          
        # Wait until above command is not finished.
        engine.runAndWait()
