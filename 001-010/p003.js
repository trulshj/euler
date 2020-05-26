// What is the largest prime factor of the number 600851475143 ?

let num = 600851475143;
let largest = 1;

const isPrime = (n) => {
    
    if (n <= 1) {
        return false;
    }

    if (n == 2) {
        return true;
    }

    const upperBound = Math.ceil(Math.sqrt(n));
    for (let i = 2; i <= upperBound; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true
}


for (let i = 0; i * i < num; i++) {
    if (isPrime(i)) {
        if (num % i === 0) {
            largest = largest < i ? i : largest;
        }
    }
}

console.log(largest);