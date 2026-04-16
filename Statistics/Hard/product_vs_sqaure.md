# 🎲 Expected Value Comparison of Two Dice Games

## 📌 Question
There are **two dice games** you can play:

### **Game 1**
- Roll **two dice**
- Earn an amount equal to the **product** of the two rolls  

### **Game 2**
- Roll **one die**
- Earn an amount equal to the **square** of the roll  

Determine:

> **Which game has the higher expected value, and why?**

---

## 🧠 Solution

Let:

- **X** = Outcome of the first die  
- **Y** = Outcome of the second die  

---

## 🎲 Game 1: Product of Two Dice

We want:

```text
E(XY)
```

Using the expected value formula:

```text
E(XY) = E(X) × E(Y) + Cov(X,Y)
```

Since the dice rolls are **independent**:

```text
Cov(X,Y) = 0
```

Thus:

```text
E(XY) = E(X) × E(Y)
```

The expected value of one fair die is:

```text
E(X) = E(Y) = (1+2+3+4+5+6)/6
```

```text
E(X) = 3.5
```

Therefore:

```text
E(XY) = 3.5 × 3.5
```

```text
E(XY) = 12.25
```

---

## 🎲 Game 2: Square of One Die

We want:

```text
E(X²)
```

Calculate the average of squared outcomes:

```text
E(X²) = (1² + 2² + 3² + 4² + 5² + 6²)/6
```

```text
E(X²) = (1 + 4 + 9 + 16 + 25 + 36)/6
```

```text
E(X²) = 91/6
```

```text
E(X²) = 15.17
```

---

## ✅ Final Comparison

| Game | Expected Value |
|------|---------------|
| Game 1 (Product of Two Dice) | 12.25 |
| Game 2 (Square of One Die) | 15.17 |

---

## 🏆 Conclusion

> **Game 2 has the higher expected value**

### Why?
Because:

```text
15.17 > 12.25
```

Thus, rolling **one die and squaring it** provides a better expected payout than rolling **two dice and multiplying them**.

---

## 🚀 Key Concepts Used

- Expected Value  
- Independence of Variables  
- Covariance  
- Probability Theory  
- Mathematical Expectation  

---
