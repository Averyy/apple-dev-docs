# Registering your app with APNs

**Framework**: Usernotifications

Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.

#### Overview

Apple Push Notification service (APNs) must know the address of a user’s device before it can send notifications to that device. This address takes the form of a device token unique to both the device and your app. At launch time, your app communicates with APNs and receives its device token, which you then forward to your provider server. Your server includes that token with any notifications it sends.

> **Note**:  You can’t use the same device token for more than one app, even when the apps are on the same device. Every app must request their own unique device token and forward it to your provider server.

##### Enable the Push Notifications Capability

To add the required entitlements to your app, enable the Push Notifications capability in your Xcode project, as shown in . Enabling this option in iOS adds the [`APS Environment Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/aps-environment) to the app. In macOS, it adds the [`APS Environment (macOS) Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.aps-environment). See [`Enable push notifications`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devdfd3d04a1) in Xcode help for more information.

![Add entitlements to your Xcode project by enabling the push notification capability in the Capabilities tab.](https://docs-assets.developer.apple.com/published/d01d47767d5a70a20a63bb93bcd68aee/media-4321361%402x.png)

> ❗ **Important**:  In your developer account, enable the push notification service for the App ID assigned to your project. For more information about configuring your developer account, go to your [`Developer Account`](https://developer.apple.comhttps://developer.apple.com/account/#/overview/) page.

##### Register Your App and Retrieve Your Apps Device Token

Register your app with APNs and receive a globally unique device token, which is effectively the address of your app on the current device. Your provider server must have this token before it can deliver notifications to the device.

You register your app and receive your device token each time your app launches using Apple-provided APIs. The registration process is similar across platforms:

- In iOS and tvOS, call the [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/UIKit/UIApplication/registerForRemoteNotifications()) method of [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) to request the device token. Upon successful registration, you receive the token in your app delegate’s [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didRegisterForRemoteNotificationsWithDeviceToken:)) method.
- In macOS, call the [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/AppKit/NSApplication/registerForRemoteNotifications()) method of [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) to request the device token. Upon successful registration, you receive the token in your app delegate’s [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:didRegisterForRemoteNotificationsWithDeviceToken:)) method.
- In watchOS, call the [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/WatchKit/WKApplication/registerForRemoteNotifications()) method of [`WKExtension`](https://developer.apple.com/documentation/WatchKit/WKExtension) to request the device token. Upon successful registration, you receive the token in your extension delegate’s [`didRegisterForRemoteNotifications(withDeviceToken:)`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate/didRegisterForRemoteNotifications(withDeviceToken:)) method.

In addition to handling successful registrations with APNs, prepare your app to handle unsuccessful registrations by implementing the [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFailToRegisterForRemoteNotificationsWithError:)) method. Registration might fail if the user’s device isn’t connected to the network, if the APNs server is unreachable for any reason, or if the app doesn’t have the proper code-signing entitlement. When a failure occurs, set a flag and try to register again at a later time.

Listing 1 shows a sample implementation of the iOS app delegate methods needed to register for remote notifications and receive the corresponding token. The `sendDeviceTokenToServer` method is a custom method that the app uses to send the data to its provider server.

Listing 1. Communicating with APNs at launch time

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Override point for customization after application launch.
    UIApplication.shared.registerForRemoteNotifications()
    return true
}

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    self.sendDeviceTokenToServer(data: deviceToken)
}

func application(_ application: UIApplication,
                 didFailToRegisterForRemoteNotificationsWithError
                 error: Error) {
    // Try again later.
}
```

> ❗ **Important**:  Never cache device tokens in local storage. APNs issues a new token when the user restores a device from a backup, when the user installs your app on a new device, and when the user reinstalls the operating system. You get an up-to-date token each time you ask the system to provide the token.

##### Forward Tokens to Your Provider Server

Upon receiving a device token, open a network connection from your app to your provider server. Securely forward the device token and any other information you need to identify the specific user to your server. For example, you might include the user’s login name or something that connects them to your service. Encrypt any information you send over the network.

On your provider server, store tokens in a secure place where you can access them to send notifications. When generating notifications, your server must be able to send notifications to specific devices. So, if you have notifications linked to a user’s account, store device tokens with the user’s account information. Because a user can have multiple devices, prepare your app to handle multiple device tokens.

For information about how to send payloads and device tokens to APNs, see [`Sending notification requests to APNs`](sending-notification-requests-to-apns.md).

## See Also

- [Generating a remote notification](generating-a-remote-notification.md)
  Send notifications to the user’s device with a JSON payload.
- [Pushing background updates to your App](pushing-background-updates-to-your-app.md)
  Deliver notifications that wake your app and update it in the background.
- [Establishing a connection to Apple Push Notification service (APNs)](establishing-a-connection-to-apns.md)
  Secure your communications with APNs to send API requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns)*