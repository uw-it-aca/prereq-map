describe('Search Page', function() {

  it('Displays accept modal', function() {
    cy.visit('/');
    cy.wait(500);
    // take a snapshot
    cy.document().matchImageSnapshot();
  })

  it('Displays Search page when user accepts', function() {

    // click the accept
    cy.get('.btn.btn-primary.float-right').click();

    // Course radio button should be selected
    cy.get('[type="radio"]').first().should("be.checked");
    // check for other stuff

    // make sure Discover shows Bothell, Seattle, Tacoma

    cy.wait(100);

    // take a snapshot of default state
    cy.document().matchImageSnapshot();
  })
})
