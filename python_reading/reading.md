## Chapter 1: Programming as a Way of Thinking

1. **Interdisciplinary Mindset**: Programming combines mathematical rigor (formal logic), engineering principles (system design/tradeoffs), and scientific methodology (hypothesis testing) into a unified problem-solving framework.
2. **Precision Over Ambiguity**: Formal languages like Python demand absolute precision in syntax and structure, unlike natural languages that tolerate redundancy and ambiguity through context.

---

## Chapter 3: Functions

1. **Modular Abstraction**: Functions act as reusable building blocks that encapsulate logic, enabling composition of complex systems from simple components (e.g., `print_verse()` calling `first_two_lines()`).
2. **Execution Stack Visualization**: Stack diagrams reveal how nested function calls create isolated execution contexts, with local variables existing only within their frame's lifetime.

---

## Chapter 5: Conditionals and Recursion

1. **Base Case Discipline**: Effective recursion requires carefully designed base cases to terminate infinite loops, mirroring mathematical induction.
2. **Error-Driven Debugging**: Runtime errors like `RecursionError` expose call stack dynamics, encouraging iterative hypothesis testing ("detective work") to isolate flaws.

---

## Chapter 10: Dictionaries

1. **Hash Table Magic**: Dictionaries achieve O(1) lookups via hashing, enabling massive efficiency gains over linear searches (e.g., 10,000x faster word reversal checks).
2. **Memoization Power**: Storing computed results (e.g., Fibonacci numbers) in dictionaries transforms exponentially slow algorithms into linear-time solutions.

---

## Known vs. Unknown
**What I Knew:**  
The concept of using dictionaries for frequency counting (e.g., `value_counts()`) was familiar from prior work with data analysis patterns.

**What I Didn't Know:**  
The specific Python implementation detail that dictionary keys must be immutable/hashable types to maintain hash table integrity, and why lists (being mutable) can't serve as keys.
