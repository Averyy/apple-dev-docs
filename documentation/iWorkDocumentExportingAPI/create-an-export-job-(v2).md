# Export a PDF document from an iWork file

**Framework**: iWork Document Exporting API  
**Kind**: httpRequest  
**Role**: Web Endpoint

Create a PDF preview of an iWork document using JSON Web Token (JWT) authorization.

**Availability**:
- iWork 14.0+

## Privacy Notice

It’s important for apps to inform people that uploaded iWork documents are temporarily stored on Apple servers for the purpose of conversion. Provide people the option to enable and disable the iWork preview feature, and display a privacy notice when doing so, such as “When using iWork online previews, your files will be temporarily stored on Apple servers.”

## Supported files

The maximum file size the service supports is 1 GB and the service can only convert documents not protected with a password.

## Authentication and request payload

For each request, the iWork service requires a signature so that the service can confirm that the client has permission to access the API. The service uses a [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) to transfer the signature, information about the client and the details of the document export request. Sign the JWT with an ES256 key acquired from [Apple Developer Keys](https://developer.apple.com/account/resources/authkeys/list).

Using Open Source libraries recommended by [JWT.io](https://jwt.io/libraries) may simplify the process of constructing and signing JWTs.

Include these claims in the JWT header:

| Header claims | Value |
| --- | --- |
| `alg` | The name of the algorithm used to sign the token.  The algorithm the service supports is “ES256”. |
| `kid` | The ID of the Apple Developer Key used to sign the token.  The portal displays this ID on the key download page when downloading the key from Apple developer portal. |

Include these claims in the JWT payload:

| Payload claims | Value |
| --- | --- |
| `iss` | Issuer of the token. This is the ID of the Apple Developer Team,  your team’s ID, displayed in the membership details section of the Apple developer portal. |
| `encoded_filename` | The original filename of the file, encoding in UTF-8 and then encoded in URL-safe base64.  If the name is too long, or if it contains invalid characters, the service may ignore parts of the filename. |
| `export_format` | The format to export. Currently, the service only supports `com.adobe.pdf`. |
| `iat` | The creation time of the token, in terms of the number of seconds since the epoch, in UTC. |
| `exp` | Optional. The time at which the token expires, in terms of the number of seconds since the epoch, in UTC.  If you don’t provide an expiration time, the default value is four hours from the time specified by `iat`.  The actual expiry would be the specified value or four hours, whichever is smaller. |

Put the signed JWT as-is in the HTTP `authorization` header.

Clients need to ensure that their system clocks are accurate: The service rejects the signed JWT if the current time falls outside of the time window specified by `iat` and `exp`.  Reconstruct and sign the JWT with a new `DateTime` for each request even if you’re retrying the request.

The method to authenticate and sign the requests may change in light of new developments in the security field. Apple will give notice to parties using the API if and when this happens.

## Examples

### Export Request

The following example demonstrates an export request using the headers and their associated values you pass to the API:

```
POST /iwork/api/v2/export HTTP/1.1
authorization: eyJhbGciOiJFUzI1NiIsImtpZCI6IkIzQ1U3TUhQUzgifQ.eyJlbmNvZGVkX2ZpbGVuYW1lIjoiOEorWWdDQmpiRzkxWk9LWWdTNXVkVzFpWlhKeiIsImV4cG9ydF9mb3JtYXQiOiJjb20uYWRvYmUucGRmIiwiaWF0IjoxNjkzMDA0MDQxLCJpc3MiOiI0M0tUTFlYTTRHIiwiZXhwIjoxNjkzMDExMjQxfQ.4Uw6_WeYZgmi2gXC82tBeSXDGwa2ajouG2tQVgNlWPld0mxTHuc0VSNWDUOr5QlPZqjJYMKEdZ4wpTmEfuuVcg
Content-Type: application/octet-stream
Host: https://iworkpreviewapi.icloud.com
Content-Length: 323927

<Binary iWork file goes here>
```

The filename is “😀 cloud☁.numbers”.

### Generating a JWT using JSON Object Signing and Encryption (JOSE)

For more information on the [JOSE](https://github.com/panva/jose) NodeJS package, see the [JOSE package documentation](https://github.com/panva/jose/blob/main/docs/classes/jwt_sign.SignJWT.md).

```javascript
import * as jose from 'jose'

const alg = 'ES256'
const pkcs8 = `-----BEGIN PRIVATE KEY——
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQg0oCMjI+HiYGjXZCz
W8BKk4ZNjutgQbRPLDkD3g47djWgCgYIKoZIzj0DAQehRANCAATtEMfktkJxsvLV
zNZtwllVtt7TCpbaDrJE10lM25cF56mRy6RXfwVyuhCqw7xMMzJH+rfciw9+vnZk
4csA9gdr
-----END PRIVATE KEY-----`
const privateKey = await jose.importPKCS8(pkcs8, alg)

const jwt = await new jose.SignJWT({
    encoded_filename: Buffer.from('😀 cloud☁.numbers').toString('base64'),
    export_format: 'com.adobe.pdf'
})
    .setProtectedHeader({ alg, kid: 'HBLUFDY367' })
    .setIssuedAt()
    .setIssuer('43KTLYXM4G')
    .setExpirationTime('2h')
    .sign(privateKey)

console.log(jwt)
```

Using the above Apple Developer key, this is the JWT header and payload the package signs:

```javascript
// Header
{
  "alg": "ES256",
  "kid": "HBLUFDY367"
}
// Payload
{
  "encoded_filename": "8J+YgCBjbG91ZOKYgS5udW1iZXJz",
  "export_format": "com.adobe.pdf",
  "iat": 1693005092,
  "iss": "43KTLYXM4G",
  "exp": 1693012292
}
```

And the resulting signed JWT is:

`eyJhbGciOiJFUzI1NiIsImtpZCI6IkhCTFVGRFkzNjcifQ.eyJlbmNvZGVkX2ZpbGVuYW1lIjoiOEorWWdDQmpiRzkxWk9LWWdTNXVkVzFpWlhKeiIsImV4cG9ydF9mb3JtYXQiOiJjb20uYWRvYmUucGRmIiwiaWF0IjoxNjkzMDA1MDkyLCJpc3MiOiI0M0tUTFlYTTRHIiwiZXhwIjoxNjkzMDEyMjkyfQ.o4haQp-Fo-r_-_rELXhMEbOIXU8n-mr8sAogH8b6i8x9_VdHYnTw29r7hu0OjwA_HWNWfwpBvgLNtqr2dcl4Vg`

> **Note**: The signed JWT can be different for the same input.

## Endpoint

`POST https://iworkpreviewapi.icloud.com/iwork/api/v2/export`

## Parameters

### Header Parameters

- `Content-Length` (int64) *(required)*: The number of bytes in the request body as defined in [RFC 7230](https://www.rfc-editor.org/info/rfc7230).

  The service doesn’t support chunked transfer coding.
- `authorization` (string) *(required)*: A JWT as defined in the Authentication and as defined in the [Authentication and request payload](./create-an-export-job-%28v2%29.md#Authentication-and-request-payload) section, below.

## Request Body

**Content-Type**: `application/octet-stream`  
**Type**: `binary`

 The body of the request. The body contains the iWork document for the service to export in raw binary form. If the original file is a package file, zip it before adding to the request.

## Responses

- `200` OK (`binary`, `application/octet-stream`): Successful export.

  If the service successfully processed the request and exported the document, the server returns an HTTP 200 response with the exported file in the body.
- `400` Bad Request (`string`, `text/plain`): Invalid request.

  If the request is invalid for some reason (such as missing or invalid header values), the server returns an HTTP 400 response.

  The server returns the reason for the error in the response body, for example: `Invalid filename`.
- `403` Forbidden (`string`, `text/plain`): Authentication failure.

  If the server can’t validate the signature, either because the signature is invalid, or because the key pair can’t recognize the signature, the server returns an HTTP 403 response with body `Invalid signature`.

  If the document is password-protected, the server responds with a HTTP 403 response with body `Password protected document`.
- `404` Not Found (`string`, `text/plain`)
- `411` Length Required (`string`, `text/plain`)
- `413` Request Entity Too Large (`string`, `text/plain`): Request too large.

  The server returns this error if the document is over 1 GB.
- `429` (`string`, `text/plain`): Client is sending too many requests.

  If you’re sending too many requests, the server returns an HTTP 429 response. The server may give this response without completely reading the contents of the request. In this case, don’t retry the request.
- `500` Internal Server Error (`string`, `text/plain`): For other errors, the server returns an HTTP 500 response.

  For export errors caused by a corrupted document or other irrecoverable errors, the response body contains `Irrecoverable export error`. In this case, don’t retry exporting the same document. In general, don’t retry unless there is a `Retry-After` header in the response.
- `503` Service Unavailable (`string`, `text/plain`): Server asks client to retry.

  In some situations where the server is under heavy load, the server may return an HTTP 503 response.  The `Retry-After` response header specifies the number of seconds after which you may retry. Don’t retry unless there is a `Retry-After` header. The server may give this response without completely reading the contents of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iworkdocumentexportingapi/create-an-export-job-(v2))*