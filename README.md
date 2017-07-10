# Generate a JSON Web Token key

This script generates a JSON Web Token key and outputs it to the command line.

Appropriate for use with https://github.com/jonhillmtl/django-jwt-auth


## Installation

- `pip install git+https://github.com/jonhillmtl/jwt-key-gen`

## Usage

- `jwt_key_gen`

After you generate the key

`export JWT_KEY=<key that was generated>`
    
or even `export JWT_KEY=\`jwt_key_gen\``_