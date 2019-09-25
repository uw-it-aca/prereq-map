describe('search page', function() {

  context('accept modal', function() {

    // TODO: lower fidelity tests should match the workflow supported by the MVP
    // (e.g. test the button functionality)

    it('should display on initial launch', function() {
      cy.visit('/');
      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(500);

      // TODO: check for the presence of modal code (modal #id?)

      // TODO: visual regression should snapshot the high-fidelity UI as it relates to the workflow
      // (e.g. test what the button should look like)

      // take a snapshot
      cy.document().matchImageSnapshot('01-accept-modal-displayed');

    });

    it('should dismiss when user accepts', function() {
      // click the accept
      cy.get('.btn.btn-primary.float-right').click();
      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(100);
    });

  });

  context('default interface', function() {

    it('should display correctly', function() {

      // course radio button should be selected
      cy.get('[type="radio"]').first().should("be.checked");

      // curric radio unselected
      // bothell, seattle, and tacoma cards are on page
      // check for other stuff

      // take a snapshot
      cy.document().matchImageSnapshot('02-default-interface');

    });

  });

  context('course search', function() {

    it('should display autocomplete', function() {

      // type 'math'
      cy.get('[type="text"]').type('math');

      // eslint-disable-next-line cypress/no-unnecessary-waiting
      cy.wait(1000);

      // show the dropdown autocomplete menu

      // take snapshot
      cy.document().matchImageSnapshot('04-course-autocomplete-math');

    });

    it('should perform action', function() {
      // select a course from autocomplete
      // click "search" button
      // user taken to course page
    });

  });

  context('curric search', function() {

    it('should display autocomplete', function() {
    });

    it('should perform action', function() {

    });

  });

});
