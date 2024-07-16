import requests

def get_states():
    """get all states"""
    response = requests.get("http://127.0.0.1:5000/states")
    states = response.json()
    print(states)


def filter_states_byName():
    """get all states by name in ascending order"""
    response = requests.get("http://127.0.0.1:5000/states/filter/name_asc")
    filtered_states = response.json()
    print(filtered_states)


def create_state():
    """create a new state"""
    state= {"name": "embu", "abbreviation": "KR", "capital": "Kutus", "population": 10000000, "year_admitted": 2021}
    headers =  {"Content-Type":"application/json"}
    response = requests.post("http://127.0.0.1:5000/state/register", json=state, headers=headers)
    print(response.text)
def filter_states_byName_starting_with_A():
    """get all states by name starting with 'A' in ascending order"""
    response = requests.get("http://127.0.0.1:5000/states/filter")
    filtered_states = response.json()
    print(filtered_states)  
def update_state_population_byID():
    """update population of a state by ID"""
    data ={"id":2,"population":3000000}
    headers =  {"Content-Type":"application/json"}
    response = requests.patch(f"http://127.0.0.1:5000/states/update/population", json=data, headers=headers)
    print(response.text) 
def delete_state_byID():
    """delete a state by ID"""
    data ={"id":20}
    headers =  {"Content-Type":"application/json"}
    response = requests.delete(f"http://127.0.0.1:5000/states/delete", json=data, headers=headers)
    print(response.text)
def get_populous_state():
    """get the state with the highest population"""
    response = requests.get("http://127.0.0.1:5000/states/populous")
    populous_state = response.json()
    print(populous_state)  
def state_capital():    
    """get the capital of a specific state"""
    response = requests.get("http://127.0.0.1:5000/states/capital")
    capitals = response.json()
    print(capitals)
def average_state_population():
    """get the average population of all states"""
    response = requests.get("http://127.0.0.1:5000/states/average_population")
    average_population = response.json()
    print(average_population)    
def range_of_population_btw_1M_and_5M():
    """get the range of population of all states between 1 million and 5 million"""
    response = requests.get("http://127.0.0.1:5000/states/range_population")
    population_range = response.json()
    print(population_range)   
def states_admitedBtw1750and1850():
    """get all states that were admitted between 1750 and 1850"""
    response = requests.get("http://127.0.0.1:5000/states/admitedBtw1750and1850")
    filtered_states = response.json()
    print(filtered_states)
def join_state_capital():
    """get the state and capital of all states"""
    response = requests.get("http://127.0.0.1:5000/states/join_state_capital")
    states_with_capitals = response.json()
    print(states_with_capitals)
get_states()   
