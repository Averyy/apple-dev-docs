# Export a PDF document from an iWork file

**Framework**: iWork Document Exporting API  
**Kind**: httpRequest

Create a PDF preview of an iWork document using JSON Web Token (JWT) authorization.

**Availability**:
- iWork 14.0+

#### Privacy Notice

It’s important for apps to inform people that uploaded iWork documents are temporarily stored on Apple servers for the purpose of conversion. Provide people the option to enable and disable the iWork preview feature, and display a privacy notice when doing so, such as “When using iWork online previews, your files will be temporarily stored on Apple servers.”

#### Supported Files

The maximum file size the service supports is 1 GB and the service can only convert documents not protected with a password.

#### Authentication and Request Payload

For each request, the iWork service requires a signature so that the service can confirm that the client has permission to access the API. The service uses a [`JSON Web Token (JWT)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7519) to transfer the signature, information about the client and the details of the document export request. Sign the JWT with an ES256 key acquired from [`Apple Developer Keys`](https://developer.apple.comhttps://developer.apple.com/account/resources/authkeys/list).

Using Open Source libraries recommended by [`JWT.io`](https://developer.apple.comhttps://jwt.io/libraries) may simplify the process of constructing and signing JWTs.

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

#### Examples

##### Export Request

The following example demonstrates an export request using the headers and their associated values you pass to the API:

```None
POST /iwork/api/v2/export HTTP/1.1
authorization: eyJhbGciOiJFUzI1NiIsImtpZCI6IkIzQ1U3TUhQUzgifQ.eyJlbmNvZGVkX2ZpbGVuYW1lIjoiOEorWWdDQmpiRzkxWk9LWWdTNXVkVzFpWlhKeiIsImV4cG9ydF9mb3JtYXQiOiJjb20uYWRvYmUucGRmIiwiaWF0IjoxNjkzMDA0MDQxLCJpc3MiOiI0M0tUTFlYTTRHIiwiZXhwIjoxNjkzMDExMjQxfQ.4Uw6_WeYZgmi2gXC82tBeSXDGwa2ajouG2tQVgNlWPld0mxTHuc0VSNWDUOr5QlPZqjJYMKEdZ4wpTmEfuuVcg
Content-Type: application/octet-stream
Host: https://iworkpreviewapi.icloud.com
Content-Length: 323927

<Binary iWork file goes here>
```

The filename is “😀 cloud☁.numbers”.

##### Generating a Jwt Using Json Object Signing and Encryption Jose

For more information on the [`JOSE`](https://developer.apple.comhttps://github.com/panva/jose) NodeJS package, see the [`JOSE package documentation`](https://developer.apple.comhttps://github.com/panva/jose/blob/main/docs/classes/jwt_sign.SignJWT.md).

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

## Request Body

 The body of the request. The body contains the iWork document for the service to export in raw binary form. If the original file is a package file, zip it before adding to the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iworkdocumentexportingapi/create-an-export-job-(v2))*