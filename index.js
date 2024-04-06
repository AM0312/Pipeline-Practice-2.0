document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".card");
  const revealBtn = document.getElementById("revealBtn");
  const resultDiv = document.getElementById("result");

  revealBtn.addEventListener("click", function () {
    const randomIndex = Math.floor(Math.random() * cards.length);
    const selectedCard = cards[randomIndex];
    resultDiv.textContent = `The magic card is: ${selectedCard.textContent}`;
  });
});
