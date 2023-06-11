import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):

    #clear the screen above
    clear()
    put_html("<p align=""left""><h2><img src=""https://\
             media.geeksforgeeks.org/wp-content/uploads/\
             20210720224119/MessagingHappyicon.png"" width=""7%"">  \
             Fun Fact Generator</h2></p>")
    
    #url to fetch the data from
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    #use GET request
    response = requests.request("GET", url)

    #load the request in json file
    data = json.loads(response.text)

    #passing 'text' from the list
    useless_fact = data['text']

    #put the facts in the blue colour and add click me button
    style(put_text(useless_fact), 'color:blue; font-size:30px')
    put_buttons(
        [dict(label='Click me', value='outline-success',
              color='outline-success')], onclick=get_fun_fact)
    
#driver function
if __name__=='__main__':

    #put a heading "Fun Fact Generator"

    put_html("<p align=""left""><h2><img src=""https://media.\
             geeksforgeeks.org/wp-content/uploads/20210720224119\
             /MessagingHappyicon.png"" width=""7%"">  \
             Fun Fact Generator</h2></p>")
    
    #prolonging session
    #put a click me button
    put_buttons(
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact)  
hold()
    