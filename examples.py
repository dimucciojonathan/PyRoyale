import pyroyale as rl

mykey = open('/Users/a1425/Documents/mykey.txt','r').read()

# Initialize Class
pyRoyale = rl.PyRoyale(mykey)

# Call desired method
pyRoyale.get_player_info('YYRVLLUV')  

# Retrieve class variable, which is in JSON format
json_info = pyRoyale.player_info
print(json_info)
