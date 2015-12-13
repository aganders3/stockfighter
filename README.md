These are just some Python functions I am using to complete the trading levels
on stockfighter.io.

I am using Python 3.5 in my environment. You will also need to install the
`requests` library if you'd like to use these functions.

There is a missing file, such that I don't expose my API key. The file is
called (fittingly) `api_key.py`, and it should look like this inside (insert
your own key):

```
api_key = <YOUR_API_KEY_HERE>
auth_header = {'X-Starfighter-Authorization' : api_key}
```
