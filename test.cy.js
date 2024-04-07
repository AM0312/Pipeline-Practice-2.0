/// <reference types="cypress" />

describe("template spec", () => {
  it("passes", () => {
    cy.visit("https://am0312.github.io/Pipeline-Practice-2.0/");
    cy.get("h1").should("contain.text", "Magic");
  });
});
