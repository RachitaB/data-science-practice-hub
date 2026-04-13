# 🐍 Roman Numeral to Integer

## 📌 Problem Statement
Given a valid **Roman numeral**, convert it into its corresponding **integer value**.

Roman numerals are represented by combinations of the following symbols:

---

## 📊 Roman Numeral Mapping

| Symbol | Value |
|--------|------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

---

## 📝 Rules
Roman numerals are generally written from **largest to smallest** from left to right.

For example:

- **XI = 10 + 1 = 11**
- **XXX = 10 + 10 + 10 = 30**

However, in certain cases, a **smaller numeral appears before a larger numeral** to indicate subtraction.

### Subtraction Cases

| Combination | Value |
|-----------|------|
| IV | 4 |
| IX | 9 |
| XL | 40 |
| XC | 90 |
| CD | 400 |
| CM | 900 |

---

## 🧾 Example 1

### Input
```python
s = "XI"
```

### Output
```python
11
```

### Explanation
- X = 10  
- I = 1  

> **XI = 10 + 1 = 11**

---

## 🧾 Example 2

### Input
```python
s = "LXIX"
```

### Output
```python
69
```

### Explanation
- L = 50  
- X = 10  
- IX = 9  

> **LXIX = 50 + 10 + 9 = 69**

---

## 🧠 Approach
- Create a dictionary mapping Roman numerals to integer values  
- Traverse the string from left to right  
- If current numeral is smaller than next numeral:
  - Subtract it  
- Otherwise:
  - Add it  
- Return final total  

---

## 🚀 Python Solution

```python
def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total
```

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

## 🚀 Key Concepts
- Hash Maps / Dictionaries  
- String Traversal  
- Conditional Logic  
- Roman Numeral Rules  

---
