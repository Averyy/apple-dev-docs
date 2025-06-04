# WKExtensionDelegate

**Framework**: WatchKit  
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

WatchKit creates your delegate object automatically by instantiating the class assigned to the [`WKExtensionDelegateClassName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKExtensionDelegateClassName) key in your WatchKit extension’s `Info.plist` file. By default, this class is named ExtensionDelegate. The system then assigns the delegate object to the [`delegate`](https://developer.apple.com/documentation/watchkit/wkextension/delegate) property of the shared [`WKExtension`](https://developer.apple.com/documentation/watchkit/wkextension) object.

## Topics

### Monitoring state changes
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()))
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()))
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()))
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()))
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()))
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange()))
  Tells the delegate that the device’s orientation has changed.
### Responding to intents
- [func handle(INIntent, completionHandler: (INIntentResponse) -> Void)](handle(_:completionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:completionhandler:)))
  Responds to a Siri intent.
### Setup Now Playing interface
- [func handleRemoteNowPlayingActivity()](handleremotenowplayingactivity().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleremotenowplayingactivity()))
  Tells the delegate when the user plays audio in the corresponding iOS app.
### Handling a workout session
- [func handle(HKWorkoutConfiguration)](handle(_:)-f27i.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-f27i))
  Tells the delegate that the user started a workout session on the paired iPhone.
- [func handleActiveWorkoutRecovery()](handleactiveworkoutrecovery().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleactiveworkoutrecovery()))
  Tells the delegate when the app relaunches after crashing during an active workout session.
### Handling background tasks
- [func handle(Set<WKRefreshBackgroundTask>)](handle(_:)-92ulv.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-92ulv))
  Tells the delegate that the app has received one or more background tasks.
### Handling extended runtime sessions
- [func handle(WKExtendedRuntimeSession)](handle(_:)-4qxgv.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv))
  Tells the delegate that the system launched your app to resume an extended runtime session.
### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](didregisterforremotenotifications(withdevicetoken:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didregisterforremotenotifications(withdevicetoken:)))
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](didfailtoregisterforremotenotificationswitherror(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didfailtoregisterforremotenotificationswitherror(_:)))
  Tells the delegate that Apple Push Notification service (APNs) cannot successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](didreceiveremotenotification(_:fetchcompletionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:fetchcompletionhandler:)))
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult))
  The result of an attempt to download the content associated with a remote notification.
### Coordinating handoff activity
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleuseractivity(_:)))
  Responds to Handoff–related activity from complications and notifications.
- [func handle(NSUserActivity)](handle(_:)-5pyj1.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-5pyj1))
  Responds to Handoff–related activity from Siri.
### Accepting CloudKit shares
- [func userDidAcceptCloudKitShare(with: CKShareMetadata)](userdidacceptcloudkitshare(with:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/userdidacceptcloudkitshare(with:)))
  Tells the delegate that the app has access to shared information in CloudKit.
### Deprecated Methods
- [func didReceiveRemoteNotification([AnyHashable : Any])](didreceiveremotenotification(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceiveremotenotification(_:)))
  Tells the delegate that a remote notification arrived.
- [func didReceive(UILocalNotification)](didreceive(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/didreceive(_:)))
  Tells the delegate that a local notification was triggered.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:)))
  Delivers a remote notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:forremotenotification:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:forremotenotification:withresponseinfo:)))
  Delivers a remote notification payload and user response information to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification)](handleaction(withidentifier:for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:)))
  Delivers a local notification payload and a user-selected action to the app.
- [func handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](handleaction(withidentifier:for:withresponseinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleaction(withidentifier:for:withresponseinfo:)))
  Delivers a local notification payload and user response information to the app.

## Relationships

### Inherits From
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project))
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](wkapplication.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication))
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension))
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)))
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [class WKInterfaceDevice](wkinterfacedevice.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice))
  An object that provides information about the user’s Apple Watch.
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate)*