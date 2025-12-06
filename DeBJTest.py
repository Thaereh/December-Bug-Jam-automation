# tests/test_landing_page.py
from DeBJMain import EC

from DeBJMain import MainPage

def test_landing_page_title_and_buttons(driver, base_url):
    """
    1.1 Landing page:
    - 'RecommenDead' title is visible
    - Left human icon is present
    - Right moon button is present
    """
    page = MainPage(driver)

    # Step 1: Open the landing page
    page.open(base_url)

    # Step 2: Check title is visible
    title = page.wait.until(EC.visibility_of_element_located(MainPage.TITLE)
    )
    assert title.is_displayed(), "RecommenDead title should be visible on landing page."

    # Step 3: Check human icon (left button) exists
    human_icon = driver.find_element(*MainPage.HUMAN_ICON)
    assert human_icon.is_displayed(), "Human icon button should be visible."

    # Step 4: Check moon button (right) exists
    moon_button = driver.find_element(*MainPage.BTN_MOON)
    assert moon_button.is_displayed(), "Moon button should be visible."
def test_human_icon_opens_login_and_signup(driver, base_url):
    """
    1.1 Landing page:
    - Clicking human icon opens a menu with 'Login' and 'Sign Up' options.
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Click on human icon
    page.click_human_icon()

    # Step 2: Wait for Login and Sign Up buttons to become visible
    login, signup = page.get_login_and_signup()

    # Step 3: Assert both buttons are displayed
    assert login.is_displayed(), "Login option should appear after clicking human icon."
    assert signup.is_displayed(), "Sign Up option should appear after clicking human icon."
def test_human_icon(driver, base_url):
    """
    1.1 Landing page:
    - Clicking human icon opens a menu with 'Login' and 'Sign Up' options.
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Click on human icon
    page.click_human_icon()

    # Step 2: Wait for Login and Sign Up buttons to become visible
    login, signup = page.get_login_and_signup()

    # Step 3: Assert both buttons are displayed
    assert login.is_displayed(), "Login option should appear after clicking human icon."
    assert signup.is_displayed(), "Sign Up option should appear after clicking human icon."
def test_valid_search_displays_one_poster(driver, base_url):
    """
    1.2 & 2.2:
    - Search accepts valid input (2–15 chars, letters + spaces)
    - When searching, exactly one film poster is displayed.
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Enter valid search term (length between 2 and 15)
    term = "ghost house"  # multi-word, valid length
    page.set_search_text(term)

    # Step 2: Click '+' to submit search
    page.click_plus()

    # Step 3: Check that exactly one poster is displayed
    assert page.posters_exist(), "Exactly one film poster should be displayed for a valid search term."
def test_no_results_shows_search_for_something_else_message(driver, base_url):
    """
    2.2 Search Results:
    - If there is no matching film, show 'Please search for something else'
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Enter a term that should NOT match any film
    page.set_search_text("zzzzzzzzzz")  # nonsense input

    # Step 2: Submit search
    page.click_plus()

    # Step 3: Get the no-results message text
    message = page.get_no_results_message()

    # Step 4: Assert that the message matches the requirement
    expected = "Please search for something else"
    assert message == expected, f"Expected message '{expected}', but got '{message}'."
