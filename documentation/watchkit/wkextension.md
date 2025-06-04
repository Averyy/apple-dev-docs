# WKExtension

**Framework**: Watchkit  
**Kind**: class

The centralized point of control and coordination for extension-based apps running in watchOS.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor class WKExtension
```

## Overview

In Xcode 13 and earlier the system divides a watchOS app into two sections:

In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later

Apps with separate WatchKit app and extensions have a single extension object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.

As relevant events occur within your WatchKit app, the extension object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see [`WKExtensionDelegate`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate).

## Topics

### Getting the extension object
- [class func shared() -> WKExtension](shared().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/shared()))
  Returns the shared WatchKit extension object.
### Accessing the extension delegate
- [var delegate: (any WKExtensionDelegate)?](delegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/delegate))
  The delegate of the WatchKit extension object.
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
  A collection of methods that manages the app-level behavior of a WatchKit extension.
### Opening a URL resource
- [func openSystemURL(URL)](opensystemurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/opensystemurl(_:)))
  Opens the specified system URL.
### Getting the interface controllers
- [var rootInterfaceController: WKInterfaceController?](rootinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/rootinterfacecontroller))
  The app’s root interface controller.
- [var visibleInterfaceController: WKInterfaceController?](visibleinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/visibleinterfacecontroller))
  Returns the last visible interface controller.
### Managing the execution state
- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate))
  The runtime state of the Watch app.
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](isfrontmosttimeoutextended.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended))
  A Boolean value that determines whether the app extends its time as the frontmost app.
### Managing the user interface
- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/globaltintcolor))
  The watchOS app’s global tint color.
- [func enableWaterLock()](enablewaterlock().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/enablewaterlock()))
  Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.
### Managing the snapshot
- [func scheduleSnapshotRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh your app’s snapshot.
### Observing messages from the notification center
- [class let applicationDidFinishLaunchingNotification: NSNotification.Name](applicationdidfinishlaunchingnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidfinishlaunchingnotification))
  A message indicating that the launch process finished and the extension is ready to run.
- [class let applicationDidBecomeActiveNotification: NSNotification.Name](applicationdidbecomeactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidbecomeactivenotification))
  A message indicating that the watchOS app is visible and processing events.
- [class let applicationWillResignActiveNotification: NSNotification.Name](applicationwillresignactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillresignactivenotification))
  A message indicating that the system is about to deactivate the watchOS app.
- [class let applicationWillEnterForegroundNotification: NSNotification.Name](applicationwillenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillenterforegroundnotification))
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [class let applicationDidEnterBackgroundNotification: NSNotification.Name](applicationdidenterbackgroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidenterbackgroundnotification))
  A message indicating that the watchOS app transitioned from the foreground to the background.
### Registering for remote notifications
- [func registerForRemoteNotifications()](registerforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications()))
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](unregisterforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/unregisterforremotenotifications()))
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](isregisteredforremotenotifications.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isregisteredforremotenotifications))
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
- [class WKApplication](wkapplication.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication))
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)))
- [class WKInterfaceDevice](wkinterfacedevice.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice))
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension)*