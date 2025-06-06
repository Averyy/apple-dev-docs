# Establishing a connection to Apple Push Notification service (APNs)

**Framework**: Usernotifications

Secure your communications with APNs to send API requests.

#### Overview

Use `HTTP/2` and `TLS 1.2` or later to establish a connection between your provider server and APNs server to send API requests. Based on the type of request you’re using, there’s a different development and production endpoint. If you’re shipping apps, use the production end points. If you’re testing, use the development endpoints. If you’re sending many remote notifications, you can establish multiple connections to these servers to improve performance.

APNs allows for multiple concurrent streams for each connection, but don’t assume a specific number of streams. The exact number varies based on server load and whether you use a provider certificate or an authentication token. For example, if you’re using an `authentication` token, APNs allows only one stream until you post a request with a valid `authentication` token. APNs ignores `HTTP/2 PRIORITY` frames, so don’t send them on your streams.

If you experience a revoked provider certificate, or if you revoke your authentication token, close all connections to APNs, fix the problem, and then open new connections. APNs may also terminate a connection by sending a `GOAWAY` frame. The payload of the `GOAWAY` frame includes `JSON` data with a `reason` key, indicating the reason for the connection termination. For a list of values for the `reason` key, refer to the response error strings in [`Handling notification responses from APNs`](handling-notification-responses-from-apns.md).

##### Create a Request to Apns

To send a notification to a person’s device, construct and send a POST notification to APNs. Send this request over the connection you created using `HTTP/2` and `TLS`. To create your POST notification, you must already have the following pieces of information:

- If you’re using device push, the device token that identifies the device to receive the notification; refer to [`Registering your app with APNs`](registering-your-app-with-apns.md).
- If you’re using token-based authentication, your current authentication token; refer to [`Establishing a token-based connection to APNs`](establishing-a-token-based-connection-to-apns.md).
- The notification’s payload, specified as JSON data; refer to [`Generating a remote notification`](generating-a-remote-notification.md).
- If you’re using certificate-based authentication, your provider certificate. You send your provider certificate to APNs when setting up your `TLS` connection. For more information, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).

> **Note**: Depending on the connection you’re establishing with APNs, each request has a different path and header requirement.

Depending on the connection you’re establishing with APNs, each request has a different path and header requirement.

##### Send a Request to Apns

APNs requires the use of HPACK (header compression for HTTP/2), which prevents repeatedly storing header keys and values. APNs maintains a small dynamic table for HPACK. To avoid filling up that table, encode your headers in the following way—especially when using many streams:

- The first time you send an APNs documented header name, encode them with incremental indexing and add the header fields to the dynamic table. Reuse the indexed header name for subsequent requests.
- Index and reuse an APNs documented header value that doesn’t change frequently for your use-case.

If you are using token-based authentication, the `authorization` header value shouldn’t change frequently and can be indexed. If you are using separate connections for different push types, `apns-push-type` header value can also be indexed and reused. If you are using broadcast push notifications, the channel ID used for push notifications might not change often and can be indexed.

##### Troubleshoot Problems with Connecting to Apns

If your provider server is unable to connect to APNs, examine the following possible causes:

- Make sure you have the needed certificates installed on your provider server. If your provider server doesn’t have the proper certificates for `TLS/SS`L validation, it cannot connect to APNs. For certificate-based connections, your provider server must also have the certificate you obtained from Apple. Refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).
- Check how often your provider server connects to APNs. If your provider server opens and closes its connection to APNs repeatedly, APNs may treat it as a denial-of-service attack and temporarily block your server from connecting.

You can verify the TLS handshake between your provider server and APNs by running the `OpenSSL s_client` command from your server, as shown below. This command can also show if your `TLS/SSL` certificates are expired or revoked.

The code listing below verifies the `TLS` handshake with device push notifications sandbox endpoint

```Other
$ openssl s_client -connect api.development.push.apple.com:443 -cert YourSSLCertAndPrivateKey.pem -debug 
-showcerts -CAfile server-ca-cert.pem
```

## See Also

- [Registering your app with APNs](registering-your-app-with-apns.md)
  Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.
- [Generating a remote notification](generating-a-remote-notification.md)
  Send notifications to the user’s device with a JSON payload.
- [Pushing background updates to your App](pushing-background-updates-to-your-app.md)
  Deliver notifications that wake your app and update it in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/establishing-a-connection-to-apns)*