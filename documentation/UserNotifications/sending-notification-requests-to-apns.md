# Sending notification requests to APNs

**Framework**: Usernotifications

Transmit your remote notification payload and device token information to Apple Push Notification service (APNs).

#### Overview

As a best-effort service, APNs may reorder notifications you send to the same device token. If APNs can’t deliver a notification immediately, it may store the notification for 30 days or less, depending on the date you specify in the `apns-expiration` header. APNs attempts to deliver the notification the next time the device activates and is available online.

APNs stores only one notification per bundle ID. When you send multiple notifications to the same device for a bundle ID, APNs selects only one notification to store in a non-deterministic way. Notifications with `apns-priority` `5` and `1` might get grouped and delivered in bursts to the user’s device. Your notifications may also get throttled, saved in storage, and in some cases, not delivered. The way the user interacts with your application and the power state of the device determines the exact behavior. For more information about the factors that impact the delivery of a push notification, refer to [`Viewing the status of push notifications using Metrics and APNs`](viewing-the-status-of-push-notifications-using-metrics-and-apns.md).

When you have a notification to send to a user, your provider must construct a POST request and send it to Apple Push Notification service (APNs). Upon receiving your server’s POST request, APNs validates the request using either the provided authentication token or your server’s certificate. If validation succeeds, APNs uses the provided device token to identify the user’s device. It then tries to send your JSON payload to that device. For information on sending test notifications without setting up the environment, refer to [`Testing notifications using the Push Notification Console`](testing-notifications-using-the-push-notification-console.md).

##### Establish a Connection to Apns

Use HTTP/2 and TLS 1.2 or later to establish a connection between your provider server and one of the following servers:

- Development server: [`api.sandbox.push.apple.com:443`](https://developer.apple.comhttps://api.sandbox.push.apple.com:443)
- Production server: [`api.push.apple.com:443`](https://developer.apple.comhttps://api.push.apple.com:443)

Use the production server for your shipping apps and the development server for testing. When sending many remote notifications, you can establish multiple connections to these servers to improve performance.

> 💡 **Tip**:  You can also use port 2197 (instead of port 443) on either server when communicating with APNs. You might use this port to allow APNs traffic through your firewall but to block other HTTPS traffic.

 You can also use port 2197 (instead of port 443) on either server when communicating with APNs. You might use this port to allow APNs traffic through your firewall but to block other HTTPS traffic.

APNs allows multiple concurrent streams for each connection, but don’t assume a specific number of streams. The exact number varies based on server load and whether you use a provider certificate or an authentication token. For example, when using an authentication token, APNs allows only one stream until you post a request with a valid authentication token. APNs ignores `HTTP/2 PRIORITY` frames, so don’t send them on your streams.

If you experience a revoked provider certificate, or if you revoke your authentication token, close all connections to APNs, fix the problem, and then open new connections. APNs may also terminate a connection by sending a `GOAWAY` frame. The payload of the `GOAWAY` frame includes JSON data with a `reason` key, indicating the reason for the connection termination. For a list of values for the `reason` key, refer to the response error strings in [`Handling notification responses from APNs`](handling-notification-responses-from-apns.md).

##### Create a Post Request to Apns

To send a notification to a user’s device, construct and send a POST notification to APNs. Send this request over the connection you created using HTTP/2 and TLS. To create your POST notification, you must already have the following pieces of information:

- The device token that identifies the user device to receive the notification; refer to [`Registering your app with APNs`](registering-your-app-with-apns.md).
- Your current authentication token (only if you’re using token-based authentication); refer to [`Establishing a token-based connection to APNs`](establishing-a-token-based-connection-to-apns.md).
- The notification’s payload, specified as JSON data; refer to [`Generating a remote notification`](generating-a-remote-notification.md).

> **Note**:  If you’re using certificate-based authentication, you send your provider certificate to APNs when setting up your TLS connection. For more information, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).

 If you’re using certificate-based authentication, you send your provider certificate to APNs when setting up your TLS connection. For more information, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).

##### Send a Post Request to Apns

