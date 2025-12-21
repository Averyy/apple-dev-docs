# Handling notification responses from APNs

**Framework**: User Notifications

Respond to the status codes that the APNs servers return.

#### Overview

Apple Push Notification service (APNs) provides a response to each POST request your server transmits. Each response contains a header with fields indicating the status of the response. If the request was successful, the body of the response is empty. If an error occurred, the body contains a JSON dictionary with additional information about the error.

If you find your device is having trouble receiving notifications, refer to [`Troubleshooting push notifications`](troubleshooting-push-notifications.md).

##### Interpret Header Responses

The table below describes the meaning of the keys in the header response.

| Header name | Value |
| --- | --- |
| `apns-id` | The same value found in the `apns-id` field of the request’s header. Use this value to identify the notification. If you don’t specify an `apns-id` field in your request, APNs creates a new UUID and returns it in this header. |
| `:status` | The HTTP status code. |
| `apns-unique-id` | An identifier that is only available in the Development environment. Use this to query Delivery Log information for the corresponding notification in Push Notifications Console. For more information, refer to [`Testing notifications using the Push Notification Console`](testing-notifications-using-the-push-notification-console.md). |

The table below lists the possible values in the `:status` header of the response.

| Status code | Description |
| --- | --- |
| `200` | Success. |
| `400` | Bad request. |
| `403` | There was an error with the certificate or with the provider’s authentication token. |
| `404` | The request contained an invalid `:path` value. |
| `405` | The request used an invalid `:method` value. Only `POST` requests are supported. |
| `410` | The device token is no longer active for the topic. |
| `413` | The notification payload was too large. |
| `429` | The server received too many requests for the same device token. |
| `500` | Internal server error. |
| `503` | The server is shutting down and unavailable. |

##### Understand Error Codes

The table below lists the keys found in the JSON dictionary for unsuccessful requests. The JSON data might also be included in a `GOAWAY` frame when a connection terminates.

| Key | Description |
| --- | --- |
| `reason` | The error code (specified as a string) indicating the reason for the failure. For a list of possible values, refer to the Response error strings table below. |
| `timestamp` | The time, represented in milliseconds since Epoch, at which APNs confirmed the token was no longer valid for the topic. This key is included only when the error in the `:status` field is `410`. |

The table below lists the possible error codes included in the reason key of a response’s JSON payload.

| Status code | Error string | Description |
| --- | --- | --- |
| `400` | `BadCollapseId` | The collapse identifier exceeds the maximum allowed size. |
| `400` | `BadDeviceToken` | The specified device token is invalid. Verify that the request contains a valid token and that the token matches the environment. |
| `400` | `BadExpirationDate` | The `apns-expiration` value is invalid. |
| `400` | `BadMessageId` | The `apns-id` value is invalid. |
| `400` | `BadPriority` | The `apns-priority` value is invalid. |
| `400` | `BadTopic` | The `apns-topic` value is invalid. |
| `400` | `DeviceTokenNotForTopic` | The device token doesn’t match the specified topic. |
| `400` | `DuplicateHeaders` | One or more headers are repeated. |
| `400` | `IdleTimeout` | Idle timeout. |
| `400` | `InvalidPushType` | The `apns-push-type` value is invalid. |
| `400` | `MissingDeviceToken` | The device token isn’t specified in the request `:path`. Verify that the `:path` header contains the device token. |
| `400` | `MissingTopic` | The `apns-topic` header of the request isn’t specified and is required. The `apns-topic` header is mandatory when the client is connected using a certificate that supports multiple topics. |
| `400` | `PayloadEmpty` | The message payload is empty. |
| `400` | `TopicDisallowed` | Pushing to this topic is not allowed. |
| `403` | `BadCertificate` | The certificate is invalid. |
| `403` | `BadCertificateEnvironment` | The client certificate doesn’t match the environment. |
| `403` | `ExpiredProviderToken` | The provider token is stale and a new token should be generated. |
| `403` | `Forbidden` | The specified action is not allowed. |
| `403` | `InvalidProviderToken` | The provider token is not valid, or the token signature can’t be verified. |
| `403` | `MissingProviderToken` | No provider certificate was used to connect to APNs, and the `authorization` header is missing or no provider token is specified. |
| `403` | `UnrelatedKeyIdInToken` | The key ID in the provider token isn’t related to the key ID of the token used in the first push of this connection. To use this token, open a new connection. |
| `403` | `BadEnvironmentKeyIdInToken` | The key ID in the provider token doesn’t match the environment. |
| `404` | `BadPath` | The request contained an invalid `:path` value. |
| `405` | `MethodNotAllowed` | The specified `:method` value isn’t `POST`. |
| `410` | `ExpiredToken` | The device token has expired. |
| `410` | `Unregistered` | The device token is inactive for the specified topic. There is no need to send further pushes to the same device token, unless your application retrieves the same device token, refer to [`Registering your app with APNs`](registering-your-app-with-apns.md) |
| `413` | `PayloadTooLarge` | The message payload is too large. For information about the allowed payload size, refer to Create a POST request to APNs in  [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md). |
| `429` | `TooManyProviderTokenUpdates` | The provider’s authentication token is being updated too often. Update the authentication token no more than once every 20 minutes. |
| `429` | `TooManyRequests` | Too many requests were made consecutively to the same device token. |
| `500` | `InternalServerError` | An internal server error occurred. |
| `503` | `ServiceUnavailable` | The service is unavailable. |
| `503` | `Shutdown` | The APNs server is shutting down. |

After 15 minutes, you can retry JSON payloads that receive response status codes that begin with 5XX. While retrying, you may employ a back-off technique. Most notifications with the status code 4XX can be retried after you fix the error noted in the `reason` field. Don’t retry notification responses with the error code `BadDeviceToken`, `DeviceTokenNotForTopic`, `Forbidden`, `ExpiredToken`, `Unregistered`, or `PayloadTooLarge`. You can retry with a delay, if you get the error code `TooManyRequests`.

> 💡 **Tip**:  An error code beginning with 4XX slows down your ability to send notifications. Refer to the [`Settings`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc9113#name-settings) frame from APNs and adjust your throughput accordingly. APNs disconnects a provider connection with too many error conditions. APNs disconnects sooner with certain error conditions, such as `BadDeviceToken`. Note that status code `410` isn’t considered an error condition.

The code listing below shows a sample response for a successful push request.

```other
HEADERS
  + END_STREAM
  + END_HEADERS
  apns-id = eabeae54-14a8-11e5-b60b-1697f925ec7b
  :status = 200
```

The code listing below shows a sample response when an error occurs.

```other
HEADERS
  - END_STREAM
  + END_HEADERS
  :status = 400
  content-type = application/json
  apns-id: <a_UUID>
DATA
  + END_STREAM
  { "reason" : "BadDeviceToken" }
```

During testing, if you find that your test devices aren’t receiving push notifications sent by your provider server, see, [`Troubleshooting push notifications`](troubleshooting-push-notifications.md) to troubleshoot.

## See Also

- [Sending notification requests to APNs](sending-notification-requests-to-apns.md)
  Transmit your remote notification payload and device token information to Apple Push Notification service (APNs).
- [Viewing the status of push notifications using Metrics and APNs](viewing-the-status-of-push-notifications-using-metrics-and-apns.md)
  Monitor and interpret the status of your push notifications with Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/handling-notification-responses-from-apns)*