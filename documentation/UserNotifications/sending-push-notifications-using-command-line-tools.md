# Sending push notifications using command-line tools

**Framework**: User Notifications

Use basic macOS command-line tools to send push notifications to Apple Push Notification service (APNs).

#### Overview

Testing your APNs connection and configuration by writing a test app can take time. The command-line tools described below provide a quick way to test your setup with APNs in a nonproduction-quality test suite or app.

Before you begin, verify that:

- Your target device is unlocked and connected to the internet.
- Your app is open and in the foreground.

##### Send a Push Notification Using a Certificate

To send a push notification using a certificate, you’ll need:

- A DER-encoded certificate from WWDR to connect to the APNs sandbox. For details on how to set up certificate-based trust with APNs, refer to [`Establishing a certificate-based connection to APNs`](establishing-a-certificate-based-connection-to-apns.md).
- The PEM-encoded private key, without a password, used to generate the above certificate. The Keychain app generates the private key when you create a certificate signing request (CSR). To learn more, refer to [`Create a certificate signing request`](https://developer.apple.comhttps://developer.apple.com/help/account/create-certificates/create-a-certificate-signing-request).
- Your App ID. To learn more about App IDs, refer to [`Register an App ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-id).

Start by launching the Terminal app in the most recent macOS version. Then set these shell variables:

```bash
CERTIFICATE_FILE_NAME=path to the certificate file
CERTIFICATE_KEY_FILE_NAME=path to the private key file
TOPIC=App ID
```

Whether you’re testing a device or a broadcast push notification determines the next set of variables to include.

##### Send a Device Push Notification Using a Certificate

To send a device push notification using a certificate, you’ll need:

- The device token from your app, as a hexadecimal-encoded ASCII string. To learn more about device tokens, refer to [`Registering your app with APNs`](registering-your-app-with-apns.md).

In the Terminal app in the most recent macOS version, set these additional shell variables:

```bash
DEVICE_TOKEN=device token for your app
APNS_HOST_NAME=api.sandbox.push.apple.com
```

Test that you can use your certificate to connect to APNs using this command:

```shell
% openssl s_client 
-connect "${APNS_HOST_NAME}":443 
-cert "${CERTIFICATE_FILE_NAME}" 
-certform DER -key "${CERTIFICATE_KEY_FILE_NAME}" 
-keyform PEM
```

Then send a push notification using this command:

```shell
% curl -v 
  --header "apns-topic: ${TOPIC}" 
  --header "apns-push-type: alert" 
  --cert "${CERTIFICATE_FILE_NAME}" 
  --cert-type DER --key "${CERTIFICATE_KEY_FILE_NAME}" 
  --key-type PEM --data '{"aps":{"alert":"test"}}' 
  --http2  https://${APNS_HOST_NAME}/3/device/${DEVICE_TOKEN}
```

The result is an HTTP status of 200 (request succeeded). A notification with the text “test” appears on your destination device.

##### Send a Broadcast Push Notification Using a Certificate

To send a broadcast push notification using a certificate, you’ll need:

- The channel ID you’re using for the broadcast, as a base64-encoded string. For more information about creating a channel, refer to [`Sending channel management requests to APNs`](sending-channel-management-requests-to-apns.md).
- Ensure the Live Activity is active on the device.

In the Terminal app in the most recent macOS version, set these additional shell variables:

```bash
CHANNEL_ID=channel ID for your application
APNS_HOST_NAME=api.sandbox.push.apple.com 
```

Test that you can use your certificate to connect to APNs using this command:

```shell
% openssl s_client 
   -connect "${APNS_HOST_NAME}":443 
   -cert "${CERTIFICATE_FILE_NAME}" 
   -certform DER 
   -key "${CERTIFICATE_KEY_FILE_NAME}" 
   -keyform PEM
```

Then send a push notification using this command:

```shell
% curl -v 
  --header "apns-channel-id: ${CHANNEL_ID}" 
  --header "apns-push-type: Liveactivity"
  --header "apns-priority: 10" 
  --cert "${CERTIFICATE_FILE_NAME}" 
  --cert-type DER 
  --key "${CERTIFICATE_KEY_FILE_NAME}" 
  --key-type PEM --data '{"aps":{"alert":"test"}}' 
  --http2  https://${APNS_HOST_NAME}/4/broadcasts/apps/${TOPIC}
```

The result is an HTTP status of 200 (request succeeded). Update the data in the curl command based on your Live Activity.

##### Send a Push Notification Using a Json Web Token Jwt

To send a push notification using a JWT, you’ll need:

- Your Team ID. For more information, refer to [`Locate your Team ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-your-team/locate-your-team-id).
- Your key identifier for APNs. For more information, refer to [`Get a key identifier`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/get-a-key-identifier).
- The PEM-encoded private key, without a password, associated with the above key identifier. To learn more about downloading keys, refer to [`Revoke, edit, and download keys`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-keys/revoke-edit-and-download-keys).
- Your App ID. To learn more about App IDs, refer to [`Register an App ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-id).

Start by launching the Terminal app in the most recent macOS version. Then set these shell variables:

```bash
TEAM_ID=Team ID
TOKEN_KEY_FILE_NAME=path to the private key file
AUTH_KEY_ID=your key identifier
TOPIC=App ID
```

Whether you’re testing a device or a broadcast push notification determines the next set of variables to include.

##### Send a Device Push Notification Using a Jwt

To send a device push notification using a JWT, you’ll need:

- The device token from your app, as a hexadecimal-encoded ASCII string. To learn more about device tokens, refer to [`Registering your app with APNs`](registering-your-app-with-apns.md).

In the Terminal app, set these additional shell variables:

```bash
DEVICE_TOKEN=device token for your app
APNS_HOST_NAME=api.sandbox.push.apple.com
```

Test that you can connect to APNs using this command:

```shell
% openssl s_client -connect "${APNS_HOST_NAME}":443
```

Set these additional shell variables just before sending a push notification:

```shell
JWT_ISSUE_TIME=$(date +%s)
JWT_HEADER=$(printf '{ "alg": "ES256", "kid": "%s" }' "${AUTH_KEY_ID}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
JWT_CLAIMS=$(printf '{ "iss": "%s", "iat": %d }' "${TEAM_ID}" "${JWT_ISSUE_TIME}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
JWT_HEADER_CLAIMS="${JWT_HEADER}.${JWT_CLAIMS}"
JWT_SIGNED_HEADER_CLAIMS=$(printf "${JWT_HEADER_CLAIMS}" | openssl dgst -binary -sha256 -sign "${TOKEN_KEY_FILE_NAME}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
AUTHENTICATION_TOKEN="${JWT_HEADER}.${JWT_CLAIMS}.${JWT_SIGNED_HEADER_CLAIMS}"
```

Send the push notification using this command:

```shell
% curl -v 
   --header "apns-topic: $TOPIC" 
   --header "apns-push-type: alert" 
   --header "authorization: bearer $AUTHENTICATION_TOKEN" 
   --data '{"aps":{"alert":"test"}}' 
   --http2 https://${APNS_HOST_NAME}/3/device/${DEVICE_TOKEN}
```

The result is an HTTP status of 200 (request succeeded). A notification with the text “test” appears on your destination device.

##### Send a Broadcast Push Notification Using a Jwt

To send a broadcast push notification using a JWT, you’ll need:

- The channel ID you’re using for the broadcast, as a base64-encoded string. For more information about creating a channel, refer to [`Sending channel management requests to APNs`](sending-channel-management-requests-to-apns.md).
- Ensure the Live Activity is active on the device.

In the Terminal app in the most recent macOS version, set these additional shell variables:

```bash
CHANNEL_ID=channel ID for your application
APNS_HOST_NAME=api.sandbox.push.apple.com
```

Test that you can use your certificate to connect to APNs using this command:

```shell
% openssl s_client -connect "${APNS_HOST_NAME}":443 
```

Set these additional shell variables just before sending a push notification:

```shell
JWT_ISSUE_TIME=$(date +%s)
JWT_HEADER=$(printf '{ "alg": "ES256", "kid": "%s" }' "${AUTH_KEY_ID}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
JWT_CLAIMS=$(printf '{ "iss": "%s", "iat": %d }' "${TEAM_ID}" "${JWT_ISSUE_TIME}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
JWT_HEADER_CLAIMS="${JWT_HEADER}.${JWT_CLAIMS}"
JWT_SIGNED_HEADER_CLAIMS=$(printf "${JWT_HEADER_CLAIMS}" | openssl dgst -binary -sha256 -sign "${TOKEN_KEY_FILE_NAME}" | openssl base64 -e -A | tr -- '+/' '-_' | tr -d =)
AUTHENTICATION_TOKEN="${JWT_HEADER}.${JWT_CLAIMS}.${JWT_SIGNED_HEADER_CLAIMS}"
```

Then send a push notification using this command:

```shell
% curl -v 
   --header "authorization: bearer $AUTHENTICATION_TOKEN" 
   --header "apns-channel-id: ${CHANNEL_ID}" 
   --header "apns-push-type: Liveactivity"
   --header "apns-priority: 10" 
   --data '{"aps":{"alert":"test"}}' 
   --http2  https://${APNS_HOST_NAME}/4/broadcasts/apps/${TOPIC}
```

The result is an HTTP status of 200 (request succeeded). Update the data in the curl command based on your Live Activity.

## See Also

- [Setting up a remote notification server](setting-up-a-remote-notification-server.md)
  Generate notifications and push them to user devices.
- [Testing notifications using the Push Notification Console](testing-notifications-using-the-push-notification-console.md)
  Send test notifications and access delivery logs to test your app’s integration with Apple Push Notification service (APNs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/sending-push-notifications-using-command-line-tools)*