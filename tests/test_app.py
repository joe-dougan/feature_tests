from playwright.sync_api import Page, expect

def test_example(page, test_web_address):

    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}/")

    # We look at the h1
    heading = page.locator("h1")

    # We assert that it has the the correct content
    expect(heading).to_have_text("User Management")

def test_user_create(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.fill('input[name="username"]','test_user')
    page.fill('input[name="email"]','test@user.com')
    page.fill('input[name="favourite_colour"]','blue')
    page.click('text = Submit')
    listitem = page.locator('li')
    expect(listitem).to_have_text(['John','Jane','Alice','Test_user'])

def test_blank_field(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.fill('input[name="username"]','test_user')
    page.fill('input[name="email"]','test@user.com')
    page.fill('input[name="favourite_colour"]','')
    page.click('text = Submit')
    listitem = page.locator('li')
    expect(listitem).to_have_text(['John','Jane','Alice'])

def test_max_users(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    for i in range(8):
        page.fill('input[name="username"]','test_user')
        page.fill('input[name="email"]','test@user.com')
        page.fill('input[name="favourite_colour"]','blue')
        page.click('text = Submit')
    listitem = page.locator('li')
    expect(listitem).to_have_text(['John','Jane','Alice','Test_user','Test_user','Test_user','Test_user','Test_user','Test_user','Test_user'])

def test_link_to_user_details(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.click('text = John')
    h1tag = page.locator('h1')
    expect(h1tag).to_have_text("John's details")
    h2tag = page.locator('h2')
    expect(h2tag).to_have_text(['Email Address', 'Favourite Colour'])
    divtag = page.locator('div')
    expect(divtag).to_have_text(['john@example.com','Pink'])

def test_capitlisation_works(page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    page.fill('input[name="username"]','test_user')
    page.fill('input[name="email"]','test@user.com')
    page.fill('input[name="favourite_colour"]','blue')
    page.click('text = Submit')
    listitem = page.locator('li')
    expect(listitem).to_have_text(['John','Jane','Alice','Test_user'])
    page.click('text = Test_user')
    h1tag = page.locator('h1')
    expect(h1tag).to_have_text("Test_user's details")
    h2tag = page.locator('h2')
    expect(h2tag).to_have_text(['Email Address', 'Favourite Colour'])
    divtag = page.locator('div')
    expect(divtag).to_have_text(['test@user.com','Blue'])