# requestAuthorization(options:completionHandler:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

Requests a person’s authorization to allow local and remote notifications for your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func requestAuthorization(options: UNAuthorizationOptions = [], completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func requestAuthorization(options: UNAuthorizationOptions = []) async throws -> Bool
```

```objc
- (void) requestAuthorizationWithOptions:(UNAuthorizationOptions) options completionHandler:(void (^)(BOOL granted, NSError *error)) completionHandler;
```

## Mentions

- [Asking permission to use notifications](../asking-permission-to-use-notifications.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestAuthorization(options: UNAuthorizationOptions = []) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

If your app’s local or remote notifications involve user interactions, you must request authorization for the system to perform those interactions on your app’s behalf. Interactions include displaying an alert, playing a sound, or badging the app’s icon.

> **Note**:  Always call this method before scheduling any local notifications and before registering with the Apple Push Notification service. Do this in a context that helps people understand why your app needs authorization, as described in [Asking permission to use notifications](../asking-permission-to-use-notifications.md).

The first time your app calls the method, the system prompts the person to authorize the requested interactions. The person may grant or deny authorization, and the system stores the person’s response. Subsequent calls to this method don’t prompt the person again. After determining the authorization status, the user notification center object executes the block in the `completionHandler` parameter. Use that block to make any adjustments to your app’s behavior. For example, if the person denied authorization, you might notify a remote notification server not to send notifications to the user’s device.

The person may change the interactions they allow at any time in system settings. Use the [`getNotificationSettings(completionHandler:)`](./getnotificationsettings%28completionhandler%29.md) method to determine what interactions are allowed for your app.

```swift
let center = UNUserNotificationCenter.current()
do {
     if try await center.requestAuthorization(options: [.badge, .sound, .alert]) == true {
          // You have authorization.
     } else {
          // You don't have authorization.
     }
} catch {
     // Handle any errors.
}
```

## Parameters

- `options`: The authorization options your app is requesting. You may combine the available constants to request authorization for multiple items. Request only the authorization options that you plan to use. For a list of possible values, see [`UNAuthorizationOptions`](../unauthorizationoptions.md).
- `completionHandler`: The block to execute asynchronously with the results. This block may execute on a background thread. The block has no return value and has the following parameters:

  - **granted**: A Boolean value indicating whether the person grants authorization. The value of this parameter is [`true`](../../Swift/true.md) when the person grants authorization for one or more options. The value is [`false`](../../Swift/false.md) when the person denies authorization or authorization is  undetermined. Use [`getNotificationSettings(completionHandler:)`](./getnotificationsettings%28completionhandler%29.md) to check the authorization status.
  - **error**: An object containing error information or `nil` if no error occurs.

## See Also

### Requesting authorization
- [struct UNAuthorizationOptions](../unauthorizationoptions.md)
  Options that determine the authorized features of local and remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/requestauthorization(options:completionhandler:))*