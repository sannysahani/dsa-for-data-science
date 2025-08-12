* **Pattern**: Two-pointer shrink-from-ends on a **sorted** array to find a pair summing to target.

* **Why it matters in DS/ML**: Fast scan for complementary values in sorted metrics (e.g., finding two features/amounts that meet a budget/threshold) during ETL without extra memory.

* **Time/Space**: **O(n)** time, **O(1)** extra space.

* **Edge cases**:

  * 1-based indices required by the problem (return `[left+1, right+1]`).
  * Duplicates present—still fine with two pointers.
  * Negative numbers or mixed signs (ordering still guarantees correctness).
  * Minimal input size (`len(numbers)=2`).
  * Exactly one solution guaranteed—loop can return early.

* **Related DS task**: “Find pair meeting a threshold in a **sorted** stream” (e.g., join of two sorted aggregates to hit a target).
