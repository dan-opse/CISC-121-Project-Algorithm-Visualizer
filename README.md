# Algorithm Name: Binary Search


## Test Case #1 (Sorted + target exists):

Test input: 2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78

Test target: 8

<img width="1410" height="296" alt="Screenshot 2025-12-03 at 4 46 10 PM" src="https://github.com/user-attachments/assets/ccb7af2a-1a47-4748-adc1-dbf5f5f51a86" />

<img width="1406" height="697" alt="Screenshot 2025-12-03 at 4 47 56 PM" src="https://github.com/user-attachments/assets/eaa776fb-9596-4742-90cb-e6076baaf1e1" />



## Test Case #2 (Unsorted):

Test input: 2, 5, 45, 12, 23, 23, 38, 45, 56, 67, 78

Test target: 2

<img width="1408" height="311" alt="Screenshot 2025-12-03 at 4 50 29 PM" src="https://github.com/user-attachments/assets/10ae9f10-0208-42d7-9d20-79790ff70f16" />



## Problem Breakdown & Computational Thinking (You can add a flowchart and write the four pillars of computational thinking briefly in bullets)

### Flow Chart:

<img width="4800" height="5614" alt="flowchart" src="https://github.com/user-attachments/assets/f75b96a8-0461-4bef-bbbd-170ec0400b9b" />

### Four Pillars of Computational Thinking:

1. **Decomposition**
   - **Breaking down the problem:** I separated the project into three distinct components: Input Validation (parsing strings to integers), The Core Algorithm (Binary Search logic), and Visualization (generating HTML for Gradio).
   - **Step-wise Breakdown:** The search itself is decomposed into smaller repeated steps:
     1. Calculate the middle index.
     2. Compare the middle value to the target.
     3. Decide which half to discard.
     4. Update pointers (`left` or `right`).

2. **Pattern Recognition**
   - **Sorted Data Property:** Recognized that in a sorted list, if `mid < target`, the target *cannot* exist to the left. This pattern allows us to ignore half the array safely.
   - **Repetitive Logic:** The process of "finding the middle" and "shrinking the window" is identical in every step, regardless of array size. This pattern is implemented using a `while` loop that repeats until the pointers cross.

3. **Abstraction**
   - **Data Abstraction:** The algorithm ignores what the numbers represent (e.g., ages, prices) and focuses purely on their numerical value and index.
   - **Visualization Abstraction:** For the user interface, I abstracted away the complex memory operations. Instead of showing raw variable states, I used color coding to represent the state:
     - **Gold:** The current middle element being compared.
     - **Blue:** The active search range (Left to Right).
     - **Gray:** The "abstracted" or discarded data that is no longer relevant to the search.

4. **Algorithm**
   - **Input Flow:**
      - **1)** The user provides a comma-separated string
      - **2)** The app cleans whitespace and converts to a list of Integers
      - **3)** The app checks if the list is sorted.
   - **Processing:** The `binary_search_with_steps` function runs the loop. Instead of just returning a result, it records the state of the array (pointers and colors) into a dictionary at every iteration.
   - **Output Flow:** The recorded steps are compiled into an HTML string which is rendered by the Gradio interface, providing the user with a step-by-step visual walkthrough and a Big-O complexity analysis.
  

## Steps to Run

### Option 1: Run Locally
1. **Clone the repository:**

```
git clone https://github.com/dan-opse/CISC-121-Project-Algorithm-Visualizer.git

cd CISC-121-Project-Algorithm-Visualizer
```

2. **Intall dependencies from requirements or directly:**

```
pip install -r requirements.txt
```
  Windows:

```
pip install gradio
```

  MacOS:

```
brew install gradio
```

3. **Run the app:**

```
python3 app.py
```

4. **Open in browser**

### Option 2: Use Hugging Face

Visit the [Hugging Face Space](https://huggingface.co/spaces/tannum/binary-search-visualizer)

## Hugging Face Link: [*click here*](https://huggingface.co/spaces/tannum/binary-search-visualizer)

## Author & Acknowledgment
- **Author:** Daniel Cheah
- **Course:** CISC 121

