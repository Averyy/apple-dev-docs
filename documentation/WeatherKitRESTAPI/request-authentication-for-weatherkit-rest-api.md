# Request authentication for WeatherKit REST API

**Framework**: Weatherkitrestapi

Create a developer token to access weather data.

#### Overview

To make requests to the WeatherKit REST API, authorize yourself as a trusted developer and member of the [`Apple Developer Program`](https://developer.apple.comhttps://developer.apple.com) (ADP). The header of every WeatherKit REST API request requires a signed developer token to identify the authorized ADP member and application or service making the request.

##### Create a Private Key and Service Id

Create a WeatherKit identifier and private key so you can use a developer token to authenticate yourself as a trusted developer and member of the Apple Developer Program.

To begin, go to your Apple Developer Account, then navigate to Certificates, Identifiers & Profiles. Select the Keys menu to create and download a WeatherKit key.

Next, create a Service ID from the Identifiers menu.

- Click + to add, select Services IDs, and then Continue.
- Set a description and the identifier you wish to use, for example, `com.example.weatherkit-client`.
- Click Continue, then Register to register the identifier.

##### Generate the Web Token

WeatherKit supports the JSON Web Token (JWT) specification, and allows you to pass statements and metadata called claims. For more information about JWT, see the [`JWT specification`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7519). There are a variety of open source libraries available online for creating and signing JWT tokens. See [`JWT.io`](https://developer.apple.comhttps://jwt.io) for more information.

Construct a developer token as a JSON object with a header that contains the following information:

WeatherKit only supports developer tokens signed with the ES256 algorithm, and rejects unsecured developer tokens or developer tokens signed with other algorithms. These rejections result in a 401 error code.

> **Note**:  Ensure that the token contains only the claims listed below.

In the claims payload of the token, include the following:

A decoded developer token has the following format:

```json
{
    "alg": "ES256",
    "kid": "ABC123DEFG",
    "id": "DEF123GHIJ.com.example.weatherkit-client"
}
{
    "iss": "DEF123GHIJ",
    "iat": 1437179036,
    "exp": 1493298100,
    "sub": "com.example.weatherkit-client"
}
```

After you create the token, sign it with your WeatherKit private key using the ES256 algorithm, which is the JSON Web Algorithms (JWA) name for the Elliptic Curve Digital Signature Algorithm (ECDSA) with the P-256 curve and the SHA-256 hash.

Follow these guidelines whenever you use signed JWTs:

- Never distribute your private key. If you need to create tokens for apps or websites, create an authenticated service to create and sign your own tokens.
- Be mindful of token expiration times. Longer times require less overhead, but shorter times ensure a higher level of security.
- If your token has an extended time before expiring, be sure to store it securely.

##### Authorize Requests

Pass the developer token as a parameter to the `Authorization: Bearer` header in each request. Here’s an example of a request:

```sh
curl -v -H 'Authorization: Bearer [developer token]' "https://weatherkit.apple.com/api/v1/availability/37.323/122.032?country=US"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/WeatherKitRESTAPI/request-authentication-for-weatherkit-rest-api)*