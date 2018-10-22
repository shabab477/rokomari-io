### Problem Description:
Rokomari has decided to give you some books for free and you will also be given an opportunity to make some profit. Books will be placed in a line and you can pick one book at a time. Let’s say Price of ith book is defined with `price (i)`. Upon picking ith book, you will gain profit of `price (i) * price (i - 1) * price (i + 1)`. In words, prices of adjacent books will be multiplied with current picked book and will be contributed to profit. But if any adjacent book is not available (e.g: Books at the ends), you don’t need to consider that. Also note that, after picking `i-th` book, `(i-1)-th` book and `(i + 1)-th` book will become adjacent. Now, you’re wondering, what is the maximum profit that you can make?

### Input Specification:
###### Input start with an integer T (<10), denoting the number of test cases.
###### Each case will start with a number n, denoting the number of books.
###### Next line will contain n numbers where ith number represents price (i) (1 <= price (i) <= 500).
- *Subtask1: Solve with input* `n = 10`.
- *Subtask2: Solve with input* `n = 100`.

### Output Specification:
*For each case, print the **case number** and a **number denoting maximum profit.***

##### Sample Input:
`1`

`3`

`4 5 6`
##### Sample Output:
`Case 1: 150`

**Explanation of sample input:** Picking `5` first will result in `(4 * 5 * 6)`. Then, picking 4 will result in `(4 * 6)`. Then picking 6 will result in `(6)`. Profit: `(4 * 5 * 6) + (4 * 6) + 6` = `150`
