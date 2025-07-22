#!/usr/bin/env python3
"""
MY ALU PLAGIARISM DETECTOR APPLICATION:
This Plagiarism detector program compares two essays and determines their plagiarism percentage
using set operations and text analysis.
"""
import re
import os
from collections import Counter

class PlagiarismDetector:
    def __init__(self, file1_path, file2_path):
        """
        This helps Initialize the PlagiarismDetector with the two essay file paths

        Args:
            file1_path (str): Path to the first essay file
            file2_path (str): Path to the second essay file
        """
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.essay1_content = ""
        self.essay2_content = ""
        self.essay1_words = []
        self.essay2_words = []
        self.essay1_word_count = Counter()
        self.essay2_word_count = Counter()

    def read_files(self):
        """
       This Reads both essay files and store their contents

        Returns:
            bool:It shows True if both files were read successfully and shows False otherwise
        """
        try:
            # Check if the files exist before
            if not os.path.exists(self.file1_path):
                print(f"Error: File '{self.file1_path}' not found.")
                return False
            if not os.path.exists(self.file2_path):
                print(f"Error: File '{self.file2_path}' not found.")
                return False

            # This Reads essay 1
            with open(self.file1_path, 'r', encoding='utf-8') as file1:
                self.essay1_content = file1.read()

            # This Reads essay 2
            with open(self.file2_path, 'r', encoding='utf-8') as file2:
                self.essay2_content = file2.read()

            print(" Files read successfully!")
            return True

        except Exception as e:
            print(f"Error reading files: {e}")
            return False

    def preprocess_text(self, text):
        """
        Preprocess the text by removing punctuation, converting to lowercase,
        and splitting them into words

        Args:\
            text (str): Raw text to preprocess

        Returns:
            list: List of the preprocessed words
        """
        # Convert to lowercase.
        text = text.lower()

        # Remove the punctuations and split them into words
        # This regex helps keeps only letters, numbers, and spaces
        words = re.findall(r'\b[a-zA-Z]+\b', text)

        # Filter out the empty strings and very short words to it
        words = [word for word in words if len(word) > 1]

        return words

    def analyze_essays(self):
        """
        Analyze both essays by preprocessing text and counting words
        """
        print("\n" + "="*50)
        print("ANALYZING ESSAYS")
        print("="*50)

        # Preprocess both essays
        self.essay1_words = self.preprocess_text(self.essay1_content)
        self.essay2_words = self.preprocess_text(self.essay2_content)

        # Count word frequencies
        self.essay1_word_count = Counter(self.essay1_words)
        self.essay2_word_count = Counter(self.essay2_words)

        print(f"Essay 1 total words: {len(self.essay1_words)}")
        print(f"Essay 1 unique words: {len(self.essay1_word_count)}")
        print(f"Essay 2 total words: {len(self.essay2_words)}")
        print(f"Essay 2 unique words: {len(self.essay2_word_count)}")

    def find_common_words(self):
        """
        Find words that appear in both essays and display their frequencies

        Returns:
            set: Set of common words
        """
        print("\n" + "="*50)
        print("FINDING COMMON WORDS")
        print("="*50)

        # Use set intersection to find common words
        essay1_set = set(self.essay1_word_count.keys())
        essay2_set = set(self.essay2_word_count.keys())
        common_words = essay1_set.intersection(essay2_set)

        print(f"Number of common words: {len(common_words)}")
        print("\nCommon words and their frequencies:")
        print("-" * 40)

        # Sort common words alphabetically for better display
        for word in sorted(common_words):
            count1 = self.essay1_word_count[word]
            count2 = self.essay2_word_count[word]
            print(f"{word:<15} | Essay 1: {count1:>3} | Essay 2: {count2:>3}")

        return common_words

    def search_word(self, word):
        """
        Search for a specific word in both essays

        Args:
            word (str): Word to search for

        Returns:
            bool: True if word is found in at least one essay, False otherwise
        """
        if not word or not isinstance(word, str):
            print("Error: Please enter a valid word.")
            return False

        # Convert search word to lowercase for case-insensitive search
        word = word.lower().strip()

        # Get word counts from both essays
        count1 = self.essay1_word_count.get(word, 0)
        count2 = self.essay2_word_count.get(word, 0)

        print(f"\nSearch results for '{word}':")
        print("-" * 30)
        print(f"Essay 1: {count1} occurrences")
        print(f"Essay 2: {count2} occurrences")

        # Return True if word is found in at least one essay
        if count1 > 0 or count2 > 0:
            print(f"Word '{word}' found!")
            return True
        else:
            print(f" Word '{word}' not found in either essay.")
            return False

    def calculate_plagiarism_percentage(self):
        """
        Calculate plagiarism percentage using set operations

        Returns:
            float: Plagiarism percentage
        """
        print("\n" + "="*50)
        print("CALCULATING PLAGIARISM PERCENTAGE")
        print("="*50)

        # Get unique words from both essays
        essay1_set = set(self.essay1_word_count.keys())
        essay2_set = set(self.essay2_word_count.keys())

        # Calculate intersection of the common words
        intersection = essay1_set.intersection(essay2_set)

        # Calculate all the unique words
        union = essay1_set.union(essay2_set)

        # Calculate the plagiarism percentage
        if len(union) == 0:
            plagiarism_percentage = 0
        else:
            plagiarism_percentage = (len(intersection) / len(union)) * 100

        print(f"Common words (intersection): {len(intersection)}")
        print(f"Total unique words (union): {len(union)}")
        print(f"Plagiarism percentage: {plagiarism_percentage:.2f}%")

        # This Determines if there is plagiarism of about 50%
        if plagiarism_percentage >= 50:
            print("\n PLAGIARISM DETECTED!")
            print("The essays show significant similarity (≥50%)")
        else:
            print("\n NO PLAGIARISM DETECTED")
            print("The essays show acceptable similarity (<50%)")

        return plagiarism_percentage

    def display_menu(self):
        """
        Displays the main menu options for you to select
        """
        print("\n" + "="*50)
        print("PLAGIARISM DETECTOR MENU")
        print("="*50)
        print("1. Compare Essays and Show Common Words")
        print("2. Search for a Specific Word")
        print("3. Calculate Plagiarism Percentage")
        print("4. Run Complete Analysis")
        print("5. Exit")
        print("-" * 50)

    def run(self):
        """
       The Main program loop
        """
        print("="*60)
        print("         PLAGIARISM APPLICATION")
        print("="*60)

        # This Reads the essay files
        if not self.read_files():
            return

        # This is to Analyze the essays
        self.analyze_essays()

        while True:
            self.display_menu()

            try:
                choice = input("Enter your choice (1-5): ").strip()
                if choice == '1':
                    self.find_common_words()

                elif choice == '2':
                    word = input("Enter a word to search: ").strip()
                    self.search_word(word)

                elif choice == '3':
                    self.calculate_plagiarism_percentage()

                elif choice == '4':
                    # Run complete analysis
                    common_words = self.find_common_words()
                    self.calculate_plagiarism_percentage()

                elif choice == '5':
                    print("\nThank You for using our Plagiarism Detector!")
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    """
    This is the Main function to run the plagiarism detector
    """
    # Define the file paths
    essay1_file = "essay1.txt"
    essay2_file = "essay2.txt"

    # This creates and run the plagiarism detector
    detector = PlagiarismDetector(essay1_file, essay2_file)
    detector.run()

if __name__ == "__main__":
    main()
