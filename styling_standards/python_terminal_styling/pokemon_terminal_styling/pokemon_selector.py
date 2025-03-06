"""
Pokemon selector module for terminal styling standards.

This module helps select appropriate Pokemon for function naming based on their characteristics.
It uses the pypokedex library to fetch Pokemon data from the PokeAPI.
"""

import pypokedex
from typing import Dict, List, Optional, Tuple

# Mapping of function types to recommended Pokemon and their characteristics
FUNCTION_TYPE_MAPPING = {
    "display": {"pokemon": "hitmonchan", "reason": "Known for precision and presentation style"},
    "error": {"pokemon": "primeape", "reason": "Reactive nature, good for alerting to problems"},
    "processing": {"pokemon": "machamp", "reason": "Multiple arms represent handling multiple operations"},
    "verification": {"pokemon": "hitmonlee", "reason": "High Jump Kick represents verification leaps"},
    "setup": {"pokemon": "machoke", "reason": "Strength represents setting up environments"},
    "configuration": {"pokemon": "machamp", "reason": "Dynamic Punch represents configuring systems"},
    "parsing": {"pokemon": "alakazam", "reason": "Psychic abilities represent parsing and understanding"},
    "formatting": {"pokemon": "kadabra", "reason": "Transformation abilities represent formatting data"},
    "progress": {"pokemon": "rapidash", "reason": "Speed represents progress tracking"},
    "file": {"pokemon": "snorlax", "reason": "Storage capacity represents file handling"},
    "network": {"pokemon": "porygon", "reason": "Digital nature represents network operations"},
    "validation": {"pokemon": "mewtwo", "reason": "Analytical abilities represent validation"},
    "logging": {"pokemon": "slowbro", "reason": "Methodical nature represents logging"}
}

# Cache for Pokemon data to avoid repeated API calls
pokemon_cache = {}

def get_pokemon_data(name: str) -> Dict:
    """
    Get Pokemon data from the PokeAPI using pypokedex.
    
    Args:
        name: The name of the Pokemon
        
    Returns:
        A dictionary with Pokemon data
    """
    if name in pokemon_cache:
        return pokemon_cache[name]
    
    try:
        pokemon = pypokedex.get(name=name)
        
        # Extract relevant data
        data = {
            "name": pokemon.name,
            "dex": pokemon.dex,
            "types": pokemon.types,
            "abilities": [ability.name for ability in pokemon.abilities],
            "height": pokemon.height,
            "weight": pokemon.weight
        }
        
        pokemon_cache[name] = data
        return data
    except Exception as e:
        print(f"Error fetching Pokemon data for {name}: {str(e)}")
        # Return basic data if API call fails
        return {
            "name": name,
            "dex": 0,
            "types": [],
            "abilities": [],
            "height": 0,
            "weight": 0
        }

def get_pokemon_for_function_type(function_type: str) -> Tuple[str, str]:
    """
    Get the recommended Pokemon for a given function type.
    
    Args:
        function_type: The type of function (display, error, processing, etc.)
        
    Returns:
        A tuple of (pokemon_name, reason)
    """
    function_type = function_type.lower()
    
    if function_type in FUNCTION_TYPE_MAPPING:
        mapping = FUNCTION_TYPE_MAPPING[function_type]
        return mapping["pokemon"], mapping["reason"]
    
    # Default to machamp if function type is not recognized
    return "machamp", "Default Pokemon for general-purpose functions"

def suggest_pokemon_name(function_description: str) -> Tuple[str, str, str]:
    """
    Suggest a Pokemon name based on the function description.
    
    Args:
        function_description: A description of what the function does
        
    Returns:
        A tuple of (pokemon_name, function_type, reason)
    """
    # Simple keyword matching to determine function type
    keywords = {
        "display": ["display", "show", "print", "output", "banner", "ui"],
        "error": ["error", "exception", "fail", "crash", "problem"],
        "processing": ["process", "handle", "compute", "calculate"],
        "verification": ["verify", "check", "validate", "test"],
        "setup": ["setup", "initialize", "prepare", "create"],
        "configuration": ["config", "configure", "setting", "option"],
        "parsing": ["parse", "extract", "read", "interpret"],
        "formatting": ["format", "style", "layout", "structure"],
        "progress": ["progress", "status", "loading", "advance"],
        "file": ["file", "save", "load", "read", "write"],
        "network": ["network", "http", "request", "api", "fetch"],
        "validation": ["validate", "check", "verify", "ensure"],
        "logging": ["log", "record", "track", "monitor"]
    }
    
    # Count keyword matches for each function type
    matches = {}
    for function_type, type_keywords in keywords.items():
        count = sum(1 for keyword in type_keywords if keyword.lower() in function_description.lower())
        if count > 0:
            matches[function_type] = count
    
    # Get the function type with the most keyword matches
    if matches:
        best_match = max(matches.items(), key=lambda x: x[1])[0]
        pokemon, reason = get_pokemon_for_function_type(best_match)
        return pokemon, best_match, reason
    
    # Default to machamp if no keywords match
    return "machamp", "general", "Default Pokemon for general-purpose functions"

def generate_function_name(pokemon: str, action: str, description: str) -> str:
    """
    Generate a Pokemon-themed function name.
    
    Args:
        pokemon: The Pokemon name
        action: The action verb (show, process, verify, etc.)
        description: Additional description
        
    Returns:
        A function name in the format pokemon_action_description
    """
    # Clean up and format the parts
    pokemon = pokemon.lower().replace("-", "_").replace(" ", "_")
    action = action.lower().replace("-", "_").replace(" ", "_")
    description = description.lower().replace("-", "_").replace(" ", "_")
    
    return f"{pokemon}_{action}_{description}"

def get_function_name_suggestion(function_description: str, action: str, description: str) -> Dict:
    """
    Get a complete function name suggestion based on the function description.
    
    Args:
        function_description: A description of what the function does
        action: The action verb (show, process, verify, etc.)
        description: Additional description
        
    Returns:
        A dictionary with the suggested function name and related information
    """
    pokemon, function_type, reason = suggest_pokemon_name(function_description)
    function_name = generate_function_name(pokemon, action, description)
    
    # Get additional Pokemon data if available
    try:
        pokemon_data = get_pokemon_data(pokemon)
    except:
        pokemon_data = {"name": pokemon}
    
    return {
        "function_name": function_name,
        "pokemon": pokemon,
        "function_type": function_type,
        "reason": reason,
        "pokemon_data": pokemon_data
    }

# Example usage
if __name__ == "__main__":
    # Example 1: Get a function name for displaying a banner
    suggestion = get_function_name_suggestion(
        "Display a banner with application information", 
        "show", 
        "banner"
    )
    print(f"Suggested function name: {suggestion['function_name']}")
    print(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
    
    # Example 2: Get a function name for error handling
    suggestion = get_function_name_suggestion(
        "Display an error message with exception details", 
        "show", 
        "error"
    )
    print(f"Suggested function name: {suggestion['function_name']}")
    print(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")