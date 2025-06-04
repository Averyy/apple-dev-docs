# WKApplicationDelegate

**Framework**: Watchkit  
**Kind**: protocol

A collection of methods that manages the app-level behavior for a single-target watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor protocol WKApplicationDelegate : NSObjectProtocol
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

## Overview

Implement the delegate’s methods to respond to your app’s life-cycle events, such as the activation and deactivation of your app. You can also implement delegate methods to respond to background tasks, Siri intents, workout sessions, or Handoff activity from another devices.

To add an app delegate, define a delegate class that subclasses [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) and adopts the [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) protocol.

```swift
import WatchKit

class MyWatchAppDelegate: NSObject, WKApplicationDelegate {

}
```

Then define an app delegate adaptor in your SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) structure.

```swift
import SwiftUI

@main
struct MyWatchApp_Watch_AppApp: App {
    @WKApplicationDelegateAdaptor var appDelegate: MyWatchAppDelegate
    var body: some Scene {
        WindowGroup {
            NavigationStack {
                ContentView()
            }
        }
    }
}

```

Finally, implement the delegate methods you want to handle.

## Code Examples

### Example

```swift
import WatchKit

class MyWatchAppDelegate: NSObject, WKApplicationDelegate {

}
```

### Example

```swift
import SwiftUI

@main
struct MyWatchApp_Watch_AppApp: App {
    @WKApplicationDelegateAdaptor var appDelegate: MyWatchAppDelegate
    var body: some Scene {
        WindowGroup {
            NavigationStack {
                ContentView()
            }
        }
    }
}
```

## Topics

### Monitoring state changes
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange()))
  Tells the delegate that the device’s orientation has changed.
### Responding to intents
- [func handle(INIntent, completionHandler: (INIntentResponse) -> Void)](handle(_:completionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:completionhandler:)))
  Responds to a Siri intent.
### Setup Now Playing interface
- [func handleRemoteNowPlayingActivity()](handleremotenowplayingactivity().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleremotenowplayingactivity()))
  Tells the delegate when the user plays audio in the corresponding iOS app.
### Handling a workout session
- [func handle(HKWorkoutConfiguration)](handle(_:)-1pfoc.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-1pfoc))
  Tells the delegate that the user started a workout session on the paired iPhone.
- [func handleActiveWorkoutRecovery()](handleactiveworkoutrecovery().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleactiveworkoutrecovery()))
  Tells the delegate when the app relaunches after crashing during an active workout session.
### Handling background tasks
- [func handle(Set<WKRefreshBackgroundTask>)](handle(_:)-4vdjo.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo))
  Tells the delegate that the app has received one or more background tasks.
### Handling extended runtime tasks
- [func handle(WKExtendedRuntimeSession)](handle(_:)-7kiwx.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-7kiwx))
  Tells the delegate that the system launched your app to resume an extended runtime session.
### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](didregisterforremotenotifications(withdevicetoken:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didregisterforremotenotifications(withdevicetoken:)))
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](didfailtoregisterforremotenotificationswitherror(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror(_:)))
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](didreceiveremotenotification(_:fetchcompletionhandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/didreceiveremotenotification(_:fetchcompletionhandler:)))
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](wkbackgroundfetchresult.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbackgroundfetchresult))
  The result of an attempt to download the content associated with a remote notification.
### Coordinating Handoff activity
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handleuseractivity(_:)))
  Responds to Handoff–related activity from complications and notifications.
- [func handle(NSUserActivity)](handle(_:)-3kqsk.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-3kqsk))
  Responds to Handoff–related activity from Siri.
### Accepting CloudKit shares
- [func userDidAcceptCloudKitShare(with: CKShareMetadata)](userdidacceptcloudkitshare(with:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/userdidacceptcloudkitshare(with:)))
  Tells the delegate that the app has access to shared information in CloudKit.

## Relationships

### Inherits From
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project))
- [class WKApplication](wkapplication.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication))
- [class WKExtension](wkextension.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension))
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)))
- [class WKInterfaceDevice](wkinterfacedevice.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice))
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate)*