describe('Demo Test', function() {
  it('t1', function() {
    cy.visit('')
    cy.title().should('eq', 'Prereq Map - University of Washington')
    cy.wait(500)
    cy.document().toMatchImageSnapshot()

    cy.get('.btn.btn-primary.float-right').click()
    cy.wait(100)
    cy.document().toMatchImageSnapshot()
  })
})