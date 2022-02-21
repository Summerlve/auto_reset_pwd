# auto_reset_pwd
auto reset stu's pwd of suzhou snd edu system

create a file <account.json> in project folder and type in:
```javascript
{
    "username": "",
    "password": ""
}
```
fill in your account information into username and password field for website auth.

install python3 dep first:
```bash
pip3 install selenium
pip3 install webdriver-manager
pip3 install pytesseract
```

install tesseract, google ocr lib
```text
# MacOSX
brew install tesseract
# other os
# do it yourself
```

usage:
```bash
python3 ./auto_reset_pwd.py
```