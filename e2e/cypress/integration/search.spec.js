describe('search page', function() {

  context('accept modal', function() {

    // TODO: lower fidelity tests should match the workflow supported by the MVP
    // (e.g. test the button functionality)

    it('should display on initial launch', function() {
      cy.visit('/');
      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(500);
      cy.get('#userAcceptance').should('exist');
      // take a snapshot
      cy.document().matchImageSnapshot();

    });

    it('should dismiss when user accepts', function() {
      // click the accept (got it) button
      cy.get('.modal-footer [type="button"]').click();
      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(100);
      // take a snapshot
      cy.document().matchImageSnapshot();
    });

  });

  context('default search', function() {

    it('should display correctly', function() {
      // course radio button should be selected
      cy.get('[type="radio"]').first().should("be.checked");
      cy.get('[placeholder="Enter a course code... (e.g MATH 124)"]').should('exist');
      // take a snapshot
      cy.document().matchImageSnapshot();
    });

  });

  context('course search', function() {

    it('should display autocomplete', function() {

      // type 'math'
      cy.get('[type="text"]').type('math');

      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(500);

      // show the dropdown autocomplete menu

      // take snapshot
      cy.document().matchImageSnapshot();

    });

    it('should perform search for MATH 100', function() {
      cy.get('[type="text"]').clear();
      cy.get('[type="text"]').type('MATH 100: Algebra');
      cy.document().matchImageSnapshot();
    });

    it('display course detail for MATH 100', function() {
      cy.get('[type="submit"]').click();
      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(1000);
      cy.document().matchImageSnapshot();
    });

  });

  context('curric search', function() {

    it('should display autocomplete', function() {
    });

    it('should perform action', function() {

    });

  });

});
