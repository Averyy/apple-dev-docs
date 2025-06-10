# Establishing a token-based connection to APNs

**Framework**: User Notifications

Secure your communications with Apple Push Notification service (APNs) by using stateless authentication tokens.

#### Overview

Token-based authentication offers a stateless way to communicate with APNs. Stateless communication is faster than certificate-based communication because it doesn’t require APNs to look up the certificate, or other information, related to your provider server. There are other advantages to using token-based authentication:

- You can use the same token from multiple provider servers.
- You can use one token to distribute notifications for all or a subset of your company’s apps.

Token-based requests are slightly larger than certificate-based requests because each request contains the token. You must also update and encrypt your tokens at least once an hour using the provider token signing key that Apple provides you. To learn more about key creation, see [`Create a private key to access a service`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/create-a-private-key/).

##### Team Scoped Keys

Use team-scoped keys to generate authentication tokens for sending notifications to any topic in a team. These keys restrict usage to either Sandbox or Production, enhancing security. They apply to all existing and new topics in the team. Each environment can have a maximum of two keys.

> ❗ **Important**:  If you have existing team-scoped keys that work in both the Sandbox and Production environments it will continue to be supported. However, it’s recommended to use different, environment-specific keys to create distinct workflows and to safely manage your development process.

##### Topic Specific Keys

Use topic-specific keys to generate authentication tokens for sending notifications to specific team topics within a single environment. These keys provide granular control and simplify management. You can create a maximum of 200 keys for Sandbox and 200 for Production, with up to 400 topics per topic-based key.

A topic-specific key can have at most one related key in the same environment. When you connect to the APNs server, you can use authentication tokens from both the topic-based key and its related key (if available) for push notification requests.

> ❗ **Important**:  APNs doesn’t support authentication tokens from multiple developer accounts over a single connection.

##### Obtain an Encryption Key and Key Id From Apple

You need an APNs authentication token signing key to generate the tokens that your server uses. You request this key from your developer account on [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com/account/resources/keys/list), as shown in the following image:

![Creating an authentication token signing key that supports APNs in your developer account.](https://docs-assets.developer.apple.com/published/0f5993178cc36a886c29a80f8178ef21/media-4286508%402x.png)

When you request a key, Apple gives you:

- A 10-character string with the Key ID. You must include this string in your JSON tokens. You can find instructions to get this ID in [`Get a key identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/get-a-key-identifier).
- An authentication token signing key, specified as a text file (with a `.p8` file extension).

Secure both pieces of information carefully. You use the authentication token signing key to encrypt your JSON tokens, so this key must remain private to prevent anyone else from generating those tokens.

> ❗ **Important**:  If you suspect that you may have a compromised authentication token signing key, revoke it and request a new one. (You revoke the key from your developer account on [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com) in the same place where you created it). For maximum security, close all of your existing HTTP/2 connections to APNs and establish new connections before making new requests.

For detailed instructions on how to use an authentication token, see the `authorization` header field in [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md).

##### Create and Encrypt Your Json Token

The token that you include with your notification requests uses the JSON Web Token (JWT) specification. The following table describes the four key-value pairs the token itself contains:

| `alg` | The encryption algorithm you used to encrypt the token. APNs supports only the ES256 algorithm, so set the value of this key to `ES256`. |
| --- | --- |
| `kid` | The 10-character Key ID you obtained from your developer account; see [`Get a key identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/get-a-key-identifier). |
| `iss` | The issuer key, the value for which is the 10-character Team ID you use for developing your company’s apps. Obtain this value from your developer account. |
| `iat` | The “issued at” time, whose value indicates the time when the JSON token generated. Specify the value as the number of seconds since Epoch, in UTC. The value must be no more than one hour from the current time. |

The keys divide between the header and claims payload of the JSON Web Token. The header of the token contains the encryption algorithm and Key ID, and the claims payload contains your Team ID and the token generation time. The code snippet below shows an example of a JSON token for a fictional developer account.

```other
{
   "alg" : "ES256",
   "kid" : "ABC123DEFG"
}
{
   "iss": "DEF123GHIJ",
   "iat": 1437179036
}
```

> ❗ **Important**:  If the value in the `iat` field is more than one hour old, APNs rejects any notifications containing the token, returning an `ExpiredProviderToken` `(403)` error.

Encrypt the resulting JSON data using your authentication token signing key and the specified algorithm. Your provider server must include the resulting encrypted data with all notification requests.

For detailed information about the JWT specification, see [`RFC 7519`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519).

##### Attach Your Token to Notification Requests

When creating the POST request for a notification, include your encrypted token in the `authorization` header of your request. The token is in Base64URL-encoded JWT format, and is specified as `bearer <token data>`, as shown in the following example:

```other
authorization = bearer eyAia2lkIjogIjhZTDNHM1JSWDciIH0.eyAiaXNzIjogIkM4Nk5WOUpYM0QiLCAiaWF0I
		 jogIjE0NTkxNDM1ODA2NTAiIH0.MEYCIQDzqyahmH1rz1s-LFNkylXEa2lZ_aOCX4daxxTZkVEGzwIhALvkClnx5m5eAT6
		 Lxw7LZtEQcH6JENhJTMArwLf3sXwi

```

For information on how to construct your POST requests, see [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md).

##### Refresh Your Token Regularly

For security, APNs requires you to refresh your token regularly. Refresh your token no more than once every 20 minutes and no less than once every 60 minutes. APNs rejects any request whose token contains a timestamp that’s more than one hour old. Similarly, APNs report an error if you use a new token more than once every 20 minutes on the same connection.

On your provider server, set up a recurring task to recreate your token with a current timestamp. Encrypt the token again and attach it to subsequent notification requests.

##### Team and Bundle Id Mapping

You can’t map a connection to APNs to multiple teams. If you manage APNs for multiple developer accounts, open separate connection pools for each of them.

As part of the authentication process, APNs relates a team ID and associated bundle IDs to a connection on the first push. After the authentication process, attempting to associate a different team or sending a push to a newly added bundle ID causes an error. To send remote notifications to a new topic, add the topic to your team in App Store Connect and create new connections to APNs.

For transferred apps, close and recreate any existing connections from your push provider server to APNs. If you don’t, APNs can’t start accepting push requests from the new team.

> ❗ **Important**:  If you use a token from a team-scoped key during the first push, trying to send a push with a topic-specific key or a team-scoped key from a different environment results in an error. After you establish a connection with a topic-specific key for the initial push, using an unrelated topic-specific key, a key from a different environment, a team-scoped key, or sending to a nonassociated topic also results in an error.

## See Also

- [Establishing a certificate-based connection to APNs](establishing-a-certificate-based-connection-to-apns.md)
  Secure your communications with Apple Push Notification service (APNs) by installing a certificate on your provider server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)*