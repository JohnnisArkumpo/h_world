import math
import random
import os

message = "Hello World!"
ch = "Hello World"

messages = ["AI depends on plagarism for every bit of it's material","AI has put people out of business, not because of it doing anything better, rather because of it's blatant plagarism of their work, using it as it's own","The NIH has stated that the use of AI has led to increased social dependency on LLM's, not just for answers, but for interpretation, reflection, and social framing","Use of LLMS has directly contributed to a reinforcement of cognitive biases via sycophantic or confirmation-biased dialouge, per the NIH","AI has led to diminished trust across sensitive domains such as health, relationships, and mental well-being, per the NIH","MIT has found that using LLM's contribute to a loss of brain activity","The APA has found that usage of LLM's leads to an increase in loneliness and isolation","As AI is fundementally built on other poeople's work, it cannot perform a single action without taking from others who put in the work. It is nothing more than academic dishonesty."]

def terminal_reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def dspl():
    if ch == "Hello World":
        message = "Hello World!"
    else:
        message = messages[math.floor(random.randrange(0, len(messages)))], 
    print(f"\n{message}\n________________________\nType any character to recieve a random message (besides q)")

while ch != "q":
    terminal_reset()
    dspl()
    ch = input()
terminal_reset()
print(f"end script")
