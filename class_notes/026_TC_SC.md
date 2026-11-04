Time Complexity (TC) and Space Complexity (SC) — DSA Notes
1. Introduction

When solving a programming problem, we should not only focus on getting the correct answer but also on writing an efficient solution.

We analyze algorithms using two important factors:

Time Complexity (TC): How the running time of an algorithm grows with input size.
Space Complexity (SC): How the memory usage of an algorithm grows with input size.

Both are expressed using Asymptotic Notations, mainly Big O notation.

PART 1: TIME COMPLEXITY (TC)
2. What is Time Complexity?

Time complexity describes how the number of operations performed by an algorithm grows as the input size increases.

It does not measure actual execution time in seconds.

It measures the growth rate of an algorithm.

Example
javascript
for (let i = 0; i < n; i++) {
    console.log(i);
}


If:

n = 5 → 5 iterations
n = 10 → 10 iterations
n = 100 → 100 iterations

Therefore:

Time Complexity = O(n)

3. What is Big O Notation?

Big O notation represents the upper bound of an algorithm's growth rate.

It helps us understand how an algorithm performs when input size becomes very large.

Common Time Complexities
Complexity	Name	Example
O(1)	Constant	Array indexing
O(log n)	Logarithmic	Binary Search
O(n)	Linear	Single loop
O(n log n)	Linearithmic	Merge Sort
O(n²)	Quadratic	Nested loops
O(n³)	Cubic	Three nested loops
O(2ⁿ)	Exponential	Naive Fibonacci
O(n!)	Factorial	Generating all permutations
Growth order (Best to Worst)

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

4. Rules to Calculate Time Complexity
Rule 1: Ignore Constants
javascript
for (let i = 0; i < n; i++) {
    console.log(i);
}

for (let i = 0; i < n; i++) {
    console.log(i);
}


Total operations = n + n = 2n

Ignore the constant 2.

TC = O(n)

Rule 2: Ignore Lower Order Terms

If complexity is:

O(n² + n + 10)

Keep only the highest-order term.

TC = O(n²)

Rule 3: Consecutive Loops
javascript
for (let i = 0; i < n; i++) {
    console.log(i);
}

for (let j = 0; j < n; j++) {
    console.log(j);
}


Total = n + n = 2n

TC = O(n)

Rule 4: Nested Loops
javascript
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        console.log(i, j);
    }
}


Total = n × n = n²

TC = O(n²)

Rule 5: Loop Dividing Input by 2
javascript
while (n > 1) {
    n = Math.floor(n / 2);
}


Each iteration divides n by 2.

TC = O(log n)

Rule 6: Loop Multiplying Input by 2
javascript
for (let i = 1; i < n; i *= 2) {
    console.log(i);
}


Values: 1, 2, 4, 8, 16...

TC = O(log n)

Rule 7: Different Variables in Nested Loops
javascript
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        console.log(i, j);
    }
}


Outer loop = n

Inner loop = m

TC = O(n × m)

Do not automatically write O(n²) when the loop limits are different.

5. Best Case, Average Case and Worst Case

Consider searching for an element in an array using Linear Search.

javascript
function search(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}

Best Case

The target is at the first position.

Only one comparison is needed.

TC = O(1)

Average Case

The target is somewhere around the middle on average.

TC = O(n)

Worst Case

The target is at the last position or is not present.

TC = O(n)

6. Common Algorithm Complexities
Algorithm	Time Complexity
Linear Search	O(n)
Binary Search	O(log n)
Bubble Sort	O(n²) worst case
Selection Sort	O(n²)
Insertion Sort	O(n²) worst case
Merge Sort	O(n log n)
Quick Sort	O(n log n) average
Quick Sort	O(n²) worst case
Heap Sort	O(n log n)
Hash Table Search	O(1) average, O(n) worst case
PART 2: SPACE COMPLEXITY (SC)
7. What is Space Complexity?

Space complexity describes how much memory an algorithm requires as input size increases.

It includes:

Input storage (depending on the convention used).
Variables.
Data structures.
Recursion stack.
Dynamically allocated memory.

In DSA, we often focus on Auxiliary Space.

What is Auxiliary Space?

Auxiliary space is the extra memory used by an algorithm, excluding the input storage itself.

Example:

javascript
function sum(a, b) {
    let result = a + b;
    return result;
}


Extra memory is constant.

Auxiliary SC = O(1)

8. Examples of Space Complexity
Example 1: Constant Space — O(1)
javascript
function findSum(n) {
    let sum = 0;

    for (let i = 1; i <= n; i++) {
        sum += i;
    }

    return sum;
}


Variables:

sum
i
n (input parameter)

The number of variables does not increase with n.

Auxiliary SC = O(1)

Example 2: Linear Space — O(n)
javascript
function createArray(n) {
    let arr = [];

    for (let i = 0; i < n; i++) {
        arr.push(i);
    }

    return arr;
}


An array of size n is created.

Auxiliary SC = O(n)

