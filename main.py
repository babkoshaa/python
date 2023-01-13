from selene.support.shared import browser
from selene import have

browser.open('https://www.google.com/')
browser.element('[name=q]').type('selene').press_enter()
browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
browser.open('https://github.com/yashaka/selene')