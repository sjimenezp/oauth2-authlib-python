## Using OAuth2/OpenID Connect Authentication with Authlib and Flask

This is an example code repository demonstrating how to implement OAuth2/OpenID Connect authentication using the Authlib library with Flask framework. OAuth2/OpenID Connect is a widely used authentication framework that allows users to authenticate with third-party providers such as Google, Facebook, or GitHub.

### Configuration

To use OAuth2/OpenID Connect authentication, you need to obtain client credentials (client ID and client secret) from the authentication provider you want to use (e.g., Google, Facebook, etc.). Once you have the credentials, you need to configure them in the config.py file. Replace the placeholders with your actual credentials:

```python
# config.py

TEST_WEB_APP_CLIENT_ID = 'your_client_id'
TEST_WEB_APP_CLIENT_SECRET = 'your_client_secret'
```
