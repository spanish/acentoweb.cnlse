# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s acentoweb.cnlse -t test_cnlse_researcher.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src acentoweb.cnlse.testing.ACENTOWEB_CNLSE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/acentoweb/cnlse/tests/robot/test_cnlse_researcher.robot
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

Scenario: As a site administrator I can add a CNLSE Researcher
  Given a logged-in site administrator
    and an add CNLSE Researcher form
   When I type 'My CNLSE Researcher' into the title field
    and I submit the form
   Then a CNLSE Researcher with the title 'My CNLSE Researcher' has been created

Scenario: As a site administrator I can view a CNLSE Researcher
  Given a logged-in site administrator
    and a CNLSE Researcher 'My CNLSE Researcher'
   When I go to the CNLSE Researcher view
   Then I can see the CNLSE Researcher title 'My CNLSE Researcher'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add CNLSE Researcher form
  Go To  ${PLONE_URL}/++add++CNLSE Researcher

a CNLSE Researcher 'My CNLSE Researcher'
  Create content  type=CNLSE Researcher  id=my-cnlse_researcher  title=My CNLSE Researcher

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the CNLSE Researcher view
  Go To  ${PLONE_URL}/my-cnlse_researcher
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a CNLSE Researcher with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the CNLSE Researcher title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
