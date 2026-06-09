# Implementing OAuth for the Apple School Manager and Apple Business API

**Framework**: Apple School Manager and Apple Business APIs

Manage secure access to Apple School Manager and Apple Business API accounts.

##### Overview

The Apple School Manager and Apple Business APIs support OAuth 2. With OAuth 2, apps authenticate with a set of credentials in exchange for an access token to make authenticated requests to the API.

A user with the role of Administrator in Apple School Manager or the role of Organization Administrator in Apple Business creates these credentials. For information about creating an app account, see:

- [`Create an API account in Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/axm33189f66a)
- [`Create an API account in Apple Business`](https://developer.apple.comhttps://support.apple.com/guide/business/axm33189f66a)

To make API calls, you attach the access token as a bearer token in the authorization header. This implementation process guides you through the following steps to obtain that access token:

- Create a client assertion.
- Request an access token.

##### Create a Client Assertion

A client assertion is a JSON web token ([`JWT`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519)) that an app creates and signs using a private key. The client assertion obtains an access token by calling the authorization server.

The example below is a Python script that generates, encodes, and signs a client assertion using an app’s private key. It expects [`PyJWT`](https://developer.apple.comhttps://pyjwt.readthedocs.io) to be installed in the executing Python environment. If you decide to create your own JWT using a different programming language and open source library, be sure the library you use supports [`elliptic curve`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc6605) methods.

> ❗ **Important**: Ensure that you copy the private key into your working directory.

```python
import datetime
import uuid

import jwt

private_key_file = "private-key.pem"
client_id = "BUSINESSAPI.c75c0a8a-a026-4dae-99aa-89ea1e1103e5"
team_id = "BUSINESSAPI.c75c0a8a-a026-4dae-99aa-89ea1e1103e5"
key_id = "e339d085-a821-438a-a527-d044edacf50a"
audience = "https://account.apple.com/auth/oauth2/v2/token"
alg = "ES256"

# Define the issue timestamp.
issued_at_timestamp = int(datetime.datetime.utcnow().timestamp())
# Define the expiration timestamp, which may not exceed 180 days from the issue timestamp.
expiration_timestamp = issued_at_timestamp + 86400*180

# Define the JWT headers.
headers = {
    "alg": alg,
    "kid": key_id,
}

# Define the JWT payload.
payload = {
    "aud": audience,
    "exp": expiration_timestamp,
    "iat": issued_at_timestamp,
    "sub": client_id,
    "jti": str(uuid.uuid4()),
    "iss": team_id,
}

# Open the private key.
with open(private_key_file, 'rb') as file:
    private_key_bytes = file.read()

# Encode the JWT and sign it with the private key.
client_assertion = jwt.encode(
    payload,
    private_key_bytes,
    headers=headers,
)

# Save the client assertion to a file.
with open('client_assertion.txt', 'wt') as output:
    output.write(client_assertion)
```

A client assertion header describes the type of the token and the hashing algorithm it uses.

| **Key** | **Description** |
| --- | --- |
| `alg` | The algorithm that signs the client assertion. The value needs to be `ES256`. |
| `kid` | The value is your `keyId` that returns when you upload a public key. |

The client assertion includes a payload with claims.

| **Claim** | **Description** |
| --- | --- |
| `aud` | The audience for the client assertion. The value is: `https://account.apple.com/auth/oauth2/v2/token`. |
| `exp` | The UNIX UTC timestamp of when the client assertion expires. The value needs to be greater than the current date and time, and less than 180 days from the `iat` timestamp. |
| `iat` | The UNIX UTC timestamp of when you create the client assertion. |
| `sub` | The subject the client assertion represents. The value is your `clientId`. |
| `jti` | Any unique identifier. |

The following is an example of an unencoded payload and header encoded into a JWT:

```json
// Header
{
"alg": "ES256",
"kid": "d136aa66-0c3b-4bd4-9892-c20e8db024ab"
}
// Payload
{
"iat": 2234567891,
"exp": 2234567900,
"aud": "https://account.apple.com/auth/oauth2/v2/token",
"sub": "BUSINESSAPI.9703f56c-10ce-4876-8f59-e78e5e23a152"
}
```

The following is an example of a client assertion:

```console
eyJraWQiOiJiYWNhZWJkYS1lMjE5LTQxZWUtYTkwNy1lMmMyNWIyNGQxYjIiLCJhbGciOiJFUzI1NiJ9.
eyJpc3MiOiJEcmVhbWNvbXBhbnkiLCJhdWQiOiJBdXRoZW50aWNhdG9yIiwiZXhwIjoxNTcxNjcwNjIx
LCJuYmYiOjE1NzE2NjcwMjEsInN1YiI6Im11c3RlciIsImNsaWVudF9pZCI6ImFiY2QxMjM0IiwiYWRt
aW4iOiJ0cnVlIn0.s4C3p9kVNFeRAB5tChatC3ldQX07v9mG7thL7FeEO6cClfNuiaLSgq8f8ymbfO3O
QYW_KuwaA1KYRuoy1JmKk 4DBbYLcz6aoABe0pzI5Z_6wgMzAyqz8pQtwDAcd4Idoi8JdRbtzZce9o-0
nZiFA4hVAXqYwpEYC4UU8ZmJO_z8tY4juHPTV3nDugdtqyNnmAiBoLryOfGNngQZccdY1_QvkXS1y0bg1
a0k8cVVtnq- _93fYJIt9Z64CTvlH3uOeh7uaEv3nIxpXhvhkTySpUmY8e04TO09oTyZijiloByv3KFQ9
2OOJ8L 5N5_CeEc5p9LWjT1pcX8ATamOycZz2Q
```

##### Request an Access Token

To receive an access token, make a POST request to the authorization server using the client assertion above. When an access token expires, use the same process to obtain a new one.

```console
curl -X POST \
-H 'Host: account.apple.com' \
-H 'Content-Type: application/x-www-form-urlencoded' \
'https://account.apple.com/auth/oauth2/token?grant_type=client_credentials&
client_id=BUSINESSAPI.27478e71-3bb0-4588-998c-182e2b405577&
client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&
client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.zI1NiIsImprdSI6Imh0dHBzOi8
vYXV0aC5kZXYuYXBpLnJpY29oL3YxL2Rpc2NvdmVyeS9rZXlzIiwia2lkIjoiMmIyZTgyMTA2NzkxZGM4Zm
FkNzgxNWQ3ZmI1NDRhNjJmNzJjMTZmYSJ9.eyJpc3MiOiJodHRwczovL2F1dGguZGV2LmFwaS5yaWNvaC8iL
CJhdWQiOiJodHRwczovL2lwcy5kZXYuYXBpLnJpY29oLyIsImlhdCI6MTQ5MDg1Mjc0MSwiZXhwI
joxNDkwODU2MzQxLCJjbGllbnRfaWQiOiI4ODQwMWU1MS05MzliLTQ3NzktYjdmNy03YzlmNGIzZj
kyYzAiLCJzY29wZSI6Imh0dHBzOi8vaXBzLmRldi5hcGkucmljb2gvdjEiLCJyaWNvaF9tc3Mi
OnsibWVkaWEiOnsicXVvdGEiOjEwLCJ0aHJvdHRsZSI6eyJ2YWx1ZSI6MCwid2luZG93IjowfX1
9fQ.jVq_c_cTzgsLipkJKBjAHzm8KDehW4rFA1Yg0EQRmqWmBDlEKtpRpDHZeF6ZSQfNH2OlrBW
FBiVDV9Th091QFEYrZETZ1IE1koAO14oj4kf8TCmhiG_CtJagvctvloW1wAdgMB1_Eubz9a8oim
cODqL7_uTmA5jKFx3ez9uoqQrEKZ51g665jSI6NlyeLtj4LrxpI9jZ4zTx1yqqjQx0doYQjBPhOB
06Z5bdiVyhJDRpE8ksRCC3kDPS2nsvDAal28sMgyeP8sPvfKvp5sa2UsH78WJmTzeZWcJfX2C2ba3
xwRMB5LaaVrQZlhj9xjum0MfDpIS1hJI6p5CHZ8w&scope=business.api'
```

| **Request header** | **Description** |
| --- | --- |
| `Host` | **(Required)** `account.apple.com` |
| `Content-Type` | **(Required)** `application/x-www-form-urlencoded` |

| **Request parameter** | **Type** | **Description** |
| --- | --- | --- |
| `grant_type` | String | **(Required)** The value needs to be `client_credentials`. |
| `client_id` | String | **(Required)** You receive your `clientId` when you upload a public key. |
| `client_assertion` | String | **(Required)** The client assertion is a JWT that you create and sign with your private key. |
| `client_assertion_type` | String | **(Required)** The value needs to be `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`. |
| `scope` | String | **(Required)** Defines the access permissions you request from the user, and limits the authorization of the access token you receive.  The value is `business.api` or `school.api`. |

After accepting the credentials, the authorization server returns an access token.

```json
{
"access_token":"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwia2lkIjpudWxsfQ
..lXm332TFi0u2E9YZ.bVVBvsjcavoQbBnQVeDiqEzmUIlaH9zLKY6rl36A_TD8wvgvWxp
yBXMQuhs-qWG_dxQ5nfuJEIxOp8bIndfLE_4a3AiYtW0BsppO3vkWxMe0HWnzglkFbKUHU
3PaJbLHpimmnLvQr44wUAeNcv1LmUPaSWT4pfaBzv3dMe3PNHJJCLVLfzNlWTmPxViIivQ
t3xyiQ9laBO6qIQiKs9zX7KE3holGpJ-Wvo39U6ZmGs7uK9BoNBPaFtd_q914mb9ChHAKc
QaxF3Gadtu_Z5rYFg.vD0iQuRwHGYVnDy27qexCw",
"token_type": "Bearer",
"expires_in": 3600,
"scope": "business.api"
}
```

| **Response parameter** | **Type** | **Description** |
| --- | --- | --- |
| `access_token` | String | Your `access_token` is a requirement to make calls to Apple School Manager and Apple Business API endpoints.  Your `access_token` is valid for the number of seconds that `expires_in` specifies. |
| `token_type` | String | The type of access token. The value is `Bearer`. |
| `expires_in` | Integer | The token lifetime (TTL) of one hour (3600 seconds). |
| `scope` | String | Defines the access permissions you request from the app, and limits the authorization of the access token you receive. |

Use this token to access Apple School Manager and Apple Business APIs. The access token has an expiration of 1 hour. Apps need to generate an access token every hour, and also whenever Apple School Manager and Apple Business APIs return a ‘401’ response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-manager-and-apple-business-api)*