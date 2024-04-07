function printStarPattern(rows) {
  let pattern = "";

  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= i; j++) {
      pattern += "* ";
    }
    pattern += "\n";
  }

  console.log(pattern);
}

// Change the number of rows as needed
const numRows = 50;
printStarPattern(numRows);
