# 🐍 Valid Anagram Checker

## 📌 Problem Statement
Given two strings **s** and **t**, return **True** if the two strings are **anagrams** of each other; otherwise return **False**.

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, using **all original letters exactly once**.

### Assumption
- Both strings contain only **lowercase alphabet characters**

---

## 🧾 Example 1

### Input
```python
s = "listen"
t = "silent"
```

### Output
```python
True
```

### Explanation
Both words contain the exact same letters arranged differently.

---

## 🧾 Example 2

### Input
```python
s = "astronomer"
t = "moonstarer"
```

### Output
```python
True
```

### Explanation
Rearranging the letters of **astronomer** forms **moonstarer**.

---

## 🧾 Example 3

### Input
```python
s = "lemur"
t = "lemer"
```

### Output
```python
False
```

### Explanation
The characters differ:
- **lemur** contains **u**
- **lemer** contains extra **e**

Thus, they are not anagrams.

---

## 🧠 Approach
- If lengths differ, return **False**
- Sort both strings
- Compare sorted versions
- If equal, return **True**, else **False**

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n log n) |
| Space Complexity | O(n) |

---

## 🚀 Key Concepts
- String Manipulation  
- Sorting  
- Character Comparison  
- Anagram Validation  

---
