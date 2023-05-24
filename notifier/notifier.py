class Notifier:
    def __init__(self) -> None:
        pass

class BarkNotifier:
    def __init__(self, server:str, token:str) -> None:
        if server[-1] != "/":
            server += "/"
        self.server = server
        self.token = token

    def push(self, title:str="Bark", content:str="Hello Bark. "):
        import requests

        url = self.server + self.token + "/" + title + "/" + content
        
        response = None
        try:
            response = requests.get(url=url)
            print("Push Successed. ") if response.status_code == 200 else print("Push failed, something went wrong with the SERVER. ")
            return True if response.status_code == 200 else False
        except:
            print(f"Bad URL: {url}")
            return False
