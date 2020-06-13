# PyRoyale V1.0

PyRoyale is a light wrapper around the [official Clash Royale API](https://developer.clashroyale.com/#/)

This wrapper has a few use cases, and can easily be used for any or all listed!
1. Retrieve JSON information from the API
2. Convert Clash Royale JSON data to a more usable format (list or pandas dataframe)
3. Custom searches for tournaments, clans, players

PyRoyale is currently in V1.0, so only use case #1 has been implemented.
-----------------

## Installation steps..

The only package requirement is 'requests', which can be installed with

``pip install requests``

Next, download PyRoyale.py, and add the file to your directory. At the top of your working file, import it with

``import PyRoyale as rl``

## Using PyRoyale..

A quick implementation is to get information about your account. The JSON data includes many data points, such as level, wins, trophies, etc. The code is:

import pyroyale as rl

  ``mykey = open('/Users/a1425/Documents/mykey.txt','r').read()
  pyRoyale = rl.PyRoyale(mykey)
  pyRoyale.get_player_info('YYRVLLUV')
  json_info = pyRoyale.player_info
  print(json_info)``


