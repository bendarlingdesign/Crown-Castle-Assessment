### Project: Crown Castle Checkers UI and Card Game API tests

### Prereqs

I used VSCode, python, selenium, and specifically the pytest library.

I needed to install Chrome WebDriver, the "webdriver_manager' library will help automatically download and manage the Chrome WebDriver for the user. 
This is a more convenient and future-proof way to handle WebDriver paths and versions. Make sure you have the webdriver_manager library installed by running (pip install webdriver-manager) if you haven't already.

I had to use Geckdriver (Firefox) on my new pc as chromedriver was problematic.

# Clone the repository
git clone https://github.com/bendarlingdesign/Crown-Castle-Assessment.git
cd your-project

# Example for installing Python packages using pip:
pip install -r requirements.txt

###Example to run a test: 
python -m pytest tests...
or
pytest my_tests.py
or
python .\tests...
