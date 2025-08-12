* **Pattern**: XOR / arithmetic-sum trick to recover the single missing value from the range `[0..n]` without extra memory.

* **Why it matters in DS/ML**: Quick integrity check for sequential IDs (rows, folds, encoded classes) during ETL to detect gaps before joins/analytics.

* **Time/Space**:

  * *My implementation (`if i not in nums` loop)*: **O(n²)** time, **O(1)** space (linear scan per membership).
  * *Optimal (XOR or Gauss sum)*: **O(n)** time, **O(1)** space.

* **Edge cases**:

  * Missing `0` (e.g., `nums = [1,2,...,n]`).
  * Missing `n` (e.g., `nums = [0,1,...,n-1]`).
  * Tiny inputs (`n = 1`).
  * Unsorted input (XOR/sum are order-agnostic).
  * If using sum in fixed-width languages, beware overflow (Python is safe).

* **Related DS task**: Audit gaps in sequential primary keys.
