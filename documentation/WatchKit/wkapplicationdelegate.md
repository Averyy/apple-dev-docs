# WKApplicationDelegate

**Framework**: WatchKit  
**Kind**: protocol  
**Role**: Protocol

A collection of methods that manages the app-level behavior for a single-target watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
protocol WKApplicationDelegate : NSObjectProtocol
```

```objc
@protocol WKApplicationDelegate <NSObject>
```

## Mentions

- [Using background tasks](./using-background-tasks.md)

## Overview

Implement the delegate’s methods to respond to your app’s life-cycle events, such as the activation and deactivation of your app. You can also implement delegate methods to respond to background tasks, Siri intents, workout sessions, or Handoff activity from another devices.

To add an app delegate, define a delegate class that subclasses [`NSObject`](../ObjectiveC/nsobject-swift.class.md) and adopts the [`WKApplicationDelegate`](./wkapplicationdelegate.md) protocol.

```swift
import WatchKit

class MyWatchAppDelegate: NSObject, WKApplicationDelegate {

}
```

Then define an app delegate adaptor in your SwiftUI [`App`](../SwiftUI/app.md) structure.

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

## Topics

### Monitoring state changes
- [Working with the watchOS app life cycle](./working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](./wkapplicationdelegate/main%28%29.md)
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](./wkapplicationdelegate/applicationdidfinishlaunching%28%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](./wkapplicationdelegate/applicationdidbecomeactive%28%29.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](./wkapplicationdelegate/applicationwillresignactive%28%29.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](./wkapplicationdelegate/applicationwillenterforeground%28%29.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](./wkapplicationdelegate/applicationdidenterbackground%28%29.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](./wkapplicationdelegate/deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.
### Responding to intents
- [func handle(INIntent, completionHandler: (INIntentResponse) -> Void)](./wkapplicationdelegate/handle%28_,completionhandler%29.md)
  Responds to a Siri intent.
### Setup Now Playing interface
- [func handleRemoteNowPlayingActivity()](./wkapplicationdelegate/handleremotenowplayingactivity%28%29.md)
  Tells the delegate when the user plays audio in the corresponding iOS app.
### Handling a workout session
- [func handle(HKWorkoutConfiguration)](./wkapplicationdelegate/handle%28_%29-1pfoc.md)
  Tells the delegate that the user started a workout session on the paired iPhone.
- [func handleActiveWorkoutRecovery()](./wkapplicationdelegate/handleactiveworkoutrecovery%28%29.md)
  Tells the delegate when the app relaunches after crashing during an active workout session.
### Handling background tasks
- [func handle(Set<WKRefreshBackgroundTask>)](./wkapplicationdelegate/handle%28_%29-4vdjo.md)
  Tells the delegate that the app has received one or more background tasks.
### Handling extended runtime tasks
- [func handle(WKExtendedRuntimeSession)](./wkapplicationdelegate/handle%28_%29-7kiwx.md)
  Tells the delegate that the system launched your app to resume an extended runtime session.
### Managing remote notifications
- [func didRegisterForRemoteNotifications(withDeviceToken: Data)](./wkapplicationdelegate/didregisterforremotenotifications%28withdevicetoken%29.md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func didFailToRegisterForRemoteNotificationsWithError(any Error)](./wkapplicationdelegate/didfailtoregisterforremotenotificationswitherror%28_%29.md)
  Tells the delegate that Apple Push Notification service (APNs) can’t successfully complete the registration process.
- [func didReceiveRemoteNotification([AnyHashable : Any], fetchCompletionHandler: (WKBackgroundFetchResult) -> Void)](./wkapplicationdelegate/didreceiveremotenotification%28_,fetchcompletionhandler%29.md)
  Tells the delegate that a background notification has arrived.
- [enum WKBackgroundFetchResult](./wkbackgroundfetchresult.md)
  The result of an attempt to download the content associated with a remote notification.
### Coordinating Handoff activity
- [func handleUserActivity([AnyHashable : Any]?)](./wkapplicationdelegate/handleuseractivity%28_%29.md)
  Responds to Handoff–related activity from complications and notifications.
- [func handle(NSUserActivity)](./wkapplicationdelegate/handle%28_%29-3kqsk.md)
  Responds to Handoff–related activity from Siri.
### Accepting CloudKit shares
- [func userDidAcceptCloudKitShare(with: CKShareMetadata)](./wkapplicationdelegate/userdidacceptcloudkitshare%28with%29.md)
  Tells the delegate that the app has access to shared information in CloudKit.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### App structure
- [Setting up a watchOS project](../watchOS-Apps/setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](./wkapplication.md)
  The centralized point of control and coordination for apps with a single watchOS app target.
- [class WKExtension](./wkextension.md)
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [protocol WKExtensionDelegate](./wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](./wkapplicationmain%28_,_,_%29.md)
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [class WKInterfaceDevice](./wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](../BundleResources/information-property-list/wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate)*