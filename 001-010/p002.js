// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

let total = 0;

// Set up for Fib seq
let a = 1, b = 1, temp;

while (b < 4e6) {
    temp = a;
    a += b;
    b = temp;

    if (b % 2 === 0) {
        total += b;
    }
}

console.log(total);