To deliver the notifications, you’re required to have some header fields. In addition to the preceding data, add the following header fields in to your request. Other headers are optional or may depend on whether you’re using token-based or certificate-based authentication.

| Header field | Required | Description |
| --- | --- | --- |
| `:method` | Required | The value `POST`. |
| `:path` | Required | The path to the device token. The value of this header is `/3/device/<device_token>`, where `<device_token>` is the hexadecimal bytes that identify the user’s device. Your app receives the bytes for this device token when registering for remote notifications. For more information, refer to [`Registering your app with APNs`](registering-your-app-with-apns.md). |
| `authorization` | Required for token-based authentication | The value of this header is `bearer <provider_token>`, where `<provider_token>` is the encrypted token that authorizes you to send notifications for the specified topic. APNs ignores this header if you use certificate-based authentication. For more information, refer to [`Establishing a token-based connection to APNs`](establishing-a-token-based-connection-to-apns.md). |
| `apns-push-type` | Required for watchOS 6 and later; recommended for macOS, iOS, tvOS, and iPadOS | The value of this header must accurately reflect the contents of your notification’s payload. If there’s a mismatch, or if the header is missing on required systems, APNs may return an error, delay the delivery of the notification, or drop it altogether. |
| `apns-id` | Optional | A canonical UUID that’s the unique ID for the notification. If an error occurs when sending the notification, APNs includes this value when reporting the error to your server. Canonical UUIDs are 32 lowercase hexadecimal digits, displayed in five groups separated by hyphens in the form 8-4-4-4-12. For example: `123e4567-e89b-12d3-a456-4266554400a0`. If you omit this header, APNs creates a UUID for you and returns it in its response. |
| `apns-expiration` | Optional | The date at which the notification is no longer valid. This value is a UNIX epoch expressed in seconds (UTC). If the value is nonzero, APNs stores the notification and tries to deliver it at least once, repeating the attempt as needed until the specified date. If the value is `0`, APNs attempts to deliver the notification only once and doesn’t store it. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) A single APNs attempt may involve retries over multiple network interfaces and connections of the destination device. Often these retries span over some time period, depending on the network characteristics. In addition, a push notification may take some time on the network after APNs sends it to the device. APNs uses best efforts to honor the expiry date without any guarantee. If the value is nonzero, the notification may deliver after the specified timestamp. If the value is `0`, the notification may deliver with some delay. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If you omit this header, APNs stores the push according to APNs storage policy. For more information, refer to [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md). |
| `apns-priority` | Optional | The priority of the notification. If you omit this header, APNs sets the notification priority to `10`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Specify `10` to send the notification immediately. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Specify `5` to send the notification based on power considerations on the user’s device. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Specify 1 to prioritize the device’s power considerations over all other factors for delivery, and prevent awakening the device. |
| `apns-topic` | Required | The topic for the notification. In general, the topic is your app’s bundle ID/app ID. It can have a suffix based on the type of push notification. To learn more about app ID, refer to [`Register an App ID`](https://developer.apple.comhttps://help.apple.com/developer-account/#/dev1b35d6f83). See more details on push type below. |
| `apns-collapse-id` | Optional | An identifier you use to merge multiple notifications into a single notification for the user. Typically, each notification request displays a new notification on the user’s device. When sending the same notification more than once, use the same value in this header to merge the requests. The value of this key must not exceed 64 bytes. |

APNs requires the use of HPACK (header compression for HTTP/2), which prevents repeatedly storing header keys and values. APNs maintains a small dynamic table for HPACK. To avoid filling up that table, encode your headers in the following way—especially when using many streams:

- Encode the `:path` and `authorization` values as .
- Encode the `apns-id`, `apns-expiration`, and `apns-collapse-id` values differently based on whether this is an initial or subsequent request.
- The first time you send these headers, encode them with  to add the header fields to the dynamic table.
- For subsequent requests, encode these headers as .
- Encode all other fields as literal header fields with .

Put the JSON payload with the notification’s content into the body of your request. You must not use a compressed JSON payload, and it’s limited to a maximum size of 4 KB (4096 bytes). The maxiumum size for a Voice over Internet Protocol (VoIP) notification is 5 KB (5120 bytes).

The code snippet below shows a sample request constructed with an authentication token.

```other
HEADERS
  - END_STREAM
  + END_HEADERS
  :method = POST
  :scheme = https
  :path = /3/device/00fc13adff785122b4ad28809a3420982341241421348097878e577c991de8f0
  host = api.sandbox.push.apple.com
  authorization = bearer eyAia2lkIjogIjhZTDNHM1JSWDciIH0.eyAiaXNzIjogIkM4Nk5WOUpYM0QiLCAiaWF0I
		 jogIjE0NTkxNDM1ODA2NTAiIH0.MEYCIQDzqyahmH1rz1s-LFNkylXEa2lZ_aOCX4daxxTZkVEGzwIhALvkClnx5m5eAT6
		 Lxw7LZtEQcH6JENhJTMArwLf3sXwi
  apns-id = eabeae54-14a8-11e5-b60b-1697f925ec7b
  apns-push-type = alert
  apns-expiration = 0
  apns-priority = 10
  apns-topic = com.example.MyApp
DATA
  + END_STREAM
  { "aps" : { "alert" : "Hello" } }

```

The code snippet below shows a sample request constructed for use with a certificate. APNs uses the app’s bundle ID as the default topic.

```other
HEADERS
  - END_STREAM
  + END_HEADERS
  :method = POST
  :scheme = https
  :path = /3/device/00fc13adff785122b4ad28809a3420982341241421348097878e577c991de8f0
  host = api.sandbox.push.apple.com
  apns-id = eabeae54-14a8-11e5-b60b-1697f925ec7b
  apns-push-type = alert
  apns-expiration = 0
  apns-priority = 10
DATA
  + END_STREAM
  { "aps" : { "alert" : "Hello" } }

```

##### Know When to Use Push Types

The `apns-push-type` header field has the following valid values. The descriptions below describe when and how to use these values. Send an `apns-push-type` header with each push. Recent and upcoming features may not work if this header is missing. See the table above to determine if this header is required or optional.

Certificate-based connection supports only a subset of push types and token-based connection supports all push-types. For more information, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md). Check Extension 1.2.840.113635.100.6.3.6 and 1.2.840.113635.100.6.3.4 of your push certificate. These extensions list all the push topics allowed for your certificate. If a push topic for a specific push type isn’t listed, you can’t use the certificate to send a notification of that push type.

