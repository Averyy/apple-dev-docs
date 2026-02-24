# Sending web push notifications in web apps and browsers

**Framework**: User Notifications

Update your web server and website to send push notifications that work in Safari, other browsers, and web apps, following cross-browser standards.

#### Overview

When important, time-sensitive events occur, inform your website users with push notifications you send from your server. To do this, add support for *web push* — push notifications that use the cross-browser Push API, Notifications API, Badging API, and Service Worker standards. For more information on these standards, see [`the W3C document on Push API standards`](https://developer.apple.comhttps://www.w3.org/TR/push-api/). Add web push to Home Screen web apps in iOS 16.4 or later and Webpages in Safari 16 for macOS 13 or later.

To send web push notifications, update your webpage to subscribe users and handle notifications, and update your server to send push notifications. If you’re already sending push notifications with web push for other browsers, confirm that your server fulfills Safari’s requirements so that your existing implementation works for webpages in macOS Safari and web apps. You don’t need to join the Apple Developer Program to send web push notifications.

If you’re already sending push notifications to users in Safari 15 or earlier using [`Safari Push Notifications`](https://developer.apple.comhttps://developer.apple.com/notifications/safari-push-notifications/), continue sending push notifications to those users. Update your webpage with feature detection to use Push API code if it’s available, or Safari Push Notifications code if it isn’t. For more information about best practices while sending a push notification with APNs, see [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md).

##### Enable Push Notifications for Your Webpage or Web App

To enable push notifications, follow this general approach in your webpage or web app:

1. Ask the user for permission to send them push notifications. Provide a method for the user to grant permission with a gesture, such as clicking or tapping a button. When the user completes the gesture, call the push subscription method immediately from the gesture’s event handler code.
2. If the user grants permission, register the provided push notification endpoint and encryption keys from the subscription on your push server with the user’s account.
3. Add a service worker that handles receiving push notifications.
4. Add Notifications API code to display push notifications when the service worker receives them.

Safari doesn’t support invisible push notifications. Present push notifications to the user immediately after your service worker receives them. If you don’t, Safari revokes the push notification permission for your site.

For more information on enabling web push in your webpage, see [`Push API`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Push_API) in Mozilla documentation.

##### Prepare Your Server to Send Push Notifications

Before you add code to send push notifications, make these preparations on your server:

1. Prepare a [`Voluntary Application Server Identification (VAPID)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/draft-ietf-webpush-vapid-00) key pair for your server. You use this to identify your server to the push notification services when you send a push notification.
2. Set up your server to build and encrypt the payload for each push notification.
3. Set up your server to package and send a push notification to a push service according to the [`RFC8030 specification`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc8030).
4. If your network infrastructure limits which URLs your server can access, allow access for `https://*.push.apple.com`.

Your service should maintain TLS encrypted connections to APNs. For more information, see [`Setting up a remote notification server`](setting-up-a-remote-notification-server.md). To send web pushes, your service must use the Server Name Indication (SNI) extension of TLS. For more information, see [`RFC3546`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc3546). APNs supports both HTTP/1.1 and HTTP/2.0. The default protocol is HTTP/1.1. An application server should use the Application-Layer Protocol Negotiation (APLN) extension of TLS to choose between the supported protocols. For more information, see [`RFC7301`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7301).

Then add code to your server to:

- Receive user push notification registrations.
- Store the push notification subscription endpoint and encryption keys together with the user’s account information.
- Determine which users should receive a push notification when important events occur.
- Prepare and send push notifications to the users you identify.

For more information on preparing your server to send push notifications, see [`Push API`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/API/Push_API) in Mozilla documentation.

##### Send Your Notification Request to the Recipients Endpoint

Prepare your push notification request according to the specification. Then send the notification request over HTTP/1.1 or HTTP/2 to the endpoint you stored from the recipient’s push registration.

The push notification service supports HTTP pipelining for HTTP/1.1. Don’t send more than 100 unacknowledged push requests over the connection. There’s a limit of concurrent streams for HTTP/2. Don’t make assumptions about the number of concurrent streams allowed; instead, don’t exceed the SETTINGS_MAX_CONCURRENT_STREAMS value in the HTTP/2 SETTINGS frame.

Include the standard headers with your push notification request:

- **`TTL`**: The number of seconds before your message expires. If the push service can’t deliver a notification immediately, it may store the notification for 30 days or fewer, depending on the value you specify. The push service attempts to deliver the notification the next time the device activates and is available online. If the push service can’t deliver the notification, the push service removes the notification from storage permanently. The number of notifications the push services stores while the device is offline is limited.
- **`Authorization`**: The VAPID JSON web token (JWT) and public key.` `The public key you include must match the public key you provided to `PushManager.subscribe`. Don’t refresh your JWT more frequently than once per hour.
- **`Content-Encoding`**: The name of the encryption method you used to encrypt the payload. If the payload is empty, you may omit this header
- **`Topic`**: Optional identifier that the push service uses to coalesce notifications. Use a maximum of 32 characters from the URL or filename-safe Base64 characters sets.
- **`Urgency`**: Indication of whether to send the notification immediately or prioritize the recipient’s device power considerations for delivery. Provide one of the following values: `very-low`, `low`, `normal`, or `high`. To attempt to deliver the notification immediately, specify `high`.

##### Display Badge Counts for Your Web App

To display badge counts on your web app’s icon, use `navigator.setAppBadge` in your JavaScript to set a badge count. Clear the badge count with `navigator.clearAppBadge`.

Users can configure badging permissions for your Home Screen web app in Notifications settings in iOS 16.4 or later.

##### Review Responses for Push Notification Errors

The push notification service provides a response for each push notification request. Inspect each response to see how the push service handled your push request. The response headers include the HTTP status code and the `apns-id`, which uniquely identifies your push request. The HTTP status code indicates if the request succeeds; if the request fails, the status code identifies the type of error:

| HTTP status code | Description |
| --- | --- |
| 201 | Success. |
| 400 | Bad request. |
| 403 | There’s an error with your authentication. |
| 404 | The request contains an invalid `:path` value. |
| 405 | The request contains an invalid `:method` value. Only use `POST` requests. |
| 410 | The device token has expired. |
| 413 | The notification payload is too large. |
| 429 | The server is receiving too many requests for the same destination. |
| 500 | Internal server error. |
| 503 | The server is shutting down and is unavailable. |

If the push service encounters an error processing your push request, it returns a JSON dictionary response, which includes an error code identified by the `reason` key. Inspect the `reason` code for more details about the cause of the error.

- **`BadTtl`**: The `TTL` header is either missing or isn’t a positive number.
- **`BadUrgency`**: The `Urgency` header is present but isn’t one of the allowed values: `very-low`, `low`, `normal`, `high`.
- **`BadWebPushRequest`**: The request doesn’t conform to the encryption rules.
- **`BadWebPushTopic`**: The `Topic` header is present but doesn’t conform to the specification.
- **`VapidPkHashMismatch`**: The VAPID public key from the push subscription doesn’t match the VAPID public key in the request.
- **`IdleTimeout`**: The connection timed out.
- **`BadAuthorizationHeader`**: The `Authorization` header doesn’t conform to the specification.
- **`BadJwtToken`**: The JSON web token (JWT) has one of following issues: The JWT is missing. The JWT is signed with the wrong private key. The JWT subject claim isn’t a URL or `mailto:`. The JWT audience claim isn’t the origin of the push service where you sent the request. The JWT expiration parameter is more than one day into the future.
- **`BadVapidPublicKey`**: The VAPID public key has one of the following issues: The VAPID public key isn’t present. The VAPID public key is present but not `base64url` encoded. The VAPID public key isn’t the correct type of key.
- **`BadPath`**: The request contained an invalid `:path` value.
- **`MethodNotAllowed`**: The specified `:method` value isn’t `POST`.
- **`PayloadTooLarge`**: The payload size is over the limit of 4 KB.
- **`TooManyRequests`**: The push service received too many consecutive requests to the same device token.
- **`InternalServerError`**: An internal server error occurred.
- **`ServiceUnavailable`**: The service is unavailable.
- **`Shutdown`**: The push server is shutting down.

To resolve an error, address the issue and resend your push notification request. For more information about factors that can impact push notification delivery, refer to [`Interpret data about discarded notifications`](https://developer.apple.comhttps://developer.apple.com/documentation/usernotifications/viewing-the-status-of-push-notifications-using-metrics-and-apns#Interpret-data-about-discarded-notifications). For more information about APNs service and storage details, see [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers)*