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

install dep first:
```bash
pip3 install selenium
pip3 install webdriver-manager
```

usage:
```bash
python3 ./auto_reset_pwd.py
```