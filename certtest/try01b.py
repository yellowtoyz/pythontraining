#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests
import pandas

API = "https://ssd-api.jpl.nasa.gov/fireball.api"

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}?limit=20")

#    fireballs = resp.json().get("data")
    fireballs = resp.json()
    print(fireballs.get("data"))

#    print(fireballs)

#    for ball in fireballs.get("data"):
#        print(ball.get("date"), ball.get("energy"))




#    print(fireballs.get("date"))
#    print(fireballs.get("energy"))

#    with open("jplFireballs.csv", "w") as jplfile:
#        for fireball in fireballs:
#            print(fireball, file=jplfile)



if __name__ == "__main__":
    main()
