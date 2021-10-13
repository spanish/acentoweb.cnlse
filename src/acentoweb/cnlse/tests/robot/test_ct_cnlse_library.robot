# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.cnlse -t test_cnlse_library.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.cnlse.testing.ACENTOWEB_CNLSE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/cnlse/tests/robot/test_cnlse_library.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a CNLSE Library
  Given a logged-in site administrator
    and an add CNLSE Library form
   When I type 'My CNLSE Library' into the title field
    and I submit the form
   Then a CNLSE Library with the title 'My CNLSE Library' has been created

Scenario: As a site administrator I can view a CNLSE Library
  Given a logged-in site administrator
    and a CNLSE Library 'My CNLSE Library'
   When I go to the CNLSE Library view
   Then I can see the CNLSE Library title 'My CNLSE Library'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add CNLSE Library form
  Go To  ${PLONE_URL}/++add++CNLSE Library

a CNLSE Library 'My CNLSE Library'
  Create content  type=CNLSE Library  id=my-cnlse_library  title=My CNLSE Library

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the CNLSE Library view
  Go To  ${PLONE_URL}/my-cnlse_library
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a CNLSE Library with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the CNLSE Library title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
