from playwright.sync_api import Page, expect

def test_example(page, test_web_address):

    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}/")

    # We look at the h1
    heading = page.locator("h1")

    # We assert that it has the the correct content
    expect(heading).to_have_text("User Management")
