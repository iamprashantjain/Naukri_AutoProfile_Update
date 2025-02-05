from playwright.sync_api import sync_playwright
import time

def test_naukri_login():
    with sync_playwright() as p:
        # Launch browser in headed mode
        browser = p.chromium.launch(headless=False)

        # Create a new browser context
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        # Open Naukri login page
        page.goto("https://www.naukri.com/")

        # Click on the "Login" button on the homepage
        page.click("#login_Layer")

        # Wait for login form to load
        page.wait_for_selector("form[name='login-form']")

        # Fill in login details
        page.fill("input[placeholder='Enter your active Email ID / Username']", "your_email")
        page.fill("input[placeholder='Enter your password']", "your_password")

        # Click the login button
        page.click("button.loginButton")

        # Wait for profile page or some confirmation element after login
        page.wait_for_selector(".view-profile-wrapper a")

        # Click on the "View Profile" link
        page.click(".view-profile-wrapper a")
        
        
        # Wait for the Resume Headline section to load
        page.wait_for_selector(".widgetHead .edit.icon")

        # Click the "Edit" button in the Resume Headline section
        page.click(".widgetHead .edit.icon")
                
        # Wait for the textarea to become editable (focused)
        page.wait_for_selector("#resumeHeadlineTxt")

        # Fill a dot (".") in the textarea
        page.fill("#resumeHeadlineTxt", "whatever you want to update everyday.. !!")            #write text you want to update in resume headline

        
        # Wait for the "Save" button to be visible using XPath
        page.wait_for_selector('xpath=/html/body/div[6]/div[8]/div[2]/form/div[3]/div/button')

        # Click the "Save" button using XPath
        page.click('xpath=/html/body/div[6]/div[8]/div[2]/form/div[3]/div/button')


        # Pause to keep the browser open
        page.pause()

# Run the function
test_naukri_login()