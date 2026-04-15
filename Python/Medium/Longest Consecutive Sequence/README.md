# 🐍 Longest Consecutive Sequence

## 📌 Problem Statement
Given an array of integers **nums**, return the **length of the longest consecutive sequence** that can be formed from the array.

A **consecutive sequence** consists of numbers where:

> Each element is exactly **1 greater** than the previous element.

### Notes
- Elements can be selected from **any position** in the array  
- They **do not** need to appear in original order  

---

## 🧾 Example 1

### Input
```python
nums = [100, 4, 200, 1, 3, 2]
```

### Output
```python
4
```

### Explanation
The longest consecutive sequence is:

```python
[1, 2, 3, 4]
```

Its length is:

> **4**

---

## 🧾 Example 2

### Input
```python
nums = [3, 2]
```

### Output
```python
2
```

### Explanation
The longest consecutive sequence is:

```python
[2, 3]
```

Its length is:

> **2**

---

## 🧠 Approach
- Identify all unique numbers in the array  
- Check for consecutive neighboring values  
- Track the maximum streak length found  
- Return the longest sequence length  

---

## 🚀 Key Concepts
- Arrays  
- Consecutive Sequences  
- Hashing / Sets  
- Sequence Tracking  

---
