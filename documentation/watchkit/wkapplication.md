# WKApplication

**Framework**: Watchkit  
**Kind**: class

The centralized point of control and coordination for apps with a single watchOS app target.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor class WKApplication
```

## Overview

In Xcode 13 and earlier, the system divides a watchOS app into two sections:

In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later

Single-target watchOS apps have a single app object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.

As relevant events occur within your WatchKit app, the app object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life-cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate).

## Topics

### Getting the app object
- [class func shared() -> WKApplication](shared().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/shared()))
  Returns the shared WatchKit app object.
### Accessing the app delegate
- [var delegate: (any WKApplicationDelegate)?](delegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/delegate))
  The delegate of the WatchKit app object.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
### Opening a URL resource
- [func openSystemURL(URL)](opensystemurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/opensystemurl(_:)))
  Opens the specified system URL.
### Getting the interface controller
- [var rootInterfaceController: WKInterfaceController?](rootinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/rootinterfacecontroller))
  The app’s root interface controller.
- [var visibleInterfaceController: WKInterfaceController?](visibleinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/visibleinterfacecontroller))
  Returns the last visible interface controller.
### Managing the app state
- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/applicationstate))
  The runtime state of the watchOS app.
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.
### Managing the user interface
- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotating))
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/globaltintcolor))
  The watchOS app’s global tint color.
### Managing the snapshot
- [func scheduleSnapshotRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh your app’s snapshot.
### Observing messages from the notification center
- [static let didFinishLaunchingNotification: NSNotification.Name](didfinishlaunchingnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didfinishlaunchingnotification))
  A message indicating that the launch process finished and the extension is ready to run.
- [static let didBecomeActiveNotification: NSNotification.Name](didbecomeactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didbecomeactivenotification))
  A message indicating that the watchOS app is visible and processing events.
- [static let willResignActiveNotification: NSNotification.Name](willresignactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/willresignactivenotification))
  A message indicating that the system is about to deactivate the watchOS app.
- [static let willEnterForegroundNotification: NSNotification.Name](willenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/willenterforegroundnotification))
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [static let didEnterBackgroundNotification: NSNotification.Name](didenterbackgroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didenterbackgroundnotification))
  A message indicating that the watchOS app transitioned from the foreground to the background.
### Registering for remote notifications
- [func registerForRemoteNotifications()](registerforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/registerforremotenotifications()))
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](unregisterforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/unregisterforremotenotifications()))
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](isregisteredforremotenotifications.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isregisteredforremotenotifications))
  A Boolean value that indicates if the app has successfully registered for remote notifications.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project))
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
- [class WKExtension](wkextension.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension))
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)))
- [class WKInterfaceDevice](wkinterfacedevice.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice))
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication)*