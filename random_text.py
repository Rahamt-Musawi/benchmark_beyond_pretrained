import random
import string

class RandomTextGenerator:
    def __init__(self, min_word_length, max_word_length, min_sentence_length, max_sentence_length):
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.min_sentence_length = min_sentence_length
        self.max_sentence_length = max_sentence_length

    def generate_word(self):
        # Ensure word length is at least `min_word_length`
        word_length = random.randint(self.min_word_length, self.max_word_length)
        word = ''.join(random.choice(string.ascii_letters) for _ in range(word_length))
        return word.capitalize() if random.random() < 0.2 else word

    def generate_sentence(self):
        # Ensure sentence length is at least `min_sentence_length`
        sentence_length = random.randint(self.min_sentence_length, self.max_sentence_length)
        sentence = ' '.join(self.generate_word() for _ in range(sentence_length))
        return sentence + random.choice('.!?')

    def generate_examples(self, num_examples):
        return [self.generate_sentence() for _ in range(num_examples)]

def save_to_txt(examples, filename='random_sentences.txt'):
    # Save the generated sentences to a text file, each on a new line
    with open(filename, 'w', encoding='utf-8') as txtfile:
        for example in examples:
            txtfile.write(example + '\n')

def main(min_word_length, max_word_length, min_sentence_length, max_sentence_length, num_examples):
    generator = RandomTextGenerator(min_word_length, max_word_length, min_sentence_length, max_sentence_length)
    examples = generator.generate_examples(num_examples)
    save_to_txt(examples)
    return examples
