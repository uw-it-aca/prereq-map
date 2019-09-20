describe('Search Page', function() {
  it('Displays accept modal', function() {
    cy.visit('');
    cy.title().should('eq', 'Prereq Map - University of Washington');
    cy.wait(500);
    cy.document().toMatchImageSnapshot();
  })
  it('Removes modal when user accepts', function() {
    cy.get('.btn.btn-primary.float-right').click();
    cy.wait(100);
    cy.document().toMatchImageSnapshot();
  })
})
