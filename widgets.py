import requests
URL = "http://cdn.getlocalmeasure.com/public/511b04e70cc0b52f7cd6db8c/widgets.json"

def load_widgets(): 
  widgets = requests.get(URL).json()
  
  for widget in widgets:
    print widget["description"]


if __name__ == '__main__':
  load_widgets()