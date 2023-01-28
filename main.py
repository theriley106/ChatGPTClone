import os
import openai
try:
    from keys import *
except:
    API_KEY = input("OpenAI Key: ")

openai.api_key = API_KEY

# Pass in a "Modified" prompt (with the chat history from before)
def fetch_openai_response(prompt):
    start_sequence = "\nAI:"
    restart_sequence = "\nStudent: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Student:", " AI:"]
    )
    return response['choices'][0]['text'].strip()

START_PROMPT = """
You are an AI model that is trained on a classroom lecture in a university setting. I will feed you the
transcript of your lecture today.

At periods of time, I will feed you questions from students in the lecture. These questions will begin
with "Student: ". You will response concisely from the perspective of the professor teaching the course. 
The lecture is as followed:
""".replace("\n", " ")

class ChatGPTClone():
    def __init__(self, lecture):
        # You probably don't need to feed it any lecture to begin
        self.prompt = START_PROMPT + "\n"

    def add_to_prompt(self, text):
        self.prompt += "Student: " + text + "\nAI: "



    def submit(self):
        return fetch_openai_response(self.prompt)

    

if __name__ == "__main__":
    chatGPT = ChatGPTClone("Hello. Today I will be teaching CS50 at Brown University.")
    chatGPT.add_to_prompt("What is this class about?")
    print(chatGPT.submit())
    # print(fetch_openai_response())