# TwitterAPIAuthorizer
Library to generate Twitter access bearer token through oauth2

## Usage

```python3
from authorizer import Authorizer

def main():
  public_key = 'xxxxxxx'
  private_key = 'xxxxxxx'

  auth = Authorizer()
  bearer = auth.get_bearer(public_key, private_key)
```
