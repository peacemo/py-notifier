class Notifier:
    def __init__(self) -> None:
        pass

    def push(self, title:str="TITLE", content:str="Hello Toast. "):
        import platform  # check which OS is using. 

        platform_os = platform.system()  # OS name
        platform_rls = platform.release()  # OS release version

        # # For Windows
        # if platform_os == "Windows" and int(platform_rls) >= 10:
        #     print(F"Super push, {title}, {content}")
        #     try:
        #         self._push2win(title=title, content=content)
        #         return True
        #     except:
        #         return False
        # else:
        #     print(F"Super push, {title}, {content}")
        #     return True

        pass

    # def _push2win(self, title:str="TITLE", content:str="Hello Toast. "):
    #     from win10toast_click import ToastNotifier 
    #     import warnings
    #     warnings.filterwarnings("ignore")

    #     toaster = ToastNotifier()

    #     toaster.show_toast(
    #         title, # title
    #         content, # message 
    #         duration=None, # for how many seconds toast should be visible; None = leave notification in Notification Center
    #         threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    #         )
        
    #     return True
    #     pass

class BarkNotifier(Notifier):
    """
    BarkNotifier(server: str, token: str)

    Class representing a Bark notifier used to send push notifications to the Bark server.

    Parameters:
    - `server` (str): The address of the Bark server.
    - `token` (str): The token used for authentication.

    Methods:
    - `push(title: str = "Bark", content: str = "Hello Bark.")`: Sends a push notification to the Bark server.

    Notes:
    - If the `server` parameter does not end with a slash `/`, it will be automatically appended during initialization.
    - The `push` method sends a push notification to the Bark server and returns a boolean value indicating whether the push was successful.
    - When the push is successful, "Push Successed." will be printed; otherwise, "Push failed, something went wrong with the SERVER." will be printed.
    - If an exception or error occurs during the push request, "Bad URL: {url}" will be printed.
    """

    def __init__(self, server:str, token:str) -> None:
        super().__init__()

        if server[-1] != "/":
            server += "/"
        self.server = server
        self.token = token

    def push(self, title:str="Bark", content:str="Hello Bark. "):
        """
        push(title: str = "Bark", content: str = "Hello Bark.") -> bool

        Sends a push notification to the Bark server.

        Parameters:
        - `title` (str): The title of the push notification. Default is "Bark".
        - `content` (str): The content of the push notification. Default is "Hello Bark.".

        Returns:
        - `bool`: True if the push notification is successful (status code 200), False otherwise.

        Note:
        - The push notification is sent using the `requests` library and a GET request to the specified URL.
        - If the push is successful (status code 200), "Push Successed." is printed; otherwise, "Push failed, something went wrong with the SERVER." is printed.
        - If an exception or error occurs during the push request, "Bad URL: {url}" is printed.
        """

        super().push(title=title, content=content)

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
