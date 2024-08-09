import random

def flip_coin():
    return random.choice([True, False])

def process_text(input_text):
    words = input_text.split()
    return ' '.join([word for word in words if flip_coin()])

def main():
    input_text = input("Enter the text: ")
    while True:
        input("Press Enter to get a new result...")
        print(process_text(input_text))

if __name__ == "__main__":
    main()
