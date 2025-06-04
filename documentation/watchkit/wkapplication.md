# WKApplication

**Framework**: WatchKit  
**Kind**: class

The centralized point of control and coordination for apps with a single watchOS app target.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
class WKApplication
```

#### Overview

In Xcode 13 and earlier, the system divides a watchOS app into two sections:

In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later

Single-target watchOS apps have a single app object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.

As relevant events occur within your WatchKit app, the app object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life-cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see [`WKApplicationDelegate`](wkapplicationdelegate.md).

## Topics

### Getting the app object
- [class func shared() -> WKApplication](wkapplication/shared.md)
  Returns the shared WatchKit app object.
### Accessing the app delegate
- [var delegate: (any WKApplicationDelegate)?](wkapplication/delegate.md)
  The delegate of the WatchKit app object.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
### Opening a URL resource
- [func openSystemURL(URL)](wkapplication/opensystemurl(_:).md)
  Opens the specified system URL.
### Getting the interface controller
- [var rootInterfaceController: WKInterfaceController?](wkapplication/rootinterfacecontroller.md)
  The app’s root interface controller.
- [var visibleInterfaceController: WKInterfaceController?](wkapplication/visibleinterfacecontroller.md)
  Returns the last visible interface controller.
### Managing the app state
- [var applicationState: WKApplicationState](wkapplication/applicationstate.md)
  The runtime state of the watchOS app.
- [enum WKApplicationState](wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](wkapplication/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh the app’s data.
### Managing the user interface
- [var isAutorotating: Bool](wkapplication/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkapplication/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.
- [var globalTintColor: UIColor](wkapplication/globaltintcolor.md)
  The watchOS app’s global tint color.
### Managing the snapshot
- [func scheduleSnapshotRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkapplication/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh your app’s snapshot.
### Observing messages from the notification center
- [static let didFinishLaunchingNotification: NSNotification.Name](wkapplication/didfinishlaunchingnotification.md)
  A message indicating that the launch process finished and the extension is ready to run.
- [static let didBecomeActiveNotification: NSNotification.Name](wkapplication/didbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [static let willResignActiveNotification: NSNotification.Name](wkapplication/willresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [static let willEnterForegroundNotification: NSNotification.Name](wkapplication/willenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [static let didEnterBackgroundNotification: NSNotification.Name](wkapplication/didenterbackgroundnotification.md)
  A message indicating that the watchOS app transitioned from the foreground to the background.
### Registering for remote notifications
- [func registerForRemoteNotifications()](wkapplication/registerforremotenotifications.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](wkapplication/unregisterforremotenotifications.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](wkapplication/isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.

## Relationships

### Inherits From
- [NSObject](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md)
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [protocol WKExtensionDelegate](wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md)
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [class WKInterfaceDevice](wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication)*