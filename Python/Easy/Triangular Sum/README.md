# 🐍 Triangular Sum of an Array

## 📌 Problem Statement
You are given an integer array **nums**, where each element is a **single digit (0–9)**.

The **triangular sum** of the array is obtained by repeatedly:

1. Replacing the array with a new array where each element is:

> **(nums[i] + nums[i+1]) % 10**

2. Continuing until only **one element remains**

Return that final remaining value.

---

## 📝 Process Rules
Given an array of length **n**:

- If **n = 1**, stop and return the only element  
- Otherwise:
  - Create a new array of length **n - 1**
  - Each new element is calculated as:

> **(nums[i] + nums[i+1]) % 10**

- Replace original array with new array  
- Repeat until one element remains  

---

## 🧾 Example 1

### Input

```python
nums = [1, 3, 5, 7]

Step-by-Step
Iteration 1
[(1+3)%10, (3+5)%10, (5+7)%10]
= [4, 8, 2]
Iteration 2
[(4+8)%10, (8+2)%10]
= [2, 0]
Iteration 3
[(2+0)%10]
= [2]
Output
2
🧾 Example 2
Input
nums = [9, 7, 5, 3]
Step-by-Step
Iteration 1
[(9+7)%10, (7+5)%10, (5+3)%10]
= [6, 2, 8]
Iteration 2
[(6+2)%10, (2+8)%10]
= [8, 0]
Iteration 3
[(8+0)%10]
= [8]
Output
8
🧠 Approach
Continue reducing the array until only one element remains
In each pass:
Create a new array of adjacent sums modulo 10
Return final remaining element
🚀 Python Solution
def triangular_sum(nums):
    while len(nums) > 1:
        nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
    
    return nums[0]
🔍 Complexity Analysis
Metric	Value
Time Complexity	O(n²)
Space Complexity	O(n)
🚀 Key Concepts
Arrays
Iterative Reduction
Modulo Arithmetic
List Comprehension
Simulation Problems
