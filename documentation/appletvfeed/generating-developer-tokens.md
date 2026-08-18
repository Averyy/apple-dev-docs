# Generating developer tokens

**Framework**: Apple TV Feed

Create a JSON Web Token to authorize your requests to the Apple Media Feed API.

#### Overview

The header of each Apple Media Feed API request requires authorization in the form of a developer token. A developer token is a signed token that authenticates you as a trusted developer and member of the Apple Developer Program.

The Apple Media Feed API supports the JSON Web Token (JWT) specification, so you can pass statements and metadata called *claims*. For more information, see the [`JWT specification`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) and the available libraries for generating signed JWTs.

The Apple Media Feed API limits the number of requests you can make using a developer token within a specific period of time. If you exceed this limit, you temporarily receive `429 Too Many Requests` error responses for requests that use the token. This error resolves itself shortly after the request rate decreases.

#### Create Your Developer Token

Use the following information supplied by Apple through the [`Performance Partner Portal`](https://developer.apple.comhttps://partners.marketingtools.apple.com) to create a signed JWT:

- Team ID
- Key ID
- Private key

Create a developer token as a JSON object with a header that includes the following:

- **`alg`**: The algorithm you use to sign the token, which requires the value of `ES256`.
- **`kid`**: The key ID supplied by Apple.

> ❗ **Important**: The Apple Media Feed API supports only developer tokens signed with the ES256 algorithm. The API rejects unsecured developer tokens or developer tokens signed with other algorithms. These rejections result in a `401` error code.

In the claims payload of the token, include the following:

- **`iss`**: The *issuer* registered claim key, the team ID supplied by Apple.
- **`iat`**: The *issued at* registered claim key. This value indicates the time that the system generated the token, in UNIX time.
- **`exp`**: The *expiration time* registered claim key. This value can’t be greater than `15777000` (6 months in seconds) from the current UNIX time on the server.
- **`origin`**: (Optional) The *origin* claim, a list of authorized URLs. This addition helps prevent unauthorized use of the tokens and is recommended for web clients. Only use this claim if the origin header of the request matches one of the values in the list.

A decoded developer token has the following format:

```None
{
    "alg": "ES256",
    "kid": "ABC123DEFG"
}
{
    "iss": "DEF123GHIJ",
    "iat": 1437179036,
    "exp": 1493298100
    "origin": [“https://example.com“,“https://tv.example.com“]
}
```

After you create the token, sign it with your private key using the ES256 algorithm.

> **Note**: ES256 is the [`JSON Web Algorithms (JWA)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7518) name for the Elliptic Curve Digital Signature Algorithm (ECDSA) with the P-256 curve and the SHA-256 hash.

#### Authorize Requests

If you manage request authorization directly, in all requests, pass the `Authorization: Bearer` header set to the developer token.

```None
curl -v -H 'Authorization: Bearer [developer token]' "https://api-feeds.tv.apple.com/v1/test"
```

## See Also

- [Requesting a feed export](requesting-a-feed-export.md)
  Create requests for Apple TV Catalog metadata.
- [Interpreting responses](interpreting-responses.md)
  Learn about responses from the Apple Media Feed API to your Apple TV Feed requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/generating-developer-tokens)*