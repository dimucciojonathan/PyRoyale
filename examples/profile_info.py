import pyroyale as rl

""" Profile info example"""

def get_player_info(player_tag):
    mykey = open('/Users/a1425/Documents/mykey.txt','r').read()

    # Initialize Class
    pyRoyale = rl.PyRoyale(mykey)

    # Call desired method
    pyRoyale.get_player_info(player_tag)  

    # Retrieve class variable, which is in JSON format
    return pyRoyale.player_info

# Test
# get_player_info('YYRVLLUV')