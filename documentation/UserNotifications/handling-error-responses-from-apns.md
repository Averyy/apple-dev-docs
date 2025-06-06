# Handling error responses from Apple Push Notification service

**Framework**: Usernotifications

Respond to the status codes returned by APNs servers.

#### Overview

Apple Push Notification service (APNs) provides a response to each request your server transmits. Each response contains a header with fields indicating the status of the response. If the request succeeded, the body of the response is empty. If an error occurred, the body contains a JSON dictionary with additional information about the error.

##### Interpret Header Responses

The table below describes the meaning of the keys in the header response for a failed request.

| Header name | Value |
| --- | --- |
| `:status` | The HTTP status code. For a failed response the status code can be `4xx` or `5xx`. |
| `apns-request-id` | The same value found in the `apns-request-id` field of the request’s header. If you don’t specify an `apns-request-id` field in your request, APNs creates a new `UUID` and returns it in this header. |

The table below lists the possible values in the `:status` header of the error response.

| Status code | Description |
| --- | --- |
| 400 | A bad request. |
| 403 | There was an error with the certificate or with the provider’s authentication token. |
| 404 | The request contained an invalid `:path` value. |
| 405 | The request used an invalid `:method` value. |
| 413 | The notification payload was too large. |
| 429 | The server received too many requests for the same device token. |
| 500 | An internal server error. |
| 503 | The server is shutting down and unavailable. |

##### Understand Error Codes

The key below is found in the JSON dictionary for unsuccessful requests. The JSON data might also be included in a `GOAWAY` frame when a connection terminates.

| Key | Description |
| --- | --- |
| `reason` | The error code (specified as a string) indicating the reason for the failure. The table below lists possible values. |

During testing, if you find that your test devices aren’t receiving push notifications sent by your provider server, refer to [`Troubleshooting push notifications`](troubleshooting-push-notifications.md) to troubleshoot.

The table below lists the possible error codes included in the reason key of a response’s JSON payload.

| Status code | Error string | Description |
| --- | --- | --- |
| `400` | `FeatureNotEnabled` | The feature isn’t enabled for this topic. Refer to [`Setting up broadcast push notifications`](setting-up-broadcast-push-notifications.md) to enable broadcast capabilities. |
| `400` | `MissingChannelId` | The `apns-channel-id` header is missing. |
| `400` | `BadChannelId` | The `apns-channel-id` header isn’t properly encoded, or it’s greater than the allowed length. |
| `400` | `ChannelNotRegistered` | The `apns-channel-id` header used in the request doesn’t exist. |
| `400` | `BadRequestParams` | The JSON Request payload contained an unrecognizable attribute. |
| `400` | `BadRequestPayload` | The JSON Request payload is unparseable. |
| `400` | `PayloadEmpty` | The push notification request didn’t include a notification payload. |
| `400` | `BadMessageId` | The `apns-id` value is invalid. |
| `400` | `MissingPushType` | The `apns-push-type` attribute is missing. |
| `400` | `InvalidPushType` | The `apns-push-type` attribute is set to an incorrect value. The only allowed value is `LiveActivity`. |
| `400` | `CannotCreateChannelConfig` | You have reached the maximum channel limit for your application. Delete channels that you no longer use. |
| `400` | `BadExpirationDate` | The `apns-expiration header` is an invalid epoch timestamp. For channels with a `No Messages Stored` storage policy, you can only specify a `0` expiration value. |
| `400` | `TopicDisallowed` | The topic is not allowed. Ensure that no push type suffix is added to the bundle ID. |
| `400` | `BadPriority` | The `apns-priority` header is an invalid value. |
| `403` | `BadCertificate` | The certificate is invalid. |
| `403` | `BadCertificateEnvironment` | The client certificate is for the wrong environment. |
| `403` | `TopicMismatch` | The bundle IDs parsed from your token or certificate don’t include the topic present in the path. |
| `403` | `MissingProviderToken` | No certificate or JWT token provided. |
| `403` | `ExpiredProviderToken` | The JWT Token is expired. |
| `403` | `InvalidProviderToken` | The JWT Token is invalid. |
| `404` | `BadPath` | The URL is invalid. Either the `HTTP/2` method or the `HTTP/2` path is incorrect. |
| `405` | `MethodNotAllowed` | The specified `:method` value isn’t allowed. |
| `413` | `PayloadTooLarge` | The message payload is too large. For information about the allowed payload size, refer to [`Sending broadcast push notification requests to APNs`](sending-broadcast-push-notification-requests-to-apns.md). |
| `429` | `TooManyRequests` | The request was throttled because too many requests were received. |
| `429` | `TooManyProviderTokenUpdates` | The provider’s authentication token is being updated too often. Update the authentication token no more than once every 20 minutes. |
| `500` | `InternalServerError` | An unexpected error occurred. |
| `503 ` | `Service Unavailable` | The service is unavailable |
| `503` | `Shutdown` | The server is shutting down and unavailable. |

The following code snippet shows a sample response when an error occurs.

```Other
HEADERS
  - END_STREAM
  + END_HEADERS
  :status = 400
  content-type = application/json
  apns-request-id: <a_UUID>
DATA
  + END_STREAM
  { "reason" : "MissingChannelId" }
```

## See Also

- [Setting up broadcast push notifications](setting-up-broadcast-push-notifications.md)
  Enable broadcast capability for Apple Push Notifications service (APNs).
- [Sending channel management requests to APNs](sending-channel-management-requests-to-apns.md)
  Manage channels that your application uses for broadcast push notifications.
- [Sending broadcast push notification requests to APNs](sending-broadcast-push-notification-requests-to-apns.md)
  Transmit your broadcast notification payload to Apple Push Notifications service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/handling-error-responses-from-apns)*