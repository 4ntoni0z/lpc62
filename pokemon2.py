import os
import requests
#JUAN ANTONIO SENA CASTILLO
#1973595
#script en python que consulta el api de pokemon 
#para listar los nombres de pokemon pero se le agrego 
#interaccion paraq ue listaras mas pokemons segun se aya redirigiendo 
#fecha 04-09-2023

def get_pokemons (url ="https://pokeapi.co/api/v2/pokemon-form/", offset=0):
    args = {'offset':offset} if offset else{}
    response = requests.get(url, params=args)
    
    
    if response.status_code==200:
        payload = response.json()
        results= payload.get("results",[])
        
        if results:
            for pokemon in results:
                name=pokemon["name"]
                print(name)
                
        next=input("Continuar listando? [Y/N]").lower
        if next == 'y':
            get_pokemons(offset=offset+20)


if __name__ == "__main__":
    url= "https://pokeapi.co/api/v2/pokemon-form/"
    get_pokemons()
    
    
