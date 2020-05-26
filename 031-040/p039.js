/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
*/


let solutions = {};

// Test each perimeter
for (let p = 0; p <= 1000; p++) {
    solutions[`${p}`] = 0;
    for (let c = 1; c <= p - 2; c++) {
        for (let a = 1; a < c; a++) {
            let b = Math.sqrt(c * c - a * a);
            if (a + b + c === p) {
                solutions[`${p}`]++;
                break;
            }  
        }
    }
}

// Find the most solutions in a perimeter
const ans = (Object.values(solutions)).reduce(function(a, b) {
    return Math.max(a, b);
});

// Figure out which perimeter that was
console.log(Object.keys(solutions).find(key => solutions[key] === ans));
