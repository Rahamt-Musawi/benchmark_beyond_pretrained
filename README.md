# Beyond Pre-trained Advantages
## A Reasoning Benchmark Using Ciphers
This project aims to develop a robust benchmark to evaluate the reasoning capabilities of LLMs using cipher tasks. 

### Note
You can ask the related pdf file. 

## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [File Structure](#file_folder-file-structure)
- [Cipher](#cipher)


##  :beginner: About
This thesis presents a diverse range of cipher tasks to evaluate LLMs’ capabilities in a
challenging reasoning level beyond their pre-trained knowledge. Our work incorporates
various configurations and complexity levels. We bring variations in the shift values
to asses how LLMs can cope with positional entanglement. We further complexify the
assesment process by defining tasks in different cipher environments such as Caesar
ciphers, Vigenère ciphers, and multistage transposition ciphers, each adding unique layers
of complexity that ensure novelty in tasks. By designing such benchmark with novel tasks,
we evaluate if the model capabilities go beyond their pre-trained knowledge scope and
generalize their training knowledge on unfamiliar tasks. Furthermore, the consistent,
language-agnostic nature of this benchmark makes it very suitable for assessing LLMs’
capabilities in multilingual settings. We evaluate the same task configurations in Greek,
which further tests the models’ reasoning ability across linguistic boundaries.




## :zap: Usage
This project is used to step toward contamination-resistant benchmarking. 




###  :file_folder: File Structure


```
Project
SOME OF IMPORTANT DIRECTORIES
├── Benchmark_Beyond_Pretrained
│   ├── data
│   │   ├── encoded ── ├─── caesar-cipher ├─ greek
│   │   └── original   └─ vigenere-cipher ├─ natural 
│   ├── dynamic_vigenere_key_dataset      └─ random
│   ├── eval
│   │   ├── caesar_cipher
│   │   ├── lookup_table
│   ├── log
│   ├── random_text_dataset
│   ├── vigenere_dataset
SOME OF IMPORTANT FILES
│   │   ├── prompt.ipynb
│   │   └── metrics.ipynb
│   │   └── ciphers.py
│   │   ├── dynamic-vigenere-key-generator.ipynb
│   │   └── interactive-cipher-generator.ipynb
│   │   └── lookup-table-eval.ipynb
│   │   ├── output-evaluation.ipynb
│   │   └── cc-gold-label-generator-json.ipynb
│   │   └── random_text_generator.py
│   │   └── random-text-generator.ipynb
│   │   └── cipher-generator.ipynb
├── README.md

```

##  :cipher: Cipher
### Main Page
file:///home/rahmat/Downloads/1SjmYA27uLF5bjssDFwt31npqCaVY-BFeNfjH9RX8ayA.png

