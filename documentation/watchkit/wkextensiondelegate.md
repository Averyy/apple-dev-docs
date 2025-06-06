# WKExtensionDelegate

**Framework**: Watchkit  
**Kind**: protocol

A collection of methods that manages the app-level behavior of a WatchKit extension.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
protocol WKExtensionDelegate : NSObjectProtocol
```

#### Overview

Implement the delegate’s methods to respond to your app’s life-cycle events, such as the activation and deactivation of your app. You can also implement delegate methods to respond to background tasks, Siri intents, workout sessions, or Handoff activity from another devices.

WatchKit creates your delegate object automatically by instantiating the class assigned to the [`WKExtensionDelegateClassName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKExtensionDelegateClassName) key in your WatchKit extension’s `Info.plist` file. By default, this class is named ExtensionDelegate. The system then assigns the delegate object to the [`delegate`](wkextension/delegate.md) property of the shared [`WKExtension`](wkextension.md) object.

## Topics

### Monitoring state changes
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](wkextensiondelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](wkextensiondelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkextensiondelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkextensiondelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](wkextensiondelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.
### Responding to intents
- [func handle(INIntent, completionHandler: (INIntentResponse) -> Void)](wkextensiondelegate/handle(_:completionhandler:).md)
  Responds to a Siri intent.
### Setup Now Playing interface
- [func handleRemoteNowPlayingActivity()](wkextensiondelegate/handleremotenowplayingactivity.md)
  Tells the delegate when the user plays audio in the corresponding iOS app.
### Handling a workout session
- [func handle(HKWorkoutConfiguration)](wkextensiondelegate/handle(_:)-f27i.md)
  Tells the delegate that the user started a workout session on the paired iPhone.
- [func handleActiveWorkoutRecovery()](wkextensiondelegate/handleactiveworkoutrecovery.md)
  Tells the delegate when the app relaunches after crashing during an active workout session.
### Handling background tasks
- [func handle(Set<WKRefreshBackgroundTask>)](wkextensiondelegate/handle(_:)-92ulv.md)
  Tells the delegate that the app has received one or more background tasks.
### Handling extended runtime sessions
- [func handle(WKExtendedRuntimeSession)](wkextensiondelegate/handle(_:)-4qxgv.md)
  Tells the delegate that the system launched your app to resume an extended runtime session.
### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:).md)
  Tells the delegate that Apple Push Notification service (APNs) cannot successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](wkextensiondelegate/didreceiveremotenotification(_:fetchcompletionhandler:).md)
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md)
  The result of an attempt to download the content associated with a remote notification.
### Coordinating handoff activity
- [func handleUserActivity([AnyHashable : Any]?)](wkextensiondelegate/handleuseractivity(_:).md)
  Responds to Handoff–related activity from complications and notifications.
- [func handle(NSUserActivity)](wkextensiondelegate/handle(_:)-5pyj1.md)
  Responds to Handoff–related activity from Siri.
### Accepting CloudKit shares
- [func userDidAcceptCloudKitShare(with: CKShareMetadata)](wkextensiondelegate/userdidacceptcloudkitshare(with:).md)
  Tells the delegate that the app has access to shared information in CloudKit.
### Deprecated Methods
- [func didReceiveRemoteNotification([AnyHashable : Any])](wkextensiondelegate/didreceiveremotenotification(_:).md)
  Tells the delegate that a remote notification arrived.
- [func didReceive(UILocalNotification)](wkextensiondelegate/didreceive(_:).md)
  Tells the delegate that a local notification was triggered.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:forremotenotification:).md)
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:).md)
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](wkextensiondelegate/handleaction(withidentifier:for:).md)
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:).md)
  Delivers a local notification payload and user response information to the app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](wkapplication.md)
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md)
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md)
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [class WKInterfaceDevice](wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](../BundleResources/Information-Property-List/WKPrefersNetworkUponForeground.md)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate)*