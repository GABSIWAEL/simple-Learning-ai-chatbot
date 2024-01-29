import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SimpleChatbot:
    def __init__(self):
        self.responses_file = "responses.txt"
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.user_inputs = []
        self.bot_responses = []

    def load_responses(self):
        if os.path.exists(self.responses_file):
            with open(self.responses_file, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i % 2 == 0:
                        self.user_inputs.append(line.strip())
                    else:
                        self.bot_responses.append(line.strip())

    def save_responses(self):
        with open(self.responses_file, "w") as file:
            for user_input, bot_response in zip(self.user_inputs, self.bot_responses):
                file.write(user_input + "\n")
                file.write(bot_response + "\n")

    def learn_from_user_input(self, user_input, category="user_input"):
        if not self.user_inputs:
            self.vectorizer.fit_transform([user_input])
        else:
            self.vectorizer.fit_transform(self.user_inputs + [user_input])

        X = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(
            X, self.vectorizer.transform(self.user_inputs))
        if np.max(similarities) > 0.5:
            index = np.argmax(similarities)
            response = self.bot_responses[index]
            print(response)
        else:
            response = input(
                f"Please provide a better response for this situation: {user_input}\n")
            self.user_inputs.append(user_input)
            self.bot_responses.append(response)
            self.save_responses()

    def chat(self):
        print("Simple Greeting Chatbot: Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            self.learn_from_user_input(user_input, category="user_input")


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.load_responses()
    chatbot.chat()


class SimpleChatbot:
    def __init__(self):
        self.responses_file = "responses.txt"
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.user_inputs = []
        self.bot_responses = []

    def load_responses(self):
        if os.path.exists(self.responses_file):
            with open(self.responses_file, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i % 2 == 0:
                        self.user_inputs.append(line.strip())
                    else:
                        self.bot_responses.append(line.strip())

    def save_responses(self):
        with open(self.responses_file, "w") as file:
            for user_input, bot_response in zip(self.user_inputs, self.bot_responses):
                file.write(user_input + "\n")
                file.write(bot_response + "\n")

    def learn_from_user_input(self, user_input, category="user_input"):
        if not self.user_inputs:
            self.vectorizer.fit_transform([user_input])
        else:
            self.vectorizer.fit_transform(self.user_inputs + [user_input])

        X = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(
            X, self.vectorizer.transform(self.user_inputs))
        if np.max(similarities) > 0.5:
            index = np.argmax(similarities)
            response = self.bot_responses[index]
            print(response)
        else:
            response = input(
                f"Please provide a better response for this situation: {user_input}\n")
            self.user_inputs.append(user_input)
            self.bot_responses.append(response)
            self.save_responses()

    def chat(self):
        print("Simple Greeting Chatbot: Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            self.learn_from_user_input(user_input, category="user_input")


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.load_responses()
    chatbot.chat()


class SimpleChatbot:
    def __init__(self):
        self.responses_file = "responses.txt"
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.user_inputs = []
        self.bot_responses = []

    def load_responses(self):
        if os.path.exists(self.responses_file):
            with open(self.responses_file, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i % 2 == 0:
                        self.user_inputs.append(line.strip())
                    else:
                        self.bot_responses.append(line.strip())

    def save_responses(self):
        with open(self.responses_file, "w") as file:
            for user_input, bot_response in zip(self.user_inputs, self.bot_responses):
                file.write(user_input + "\n")
                file.write(bot_response + "\n")

    def learn_from_user_input(self, user_input, category="user_input"):
        if not self.user_inputs:
            self.vectorizer.fit_transform([user_input])
        else:
            self.vectorizer.fit_transform(self.user_inputs + [user_input])

        X = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(
            X, self.vectorizer.transform(self.user_inputs))
        if np.max(similarities) > 0.5:
            index = np.argmax(similarities)
            response = self.bot_responses[index]
            print(response)
        else:
            response = input(
                f"Please provide a better response for this situation: {user_input}\n")
            self.user_inputs.append(user_input)
            self.bot_responses.append(response)
            self.save_responses()

    def chat(self):
        print("Simple Greeting Chatbot: Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            self.learn_from_user_input(user_input, category="user_input")


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.load_responses()
    chatbot.chat()


class SimpleChatbot:
    def __init__(self):
        self.responses_file = "responses.txt"
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.user_inputs = []
        self.bot_responses = []

    def load_responses(self):
        if os.path.exists(self.responses_file):
            with open(self.responses_file, "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if i % 2 == 0:
                        self.user_inputs.append(line.strip())
                    else:
                        self.bot_responses.append(line.strip())

    def save_responses(self):
        with open(self.responses_file, "w") as file:
            for user_input, bot_response in zip(self.user_inputs, self.bot_responses):
                file.write(user_input + "\n")
                file.write(bot_response + "\n")

    def learn_from_user_input(self, user_input, category="user_input"):
        if not self.user_inputs:
            self.vectorizer.fit_transform([user_input])
        else:
            self.vectorizer.fit_transform(self.user_inputs + [user_input])

        X = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(
            X, self.vectorizer.transform(self.user_inputs))
        if np.max(similarities) > 0.5:
            index = np.argmax(similarities)
            response = self.bot_responses[index]
            print(response)
        else:
            response = input(
                f"Please provide a better response for this situation: {user_input}\n")
            self.user_inputs.append(user_input)
            self.bot_responses.append(response)
            self.save_responses()

    def chat(self):
        print("Simple Greeting Chatbot: Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            self.learn_from_user_input(user_input, category="user_input")


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.load_responses()
    chatbot.chat()
