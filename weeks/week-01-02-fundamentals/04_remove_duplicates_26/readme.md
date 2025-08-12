* **Pattern**: In-place two-pointer dedup on a **sorted** array (slow `j` keeps last unique, fast `i` scans ahead).

* **Why it matters in DS/ML**: Efficiently deduplicates sorted IDs/keys during ETL without extra memory—useful before joins, group-bys, or cardinality checks.

* **Time/Space**: **O(n)** time, **O(1)** extra space.

* **Edge cases**:

  * All elements identical → result length `1`.
  * All elements unique → result length `len(nums)`.
  * Runs of duplicates of varying lengths.
  * Input must be **sorted**; otherwise this strategy fails.
  * Postcondition: only the **first `k` positions** (returned length) are valid; trailing values are unspecified.

* **Related DS task**: “Deduplicate sorted primary keys / compress consecutive duplicates in clickstream logs.”
