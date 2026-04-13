# 🐍 Compound Interest Calculator

## 📌 Problem Statement
Build a **compound interest calculator** that computes the final investment amount using the following inputs:

- **Principal** → Initial amount invested  
- **Interest Rate** → Annual percentage earned on current balance  
- **Annual Contribution** → Fixed amount added at the end of every year  
- **Years to Invest** → Number of years money remains invested  

At the end of each year:

1. Interest is applied to the current balance  
2. Annual contribution is added  

Return the final amount **rounded to two decimal places**.

---

## 📝 Input Variables

| Variable | Description |
|---------|-------------|
| Principal | Starting investment amount |
| Rate | Annual interest rate (%) |
| Contribution | Fixed yearly deposit |
| Years | Total years invested |

---

## 🧾 Example 1

### Input

| principal | rate | contribution | years |
|----------|------|-------------|------|
| 500 | 10 | 50 | 3 |

### Output

```python id="3sd2hr"
831.00