##### Follow Best Practices While Sending Push Notifications with Apns

Below are some APNs best practices to consider:

- Make an uncached DNS query to resolve the APNs server name, before each connection. This helps distribute push traffic from all providers across all APNs servers.
- Avoid push bursts over selective connections. Diversifying push traffic over many connections distributes push traffic for your application across all APNs servers.
- Reuse a connection as long as possible. In most cases, you can reuse a connection for many hours to days. If your connection is mostly idle, you may send a HTTP2 PING frame after an hour of inactivity. Reusing a connection often results in less bandwidth and CPU consumption.
- Create a unique value for the `apns-id` header to track your push notification. If you don’t provide one, APNs creates one and returns it as part of the response. Record this UUID to assist with debugging.
- Pay attention to status returned by APNs for each push and take appropriate action for your application. For more information, refer to [`Handling notification responses from APNs`](handling-notification-responses-from-apns.md).
- If you’re using a certificate to connect to APNs, remember to get a new certificate and deploy it with your service before the expiry of the current certificate.
- Don’t make assumptions about device token size.

> **Note**:  APNs doesn’t support legacy binary protocol as of March 31, 2021. Update to the HTTP/2-based API as soon as possible.

 APNs doesn’t support legacy binary protocol as of March 31, 2021. Update to the HTTP/2-based API as soon as possible.

## See Also

- [Handling notification responses from APNs](handling-notification-responses-from-apns.md)
  Respond to the status codes that the APNs servers return.
- [Viewing the status of push notifications using Metrics and APNs](viewing-the-status-of-push-notifications-using-metrics-and-apns.md)
  Monitor and interpret the status of your push notifications with Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns)*