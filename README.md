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
   - Break the seearch problem into smaller subproblems (divide and conquer)
   - Cut the array in have every step
   - Reduce search space by removing half of the remaining elements
  
2. **Pattern Recognition**
   - Recognize that a sorted array has a predictable order
   - Identify that middle element comparison determines which half to search
   - Notice the logarithmic reduction pattern (n → n/2 → n/4 → ...)

3. **Abstraction**
   - Focus on the essential comparison logic (target vs. middle element)
   - Ignore irrelevant details about what the data represents
   - Use left/right pointers to represent the search boundaries

4. **Algorithm Design**
   - Create a systematic approach: calculate mid, compare, adjust boundaries
   - Use a while loop that continues until the target is found or search space is exhausted
   - Define base cases: target found (return index) or not found (return -1)
  

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
Daniel Cheah
