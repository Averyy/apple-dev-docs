# Authorizing API calls using bearer tokens

**Framework**: Video Subscriber Account  
**Role**: Article

Authenticate your endpoint calls by including a signed JWT token in the header of your requests.

## Overview

To call the Automatic Sign-In API, the web service requires you to include identifying information in the header of your request. The information is a *bearer token*, which is a string that specifies your organization as the token creator, and certifies the authenticity of the entity making the request. An example call to the API looks like this:

```shell
curl -v -H 'Authorization: Bearer [token string]' 
"https://api.storekit.itunes.apple.com/account/v1/autoSignIn/update"
```

The `[token string]` format is JSON Web Token (JWT), which consists of a header and a payload. The information you add in the token primarily provides the web service with:

- A number that App Store Connect issues that identifies your development team
- The bundle ID of the app that generates the Automatic Sign-In tokens (your media-streaming app)
- Certification of authenticity by using a cryptographic signature

## Generate an API key or access an existing key

Automatic Sign-In API relies on the same authentication mechanism as StoreKit, so the web service checks the request header for an identifier of an In-App Purchase API key. App Store Connect issues your development team a unique key ID at your request and you include it in the header to identify that you’re the request originator.

If your app implements In-App Purchase and you have an existing API key, you can use it in the requests. Retrieve an existing key ID in [App Store Connect](https://appstoreconnect.apple.com) on the Users and Access page, from the Keys tab. The page lists any existing key IDs in a column under the Active heading. Hover over a key to reveal a link that copies the ID to the clipboard.

To create an API key:

1. Navigate to the [App Store Connect](https://appstoreconnect.apple.com) Users and Access page and the Integrations tab.
2. In the sidebar under Keys, click In-App Purchase.
3. Click Generate In-App Purchase Key, or the Add (+) icon to add another key.
4. Enter a name for the key. The name is for your reference on the website only.
5. Click Generate to finalize creation and see the key ID next to the key’s name on the page.

You only have to create an API key once. Use its ID on all of your requests. However, the key information is read only, so if you want to change the key name, for example, you revoke it and generate a new one.

## Create the token header

The token header is a JSON object that contains the following fields:

| Header field | Value |
| --- | --- |
| `alg` (Encryption algorithm) | “`ES256`”, per the JWT specification. |
| `kid` (Key ID) | Your API key ID from App Store Connect, for example, “`2X9R4HXF34`”. Use the same value for all requests. |
| `typ` (Token type) | “`JWT`”, per the JWT specification. |

Here’s an example of a complete JWT header:

```json
{
  "alg": "ES256",
  "kid": "2X9R4HXF34",
  "typ": "JWT"
}
```

## Create the token payload

The token payload is a JSON object that contains the following fields:

| Payload field | Value |
| --- | --- |
| `iss` (Issuer) | Your issuer ID from the Keys page in [App Store Connect](https://appstoreconnect.apple.com), for example, “`57246542-96fe-1a63-e053-0824d011072a"`. You can retrieve the issuer ID in the App Store Connect Users and Access page by selecting the Keys tab. The issuer ID appears near the top, near a Copy button that copies the ID to the clipboard. |
| `iat` (Issued at) | A UNIX timestamp (seconds since epoch) for the token’s issuance, for example, `1623085200`. |
| `exp` (Expiration) | A UNIX timestamp (seconds since epoch) for the token’s expiration, for example, `1623086400`. The system invalidates a token 60 minutes past issuance, so the expiration time is meaningful only within a 60 minute window past issuance. |
| `aud` (Audience) | “`appstoreconnect-v1`” |
| `bid` (Bundle ID) | Your app’s bundle ID, for example, `“com.example.mediaStreamingApp”` |

Here’s an example of a complete JWT payload:

```json
{
  "iss": "57246542-96fe-1a63e053-0824d011072a",
  "iat": 1623085200,
  "exp": 1623086400,
  "aud": "appstoreconnect-v1",
  "bid": "com.example.mediaStreamingApp"
}
```

## Sign the token

To ensure the authenticity of the request, sign the token with your API-key private key using ES256 encryption. If you have more than one API key, sign the token using the private key that corresponds the `kid` field you choose in the token header.

> ❗ **Important**: [App Store Connect](https://appstoreconnect.apple.com) provides the private key when you generate your API key. Download the private key on the Users and Access page, from the Integrations tab. Click In-App Purchase under Keys in the sidebar, and click Download for the desired key under the Active heading.
>
> The download link appears only once per key. Store your private key in a secure place, as Apple can’t restore a private key if you lose it.

Finally, include the signed token value in the header of your API request. For more information on signing JWTs, see [JWT.io](https://jwt.io/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/authorizing-api-calls-using-bearer-tokens)*