# 🐍 Total Letters Used in Number Words

## 📌 Problem Statement
Given an integer **N**, calculate the total number of letters used when writing all numbers from **1 to N** (inclusive) in words.

### Rules:
- **Do not count spaces or hyphens**
- Use **British number formatting**
  - Include **"and"** for numbers over 100  
    Example: **115 → "one hundred and fifteen"**
- Assume:

> **1 ≤ N ≤ 1000**

Return the total number of letters used.

---

## 🧾 Example 1

### Input
```python
N = 5
```

### Numbers Written in Words

| Number | Word | Letter Count |
|--------|------|-------------|
| 1 | one | 3 |
| 2 | two | 3 |
| 3 | three | 5 |
| 4 | four | 4 |
| 5 | five | 4 |

### Output
```python
19
```

### Explanation

> **3 + 3 + 5 + 4 + 4 = 19**

---

## 🧠 Approach
- Create a helper function to convert each number into words  
- Handle:
  - Numbers **1–19** directly using dictionary lookup  
  - Numbers **20–99** using tens + ones decomposition  
  - Numbers **100–999** using hundreds logic with British "and"  
  - Number **1000** separately  
- Iterate from **1 to N**
- Sum the length of each word after removing spaces  

---

## 🚀 Python Solution

```python
def total_letters(N):
    def get_word(number):
        base = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
            13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty',
            40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'
        }

        if number == 1000:
            return "onethousand"

        if number >= 100:
            hundreds = base[number // 100] + "hundred"
            if number % 100 != 0:
                hundreds += "and" + get_word(number % 100)
            return hundreds

        if number >= 20:
            return base[(number // 10) * 10] + base.get(number % 10, "")

        return base[number]

    ans = 0
    for num in range(1, N + 1):
        ans += len(get_word(num))

    return ans
```

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(N) |
| Space Complexity | O(1) |

---

## 🚀 Key Concepts
- Dictionaries / Hash Maps  
- Number Decomposition  
- String Concatenation  
- British Number Formatting  
- Simulation / Iteration  

---
