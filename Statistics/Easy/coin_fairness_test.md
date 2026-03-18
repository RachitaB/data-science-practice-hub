# 🪙 Coin Fairness Test (Facebook)

## ❓ Problem

You flip a coin 10 times and observe only **1 head**.
Test whether the coin is fair.

---

## 🧠 Hypothesis

* **H₀ (Null Hypothesis):** Coin is fair → p = 0.5
* **H₁ (Alternative Hypothesis):** Coin is biased towards tails → p < 0.5

---

## 📊 Approach

* Number of trials (n) = 10
* Observed heads = 1

We use **binomial distribution** (small sample, no CLT).

Total possible outcomes:
2¹⁰ = 1024

Number of outcomes with exactly 1 head:
= 10

---

## 📉 P-value

p-value = 10 / 1024 = **0.0098**

---

## ✅ Conclusion

Since **p-value (0.0098) < 0.05**,
we **reject the null hypothesis**.

👉 The coin is likely **biased towards tails**.

---

## ⚠️ Note

* Normal approximation is **not valid** (small sample size)
* Exact binomial probability is used

---
