import ephem
from datetime import datetime

dt_now = datetime.now()

def planet_const(planet_name):
    planet_name = planet_name.lower()

    if planet_name == 'mercury':
        e_planet = ephem.Mercury(datetime.now())
        const = ephem.constellation(e_planet) 
    elif planet_name =='venus' :
        e_planet = ephem.Venus(datetime.now())
        const = ephem.constellation(e_planet) 
    elif planet_name == 'mars':
        e_planet = ephem.Mars(datetime.now())
        const = ephem.constellation(e_planet) 
    elif planet_name == 'jupiter':
        e_planet = ephem.Jupiter(datetime.now())
        const = ephem.constellation(e_planet) 
    elif planet_name == 'saturn':
        e_planet = ephem.Saturn(datetime.now())
        const = ephem.constellation(e_planet)
    elif planet_name == 'uranus':
        e_planet = ephem.Uranus(datetime.now())
        const = ephem.constellation(e_planet) 
    elif planet_name == 'neptune':
        e_planet = ephem.Neptune(datetime.now())
        const = ephem.constellation(e_planet) 
    else:
        print('Название некорректно!')  
    return const
    
    

if __name__ == "__main__":
    planet_const()

