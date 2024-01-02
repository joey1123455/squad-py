# SQUAD PYTHON

A Python wrapper for [Squadco API](https://squadinc.gitbook.io/squad-api-documentation/)

The api call descriptions are from the official documentation.


## Getting Started

To install the wrapper, enter the following into the terminal.
```bash
pip install squadco
```

Every api call requires this secret_key. Make sure to use this key when getting started. 
```python
from squad import Squad
client = Squad("SECRET_KEY")

```

If you want to use the Live Endpoint, pass the test=False in the client initialization.
```python
from squad import Squad
client = Squad("SECRET_KEY",test=False)

```

##  Sample Usage

```python
from squad import Squad
client = Squad("SECRET_KEY")

verify_transaction = client.payments.verify_transaction(txn_ref="SQDEBU6383961457377100021")
print(verify_transaction)
```


