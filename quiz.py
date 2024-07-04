#!/bin/python3

import csv
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_enter():
    input("Press Enter to continue...")

def load_word_pairs(filename):
    word_pairs = []
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            spanish, english = row
            word_pairs.append((spanish, english))
    return word_pairs

def test_user(word_pairs):
    correct = 0
    incorrect = 0
    incorrect_pairs = []

    for spanish, english in word_pairs:
        clear_screen()
        user_input = input(f"spanish: {spanish}\nenglish: ").strip().lower()
        if user_input == english.lower():
            print("Correct!")
            correct += 1
            continue
        else:
            print(f"Incorrect! The correct answer is '{english}'.")
            incorrect += 1
            incorrect_pairs.append((spanish, english))
        
        user_input = input(f"ask again (Y|n)?")
        if user_input == "n":
            incorrect_pairs.remove((spanish, english))
            

    print(f"\nYou got {correct} correct and {incorrect} incorrect.")
    wait_for_enter()

    return incorrect_pairs

def main():
    filename = 'test.csv'  # Replace with your CSV file name
    word_pairs = load_word_pairs(filename)
    
    clear_screen()
    while word_pairs:
        word_pairs = test_user(word_pairs)
        if word_pairs:
            print("\nRe-examining incorrect words...\n")

if __name__ == "__main__":
    main()
