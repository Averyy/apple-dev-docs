# Implementing OAuth for the Apple Ads Platform API

**Framework**: Apple Ads Platform API

Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

The Apple Ads Platform API supports the OAuth2 framework. With this framework, you can authenticate using credentials in exchange for an access token to make authenticated requests to the Apple Ads Platform API.

The implementation process:

- Invite users with API permissions.
- Generate a private-public key pair.
- Extract a public key from your persisted private key.
- Upload a public key.
- Create a client secret.
- Request an access token.

#### Invite Users

Account administrators invite users with API permissions using the following process:

1. From [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com), choose Sign In > Advanced and log in as an account administrator.
2. From the Users menu in the top-right corner, select the account to invite users to.
3. Choose Account Settings > User Management.
4. Click Invite Users to invite users to your Apple Ads organization.
5. In the User Details section, enter the user’s first name, last name, and Apple Account.
6. In the User Access and Role section, select an API user role. For non-API roles, see [`Invite users to your account`](https://developer.apple.comhttps://ads.apple.com/help/advanced/0011-invite-users-to-your-account/).
7. Click Send Invite. The invited user receives an email with a secure code. The user signs into the secure Apple URL in the email and inputs the provided code, which activates the user’s account.

#### Generate a Private Key

API users need to create a private key. If you’re using macOS or a Unix-like operating system, OpenSSL works natively. If you’re on a Windows platform, you need to download [`OpenSSL`](https://developer.apple.comhttps://www.openssl.org).

This command uses OpenSSL to generate a new elliptic curve private key, which you use to sign requests and prove ownership of the public key you upload to Apple Ads:

```console
openssl ecparam -genkey -name prime256v1 -noout -out private-key.pem
```

- **`-name`**: The name of the Elliptic Curve Digital Signature Algorithm (ECDSA) curve to use, `prime256v1`.
- **`-out`**: The `.pem` filename where you generate and store the key pair.

The generated `private-key.pem` file resembles the following example:

```console
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIKtnxllRY8nbndBQwT9we4pEULtjpW605iwvzLlKcBq4oAoGCCqGSM49
AwEHoUQDQgAEY58v74eQFyLtu5rtCpeU4NggVSUQSOcHhN744t0gWGc/xXkCSusz
LaZriCQnnqq4Vx+IscLFcrjBj+ulZzKlUQ==
-----END EC PRIVATE KEY-----
```

> ❗ **Important**: Always keep your private key secure and never share it. If your private key is compromised, you need to re-create a private key and client secret, and reupload it to your [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com) account.

#### Extract a Public Key

To extract a public key from your persisted private key, use the following command:

```console
openssl ec -in private-key.pem -pubout -out public-key.pem
```

This command takes two parameters:

- **`-in`**: The private key filename `private-key.pem`.
- **`-out`**: The `public-key.pem` file where you generate and store the public key.

Open the `public-key.pem` file in a text editor and copy the public key, including the begin and end lines.

#### Upload a Public Key

Follow these steps to upload your public key:

1. From the Ads UI, choose Account Settings > API. Paste the key you created in Extract a Public Key into the Public Key field.
2. Click Save.
3. Copy your private-public key pair into your working directory.

After you save, a group of credentials displays as a code block above the public key field. To create a client secret, use the `clientId`, `teamId`, and `keyId` from this block:

```console
clientId SEARCHADS.aeb3ef5f-0c5a-4f2a-99c8-fca83f25a9
teamId SEARCHADS.hgw3ef3p-0w7a-8a2n-77c8-scv83f25a7
keyId a273d0d3-4d9e-458c-a173-0db8619ca7d7
```

You can make edits to the public key by choosing Account Settings > API > Edit.

#### Create a Client Secret

A *client secret* is a JSON web token ([`JWT`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519)) that you create and sign using your private key. Your client secret authenticates token requests to the authorization server. Only you and the authorization server know the client secret.

The following example is a Python 3 script that generates, encodes, and signs the client secret using your private key. If you decide to create your own JWT using a different programming language and open-source library, make sure the library you use supports elliptic curve methods.

> ❗ **Important**: Make sure that you copy the private-public key pair into your working directory.

```python
import os
import datetime as dt
from authlib.jose import jwt
from Crypto.PublicKey import ECC


private_key_file = "private-key.pem"
public_key_file = "public-key.pem"
client_id = "SEARCHADS.8b8cdf43-5299-41d1-be59-cfa5ccd99228"
team_id = "SEARCHADS.8b8cdf43-5299-41d1-be59-cfa5ccd99228"
key_id = "8c33455f-4944-4926-87dc-44cb13796d7c"
audience = "https://appleid.apple.com"
alg = "ES256"

if os.path.isfile(private_key_file):
    with open(private_key_file, "rt") as file:
        private_key = ECC.import_key(file.read())
else:
    private_key = ECC.generate(curve='P-256')
    with open(private_key_file, 'wt') as file:
        file.write(private_key.export_key(format='PEM'))

    public_key = private_key.public_key()
    if not os.path.isfile(public_key_file):
        with open(public_key_file, 'wt') as file:
            file.write(public_key.export_key(format='PEM'))


# Use timezone-aware UTC datetime so .timestamp() is correct on all systems.
issued_at_timestamp = int(dt.datetime.now(dt.timezone.utc).timestamp())
expiration_timestamp = issued_at_timestamp + 86400 * 180

headers = {'alg': alg, 'kid': key_id}

payload = {
 'sub': client_id,
 'aud': audience,
 'iat': issued_at_timestamp,
 'exp': expiration_timestamp,
 'iss': team_id,
}

# Open the private key.
with open(private_key_file, 'rt') as file:
    private_key = ECC.import_key(file.read())

client_secret = jwt.encode(
 header=headers,
 payload=payload,
 key=private_key.export_key(format='PEM')
).decode('UTF-8')

with open('client_secret.txt', 'w') as output:
    output.write(client_secret)
```

A client secret header describes the type of the token and the hashing algorithm it uses:

- **`alg`**: The algorithm that signs the client secret. The value must be `ES256`.
- **`kid`**: The value is your `keyId` that returns when you upload a public key.

The client secret includes a payload with claims:

- **`aud`**: The audience for the client secret. The value is `https://appleid.apple.com`.
- **`exp`**: The UNIX UTC timestamp of when the client secret expires. The value must be greater than the current date and time, and less than 180 days from the `iat` timestamp.
- **`iss`**: The issuer of the client secret. The value is your `teamId`.
- **`iat`**: The UNIX UTC timestamp of when you create the client secret.
- **`sub`**: The subject the client secret represents. The value is your `clientId`.

The following is an example of an unencoded payload and header encoded into a JWT:

```None
// Header
{
"alg": "ES256",
"kid": "d136aa66-0c3b-4bd4-9892-c20e8db024ab"
}
// Payload
{
"iss": "SEARCHADS.9703f56c-10ce-4876-8f59-e78e5e23a152",
"iat": 2234567891,
"exp": 2234567900,
"aud": "https://appleid.apple.com",
"sub": "SEARCHADS.9703f56c-10ce-4876-8f59-e78e5e23a152"
}
```

The following is an example client secret:

```console
eyJraWQiOiJiYWNhZWJkYS1lMjE5LTQxZWUtYTkwNy1lMmMyNWIyNGQxYjIiLCJhbGciOiJFUzI1NiJ9.
eyJpc3MiOiJEcmVhbWNvbXBhbnkiLCJhdWQiOiJBdXRoZW50aWNhdG9yIiwiZXhwIjoxNTcxNjcwNjIx
LCJuYmYiOjE1NzE2NjcwMjEsInN1YiI6Im11c3RlciIsImNsaWVudF9pZCI6ImFiY2QxMjM0IiwiYWRt
aW4iOiJ0cnVlIn0.s4C3p9kVNFeRAB5tChatC3ldQX07v9mG7thL7FeEO6cClfNuiaLSgq8f8ymbfO3O
QYW_KuwaA1KYRuoy1JmKk4DBbYLcz6aoABe0pzI5Z_6wgMzAyqz8pQtwDAcd4Idoi8JdRbtzZce9o-0
nZiFA4hVAXqYwpEYC4UU8ZmJO_z8tY4juHPTV3nDugdtqyNnmAiBoLryOfGNngQZccdY1_QvkXS1y0bg1
a0k8cVVtnq-_93fYJIt9Z64CTvlH3uOeh7uaEv3nIxpXhvhkTySpUmY8e04TO09oTyZijiloByv3KFQ9
2OOJ8L5N5_CeEc5p9LWjT1pcX8ATamOycZz2Q
```

#### Request an Access Token

The client credentials code grant authenticates with your credentials in exchange for an access token. To receive an access token, make a `POST` request from the token endpoint to the authorization server, as shown in the code below. To obtain a new access token after one expires, repeat the same process.

```console
curl -X POST \
-H 'Host: appleid.apple.com' \
-H 'Content-Type: application/x-www-form-urlencoded' \
'https://appleid.apple.com/auth/oauth2/token?grant_type=client_credentials&
client_id=SEARCHADS.27478e71-3bb0-4588-998c-182e2b405577&client_secret=eyJhbGciOiJFUzI1NiIsImtpZCI6IllPVVJfS0VZX0lEIn0.PLACEHOLDER_PAYLOAD.PLACEHOLDER_SIGNATURE&scope=searchadsorg'
```

The request requires the following headers:

- **`Host`**: **Required**. `appleid.apple.com`.
- **`Content-Type`**: **Required**. `application/x-www-form-urlencoded`.

Include the following parameters in the request body:

- **`client_id`**: String. **Required**. You receive your `clientId` when you upload a public key.
- **`client_secret`**: String. **Required**. The client secret is a JWT that you create and sign with your private key.
- **`grant_type`**: String. **Required**. The method to request authorization and get an access token. The value is `client_credentials`.
- **`scope`**: String. **Required**. Defines the access permissions you request from the user, and limits the authorization of the access token you receive. The value is `searchadsorg`.

After accepting the credentials, the authorization server returns an access token, as shown here:

```json
{
  "access_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjpudWxsfQ..lXm332TFi0u2E9YZ.bVVBvsjcavoQbBnQVeDiqEzmUIlaH9zLKY6rl36A_TD8wvgvWxpyBXMQuhs-qWG_dxQ5nfuJEIxOp8bIndfLE_4a3AiYtW0BsppO3vkWxMe0HWnzglkFbKUHU3PaJbLHpimmnLvQr44wUAeNcv1LmUPaSWT4pfaBzv3dMe3PNHJJCLVLfzNlWTmPxViIivQt3xyiQ9laBO6qIQiKs9zX7KE3holGpJ-Wvo39U6ZmGs7uK9BoNBPaFtd_q914mb9ChHAKcQaxF3Gadtu_Z5rYFg.vD0iQuRwHGYVnDy27qexCw",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "searchadsorg"
}
```

The response includes the following parameters:

- **`access_token`**: String. Your `access_token` is a requirement to make calls to Apple Ads Platform API endpoints. See [`Managing Ad Accounts and API Access`](access-overview.md) for a complete walkthrough from this token to your first real request. Your `access_token` is valid for the number of seconds that `expires_in` specifies.
- **`token_type`**: String. The type of access token. The value is always `Bearer`.
- **`expires_in`**: Integer. The token lifetime (TTL) of one hour (3600 seconds).
- **`scope`**: String. Defines the access permissions you request from the user, and limits the authorization of the access token you receive.

## See Also

- [Calling the Apple Ads Platform API](calling-apple-ads-platform-api.md)
  Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.
- [Using Client Libraries](client-libraries.md)
  Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.
- [Applying Rate Limits](rate-limits.md)
  Track your remaining quota and pace requests.
- [Advertising Your App on the App Store](journey-app-store-ads.md)
  Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.
- [Advertising Your Business on Apple Maps](journey-apple-maps-brand-ads.md)
  Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/implementing-oauth-for-the-apple-ads-platform-api)*