describe('Search Page', function() {

  it('should display accept modal', function() {
    cy.visit('/');
    // eslint-disable-next-line cypress/no-unnecessary-waiting
    cy.wait(500);

    // take a screenshot & snapshot
    cy.document().matchImageSnapshot('01-accept-modal-displayed');
  });

  it('should dismiss modal when user accepts', function() {

    // click the accept
    cy.get('.btn.btn-primary.float-right').click();

    // Course radio button should be selected
    cy.get('[type="radio"]').first().should("be.checked");
    // TODO: check for other stuff
    // TODO: make sure Discover shows Bothell, Seattle, Tacoma

    // eslint-disable-next-line cypress/no-unnecessary-waiting
    cy.wait(100);

    // take a screenshot & snapshot
    cy.document().matchImageSnapshot('02-accept-modal-dismissed');
  });

});
