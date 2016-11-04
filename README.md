# Unofficial OpenProvider client for Python

...

## Requirements

To use the Unofficial OpenProvider API client, the following things are required:
- Get yourself a [OpenProvider](https://www.openprovider.nl/) account.
- OpenProvider API client has a dependecy on [Requests](http://docs.python-requests.org/en/master/) and [xmltodict](https://github.com/martinblech/xmltodict).

## Installation

...

## Getting started

Require the OpenProvider API Client.

```python
openprovider = OpenProvider.API.Client()
openprovider.setApiUsername('username')
openprovider.setApiHash('hashcode')
```

Retrieving domain information.

```python
domains = openprovider.domains.search(
    domain_name_pattern='example',
    extension='nl'
)
```

## License

...
