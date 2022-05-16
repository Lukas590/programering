import random

import requests, lxml
from bs4 import BeautifulSoup
from playsound import playsound
import cv2



image = cv2.imread("R.jpg")
cv2.imshow("magic 8 ball", image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

def magic8ball():
    response = input("(Press 'any key' for answer and 'quit' to exit)\nWhat is your question?\n")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=' + response, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    result = soup.find('div', class_='Z0LcW')


    Eightball_answers = [
        "It is certain",
        "Outlook good",
        "You may rely on it",
        "Ask again later",
        "Concentrate and ask again",
        "Reply hazy, try again",
        "My reply is no",
        "My sources say no",
        "Without a doubt",
        "Better not tell you now",
        "Very doubtful",
        "Signs point to yes",
        "Don't count on it",
        "It is decidedly so",
        "Yes definitely"
        ]
    
    if response == "quit":
        print("Have A Good Day!")
    else:
        cv2.imshow("magic 8 ball", image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        playsound('magic-chime-02.wav')
        if result == None:
            print(random.choice(Eightball_answers), "\n")
        else:
            print(result.text)

        magic8ball()

magic8ball()
