import random
import string
import csv

class RandomTextGenerator:
    def __init__(self, max_word_length, max_sentence_length):
        self.max_word_length = max_word_length
        self.max_sentence_length = max_sentence_length

    def generate_word(self):
        word_length = random.randint(1, self.max_word_length)
        word = ''.join(random.choice(string.ascii_letters) for _ in range(word_length))
        return word.capitalize() if random.random() < 0.2 else word

    def generate_sentence(self):
        sentence_length = random.randint(1, self.max_sentence_length)
        sentence = ' '.join(self.generate_word() for _ in range(sentence_length))
        return sentence + random.choice('.!?')

    def generate_examples(self, num_examples):
        return [self.generate_sentence() for _ in range(num_examples)]

def save_to_csv(examples, filename='random_sentences.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sentence'])
        for example in examples:
            writer.writerow([example])

def main(max_word_length, max_sentence_length, num_examples):
    generator = RandomTextGenerator(max_word_length, max_sentence_length)
    examples = generator.generate_examples(num_examples)
    save_to_csv(examples)
    return examples