# JSON Responses

We can build a JSON API fairly quickly with flask. To do so, we import the
`jsonify` function and use when returning a dictionary:

```python
from flask import jsonify

@app.route('/json-response')
def json_response():
    return jsonify({
        'message': 'Hello, World!'
    })
```
