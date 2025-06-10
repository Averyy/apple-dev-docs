# Troubleshooting push notifications

**Framework**: User Notifications

Debug your server to send push notifications with device and broadcast push notifications.

#### Overview

When encountering issues where test devices fail to receive push notifications from the provider server, troubleshooting becomes essential to ensure the functionality of your app’s notification system. Verify that you aren’t spamming the device. If you send too many notifications to the same device within a short timespan, APNs may treat it as a denial-of-service attack and temporarily block your server from sending notifications. Check to refer to if silent notifications are being throttled. APNs sends a limited number of silent notifications with the `content-available` key. In addition, if the device has already exceeded its power budget for the day, silent notifications aren’t sent again until the power budget resets, which happens once a day. These limits are disabled when testing your app from Xcode. For more information, refer to [`Pushing background updates to your App`](pushing-background-updates-to-your-app.md).

Make sure you have the necessary certificates installed on your provider server. If your provider server doesn’t have the proper certificates for TLS/SSL validation, it can’t connect to APNs. For certificate-based connections, your provider server also needs the certificate you obtained from Apple. For more information, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).

Check how often your provider server connects to APNs. If your provider server opens and closes its connection to APNs repeatedly, APNs may treat it as a denial-of-service attack and temporarily block your server from connecting.

Depending on whether you are troubleshooting issues with device or broadcast notifications, there are different areas you can verify to fix your connection with APNs.

You can verify the TLS handshake between your provider server and APNs by running the OpenSSL `s_client` command from your server, as in code snippet below.. This command can also show if your TLS/SSL certificates have expired or been revoked.

```other
$ openssl s_client -connect api-broadcast.push.apple.com:443 -cert YourSSLCertAndPrivateKey.pem -debug 
-showcerts -CAfile server-ca-cert.pem
```

##### Troubleshoot Receiving Device Push Notifications

If your test devices aren’t receiving notifications sent by your provider server, examine the following possible causes:

-  Each time your app launches, it needs to request its current token and forward that token to your provider server. Implement the appropriate failure handler methods to determine if APNs reported an error. For more information, refer to [`Registering your app with APNs`](registering-your-app-with-apns.md).
-  When failures occur, APNs reports an appropriate error back to your provider server. Use the error code to decide the proper action that makes sense for your app.
-  This key is required starting in watchOS 6. The absence of this key may delay the delivery of notifications, or prevent their delivery altogether. See .
-  APNs queues only one notification at a time for each device, and the device must acknowledge receipt of the notification before APNs dequeues it. If you send multiple notification requests in a very short period of time, each new request might overwrite the previous request.
-  To send notifications, your provider server must allow inbound and outbound TCP packets over port 443 for HTTP/2 connections, or port 2195 when using the binary interface. Devices connecting to APNs over Wi-Fi need to allow inbound and outbound TCP packets over port 5223, falling back to port 443 if port 5223 is unavailable.

##### Troubleshoot Receiving Broadcast Push Notifications

During testing, if you find that your test devices aren’t receiving notifications sent by your provider server, examine the following possible causes:

-  The bundle ID string you use in the `:path` needs to exactly match your app’s bundle ID. The string can’t include a suffix, such as `.push-type.liveactivity`.
-  Make sure that your provider server uses a valid channel ID for your channel.
-  When failures occur, APNs reports an appropriate error back to your provider server. Use the error code to decide the proper action that makes sense for your app.
-  To send notifications, your provider server allows inbound and outbound TCP packets over port 443 for HTTP/2 connections. Devices connecting to APNs over Wi-Fi need to allow inbound and outbound TCP packets over port 5223, falling back to port 443 if port 5223 is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/troubleshooting-push-notifications)*