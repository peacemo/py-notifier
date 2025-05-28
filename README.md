# Py-Notifier

To push text to your iPhone via Bark Server or push something to your Webhook!

- TODOS

- [X] Bark
- [ ] Webhook
- [ ] Local push - system notification, or just a simple sound play.

## Installation

run:

```bash
pip install git+https://github.com/peacemo/py-notifier.git
```

## Usage

Here is an Example of how to use **Notifier** to push via Bark Server:

```python
from notifier import BarkNotifier  # get BarkNotifier 

server = "http://xxx.xxx:xxx"  # put your server address here! 
token = "xxxxxxxxxxxxxxxxxxxxxx"  # and put your token here! 

bark = BarkNotifier(server=server, token=token)  # assign a BarkNotifier, your server and token MUST be passed

title = "Title" 
content = "Content" 

bark.push(title=title, content=content) 
```

Now, if it successed, a message should have been pushed to your iPhone, and a console message would appear: Push successed!

If a message shows "Push failed, something went wrong with the SERVER. ". It should be the problem with your server.

if a message shows "Bad URL: http://xxx.xxx/xxxxx/xxx/xxx". Please check your server, it may be a typo!
