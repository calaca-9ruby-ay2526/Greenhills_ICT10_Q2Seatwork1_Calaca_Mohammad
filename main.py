from pyscript import document, display

# FUNCTION
def finding_nickname(e):
    # Variables
    document.getElementById('result').innerHTML = " "
    type = document.getElementById('country')
    #This will get the value assigned to the country on the dropdown menu
    nickname = type.value
    #This will display the nickname
    display(nickname,  target='result')

