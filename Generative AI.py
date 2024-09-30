#GENERATIVE AI 
#Lwazi Somtsewu

import random

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.words = {}
    
    def train(self, text):
        # Split the text into words
        words = text.split()
        
        # Build the Markov chain
        for i in range(len(words) - self.order):
            key = tuple(words[i:i + self.order])
            next_word = words[i + self.order]
            if key not in self.words:
                self.words[key] = []
            self.words[key].append(next_word)

    def generate_sentence(self, length=10):
        # Start with a random key
        key = random.choice(list(self.words.keys()))
        sentence = list(key)

        for _ in range(length - self.order):
            next_word_options = self.words.get(key)
            if not next_word_options:
                break  # Stop if no next words are found
            next_word = random.choice(next_word_options)
            sentence.append(next_word)
            key = tuple(sentence[-self.order:])  # Move the window

        return ' '.join(sentence)

def main():
    # Sample text corpus (you can replace this with any large text)
    corpus = (
        "Generative AI is a fascinating field. "
        "It allows us to create new content based on existing data. "
        "Markov chains are a simple way to generate text. "
        "They work by predicting the next word based on the previous words. "
        "With enough data, you can create surprisingly coherent sentences."
    )
    
    # Create a Markov chain instance
    markov_chain = MarkovChain(order=2)
    markov_chain.train(corpus)

    # Generate a sentence
    generated_sentence = markov_chain.generate_sentence(length=10)
    print("Generated Sentence:", generated_sentence)

if __name__ == "__main__":
    main()
