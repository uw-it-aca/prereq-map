describe('Search Page', function() {

  it('Displays accept modal', function() {
    cy.visit('/');

    // eslint-disable-next-line cypress/no-unnecessary-waiting
    cy.wait(500);

    // take a snapshot
    cy.document().matchImageSnapshot();
  });

  it('Displays Search page when user accepts', function() {

    // click the accept
    cy.get('.btn.btn-primary.float-right').click();

    // Course radio button should be selected
    cy.get('[type="radio"]').first().should("be.checked");
    // TODO: check for other stuff
    // TODO: make sure Discover shows Bothell, Seattle, Tacoma

    // eslint-disable-next-line cypress/no-unnecessary-waiting
    cy.wait(100);

    // take a snapshot of default state
    cy.document().matchImageSnapshot();
  });

});
