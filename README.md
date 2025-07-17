# Plagiarism Detector

A Python application that compares two essays and determines plagiarism percentage using set operations and text analysis.

## Features

- **Compare Two Essays**: Reads and analyzes two text documents
- **Find Common Words**: Identifies words that appear in both essays with their frequencies
- **Word Search**: Searches for specific words in both essays
- **Plagiarism Calculation**: Calculates plagiarism percentage using set operations
- **Interactive Menu**: User-friendly command-line interface

## Files Structure

```
plagiarism_detector/
├── a.zakariam@alustudent.com_IL-1.py    # Main application
├── essay1.txt                # First essay file
├── essay2.txt                # Second essay file
└── README.md                 # This file
```

## Installation and Setup

1. **Create the project directory:**
   ```bash
   mkdir plagiarism_detector
   cd plagiarism_detector
   ```

2. **Create the main file** (copy the code provided in the main app)

   ```

## Usage

### Running the Main Application

```bash
./a.zakariam@alustudent.com_IL-1.py
```

## How It Works

### 1. Text Preprocessing
- Converts text to lowercase
- Removes punctuation
- Splits text into individual words
- Filters out very short words

### 2. Set Operations
- **Intersection**: Finds common words between essays
- **Union**: Finds all unique words from both essays
- **Plagiarism Percentage**: (Common Words / Total Unique Words) × 100

### 3. Plagiarism Threshold
- **≥50%**: Plagiarism detected
- **<50%**: No plagiarism detected

## Menu Options

1. **Compare Essays and Show Common Words**: Displays all words that appear in both essays with their frequencies
2. **Search for a Specific Word**: Search for a word in both essays and show occurrence count
3. **Calculate Plagiarism Percentage**: Calculate and display the plagiarism percentage
4. **Run Complete Analysis**: Performs all analysis steps
5. **Exit**: Quit the application

## Example Output

```
PLIAGIARISM DETECTOR APPLICATION
==================================================
Files read successfully!

==================================================
ANALYZING ESSAYS
==================================================
Essay 1 total words: 94
Essay 1 unique words: 65
Essay 2 total words: 101
Essay 2 unique words: 74

...
==================================================
 PLAGIARISM DETECTOR MENU
==================================================
1. Compare Essays and Show Common Words
2. Search for a Specific Word
3. Calculate Plagiarism Percentage
4. Run Complete Analysis
5. Exit
--------------------------------------------------
```

## Requirements

- Python 3.x
- Ubuntu Terminal (or any Linux terminal)
- Standard Python libraries: `re`, `os`, `collections`

## Learning Outcomes Covered

1. **File Handling**: Reading and processing text files
2. **Data Structures**: Using lists, sets, and dictionaries
3. **String Manipulation**: Text preprocessing and word extraction
4. **Loops and Iterations**: Iterating through text data
5. **Input/Output Operations**: User interaction and result display

## Error Handling

- File not found errors
- Empty file handling
- Invalid input validation
- Graceful error messages