Example 3: Two-Dimensional Array — O(n²)
javascript
function createMatrix(n) {
    let matrix = [];

    for (let i = 0; i < n; i++) {
        matrix.push(new Array(n).fill(0));
    }

    return matrix;
}


The matrix contains n × n elements.

Auxiliary SC = O(n²)

Example 4: Recursion — O(n)
javascript
function count(n) {
    if (n === 0) {
        return;
    }

    count(n - 1);
}


Each recursive call occupies stack memory.

Maximum recursion depth = n + 1.

Auxiliary SC = O(n)

Example 5: Binary Search Recursion — O(log n)
javascript
function binarySearch(arr, low, high, target) {
    if (low > high) return -1;

    let mid = Math.floor((low + high) / 2);

    if (arr[mid] === target) return mid;

    if (arr[mid] > target) {
        return binarySearch(arr, low, mid - 1, target);
    }

    return binarySearch(arr, mid + 1, high, target);
}


Each call reduces the search space by half.

Maximum recursion depth = O(log n).

Auxiliary SC = O(log n)

9. Common Space Complexities
Complexity	Meaning	Example
O(1)	Constant space	A few variables
O(log n)	Logarithmic space	Recursive Binary Search
O(n)	Linear space	Extra array
O(n²)	Quadratic space	n × n matrix
PART 3: TIME AND SPACE TOGETHER
10. TC and SC Comparison
Parameter	Time Complexity	Space Complexity
Measures	Operations/growth in time	Memory usage
Focus	Execution efficiency	Memory efficiency
Example	Number of loop iterations	Extra array size
Common notation	Big O	Big O
Example
javascript
function example(n) {
    let arr = [];

    for (let i = 0; i < n; i++) {
        arr.push(i);
    }

    return arr;
}


Time Complexity:

Loop executes n times.
TC = O(n)

Space Complexity:

Array stores n elements.
Auxiliary SC = O(n)

Final Answer:

TC = O(n)

SC = O(n)

11. In-Place Algorithms

An in-place algorithm uses very little additional memory, usually O(1) auxiliary space.

Example:

javascript
function reverse(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        let temp = arr[left];

        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}

Time Complexity = O(n)
Auxiliary Space = O(1)

The input array is modified directly without creating another array.

12. Recursion and Space Complexity

Every recursive function uses the call stack.

Consider:

javascript
function factorial(n) {
    if (n === 0) return 1;

    return n * factorial(n - 1);
}


For factorial(4):

text
factorial(4)
    factorial(3)
        factorial(2)
            factorial(1)
                factorial(0)


Maximum call stack depth = n + 1.

TC = O(n)
Auxiliary SC = O(n)

Important: Recursive calls consume stack memory even if you do not create an array or object.

PART 4: QUICK REVISION
13. Important Rules
Time Complexity
Single loop running n times → O(n).
Two separate loops running n times → O(n).
Two nested loops running n times → O(n²).
Three nested loops running n times → O(n³).
Input divided by 2 each iteration → O(log n).
Input multiplied by 2 each iteration → O(log n).
Consecutive operations → Add complexities.
Nested operations → Multiply complexities.
Ignore constants.
Ignore lower-order terms.
Space Complexity
Fixed number of variables → O(1).
Extra array of size n → O(n).
Matrix of n × n → O(n²).
Recursive calls with depth n → O(n).
Recursive calls with depth log n → O(log n).
In-place algorithms often use O(1) auxiliary space.
14. Practice Questions

Try calculating both TC and SC.

Q1
javascript
for (let i = 0; i < n; i++) {
    console.log(i);
}

Q2
javascript
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        console.log(i, j);
    }
}

Q3
javascript
let arr = new Array(n).fill(0);

Q4
javascript
let i = 1;

while (i < n) {
    i *= 2;
}

Q5
javascript
function print(n) {
    if (n === 0) return;

    print(n - 1);
}

Q6
javascript
for (let i = 0; i < n; i++) {
    console.log(i);
}

for (let j = 0; j < n * n; j++) {
    console.log(j);
}

Q7
javascript
function example(n) {
    let arr = [];

    for (let i = 0; i < n; i++) {
        arr.push(i);
    }

    return arr;
}

15. Final Cheat Sheet
Code Pattern	TC	Auxiliary SC
Fixed operations	O(1)	O(1)
Single loop	O(n)	O(1)
Two nested loops	O(n²)	O(1)
Three nested loops	O(n³)	O(1)
Loop with i *= 2	O(log n)	O(1)
Extra array of n elements	O(n) if filled	O(n)
Recursive linear calls	O(n)	O(n)
Recursive Binary Search	O(log n)	O(log n)
Merge Sort	O(n log n)	O(n)

Golden Rule:

TC tells us how the number of operations grows.
SC tells us how the extra memory usage grows.
Always analyze both when solving DSA problems.

Practice regularly. The best way to master TC and SC is to analyze code yourself rather than memorize complexity tables.