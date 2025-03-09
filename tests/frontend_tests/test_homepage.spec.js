describe('Homepage', () => {
  it('loads the homepage and displays a welcome message', () => {
    cy.visit('http://localhost:3000');
    cy.contains('Welcome to UCODTS');
  });
});
