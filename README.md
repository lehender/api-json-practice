# API & JSON Practice

This mini-project demonstrates REST API troubleshooting and JSON validation using the public [PokéAPI](https://pokeapi.co/).  
It’s designed to show hands-on familiarity with SaaS-style API concepts: requests, responses, and error handling.

---

### What It Does
- Sends GET requests to REST endpoints (`https://pokeapi.co/api/v2/pokemon/{name}`)
- Parses JSON payloads and displays key-value data
- Demonstrates handling of valid (200 OK) and invalid (404 Not Found) responses
- Uses the Python `requests` library to automate API testing
- Complements manual inspection with Postman

---

### Skills Demonstrated
- REST API fundamentals  
- JSON structure validation  
- HTTP status troubleshooting (200/404)  
- Basic Python scripting (`requests`, error handling)  
- Postman usage for API verification  

---

### How to Run
```bash
pip install requests
python api_practice.py
```