def test_query_appears_above_input_after_search(driver, base_url):
    """
    2.3 Displaying Search Query:
    - After clicking '+', search query should appear above the search input field.
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Enter a valid search term
    term = "vampire"
    page.set_search_text(term)

    # Step 2: Click '+' to submit
    page.click_plus()

    # Step 3: Get all query tags above the input
    tags = page.get_query_tags()
    assert len(tags) >= 1, "At least one query tag should appear above the search field after a search."

    # Step 4: The last tag should match the latest search term
    last_tag_text = tags[-1].text.strip().lower()
    assert last_tag_text == term.lower(), (
        f"Expected last query tag to be '{term}', but found '{last_tag_text}'."
    )
def test_max_three_queries_shows_warning(driver, base_url):
    """
    2.3 Displaying Search Query:
    - Only up to 3 queries allowed.
    - 4th query should trigger a warning message.
    """
    page = MainPage(driver)
    page.open(base_url)

    # Step 1: Add three valid queries
    terms = ["ghost", "vampire", "zombie"]
    for t in terms:
        page.set_search_text(t)
        page.click_plus()

    # Step 2: Confirm that 3 query tags now exist
    tags = page.get_query_tags()
    assert len(tags) == 3, f"Expected 3 query tags, but found {len(tags)}."

    # Step 3: Try to add a 4th query
    page.set_search_text("witch")
    page.click_plus()

    # Step 4: Get the max-query message
    message = page.get_max_query_message()
    expected = "Maximum three search queries. Please remove one query."
    assert message == expected, f"Expected '{expected}', but got '{message}'."
def test_valid_single_word_search_shows_poster(driver, base_url):
    """
    Requirement: Search input accepts 2–15 characters (letters + spaces).
    A valid search should display exactly ONE film poster.
    """
    page = MainPage(driver)
    page.open(base_url)

    page.enter_search_text("ghost")
    page.submit_search()

    posters = page.get_posters()
    assert len(posters) == 1, "Expected one poster for valid search input."
def test_multi_word_search_is_accepted(driver, base_url):
    """
    Requirement: Search input should accept multiple words.
    """
    page = MainPage(driver)
    page.open(base_url)

    term = "ghost house"
    page.enter_search_text(term)
    page.submit_search()

    posters = page.get_posters()
    assert len(posters) == 1, "Expected poster for valid multi-word search."
def test_search_too_short_shows_error(driver, base_url):
    """
    Requirement: Search must allow only 2–15 characters.
    Input shorter than 2 should NOT trigger poster search.
    """
    page = MainPage(driver)
    page.open(base_url)

    page.enter_search_text("a")  # only 1 character
    page.submit_search()

    posters = page.get_posters()
    assert len(posters) == 0, "No posters should be shown for input shorter than 2 characters."
def test_search_too_long_fails_validation(driver, base_url):
    """
    Requirement: Max search length = 15.
    Longer inputs should not produce a poster.
    """
    page = MainPage(driver)
    page.open(base_url)

    long_text = "supernatural ghost"  # > 15 characters
    page.enter_search_text(long_text)
    page.submit_search()

    posters = page.get_posters()
    assert len(posters) == 0, "No posters should appear for >15 character input."
def test_search_rejects_invalid_characters(driver, base_url):
    """
    Requirement: Only Latin letters + spaces allowed.
    """
    page = MainPage(driver)
    page.open(base_url)

    page.enter_search_text("gh0st!")  # contains numbers + symbol
    page.submit_search()

    posters = page.get_posters()
    assert len(posters) == 0, "No result should be shown for invalid characters."
def test_no_results_message_appears(driver, base_url):
    """
    Requirement: If no matching film found, show message:
    'Please search for something else'
    """
    page = MainPage(driver)
    page.open(base_url)

    page.enter_search_text("xxxxxxx")
    page.submit_search()

    msg = page.get_no_results_message()
    assert msg == "Please search for something else", \
        f"Expected message but got: {msg}"
def test_query_tag_displays_above_input(driver, base_url):
    """
    Requirement: After clicking '+', query appears above the search input.
    """
    page = MainPage(driver)
    page.open(base_url)

    page.enter_search_text("vampire")
    page.submit_search()

    tags = page.get_query_tags()
    assert len(tags) >= 1, "Expected query tag to appear."
    assert "vampire" in tags[-1].text.lower()

def test_multi_query(driver, base_url):
    """
    Requirement: Posters must contain ALL terms when multiple queries exist.
    """
    page = MainPage(driver)
    page.open(base_url)

    queries = ["ghost", "night","hill","dance"]
    for q in queries:
        page.enter_search_text(q)
        page.submit_search()

    posters = page.get_poster_titles()
    assert all("ghost" in title and "night" in title for title in posters), \
        "Poster titles do not match ALL required terms."
def test_max_three_queries_warning(driver, base_url):
    """
    Requirement: When 3 queries exist, adding a 4th shows:
    'Maximum three search queries. Please remove one query.'
    """
    page = MainPage(driver)
    page.open(base_url)

    valid_terms = ["ghost", "zombie", "witch"]

    for term in valid_terms:
        page.enter_search_text(term)
        page.submit_search()

    # sanity check
    assert len(page.get_query_tags()) == 3

    # add fourth
    page.enter_search_text("vampire")
    page.submit_search()

    msg = page.get_max_query_message()
    assert msg == "Maximum three search queries. Please remove one query."

