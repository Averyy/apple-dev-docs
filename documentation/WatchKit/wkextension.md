# WKExtension

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

The centralized point of control and coordination for extension-based apps running in watchOS.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2 (renamed: WKApplication)

## Declaration

```swift
@MainActor
class WKExtension
```

```objc
@interface WKExtension : NSObject
```

#### Overview

In Xcode 13 and earlier the system divides a watchOS app into two sections:

- **WatchKit app**: An app bundle that contains your app icon. For storyboard-based apps, it also includes your storyboard and any assets used by the storyboard.
- **WatchKit extension**: An extension that contains your watchOS app’s code.

In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later

Apps with separate WatchKit app and extensions have a single extension object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.

As relevant events occur within your WatchKit app, the extension object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see [`WKExtensionDelegate`](./wkextensiondelegate.md).

## Topics

### Getting the extension object
- [class func shared() -> WKExtension](./wkextension/shared%28%29.md)
  Returns the shared WatchKit extension object.
### Accessing the extension delegate
- [var delegate: (any WKExtensionDelegate)?](./wkextension/delegate.md)
  The delegate of the WatchKit extension object.
- [protocol WKExtensionDelegate](./wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
### Opening a URL resource
- [func openSystemURL(URL)](./wkextension/opensystemurl%28_%29.md)
  Opens the specified system URL.
### Getting the interface controllers
- [var rootInterfaceController: WKInterfaceController?](./wkextension/rootinterfacecontroller.md)
  The app’s root interface controller.
- [var visibleInterfaceController: WKInterfaceController?](./wkextension/visibleinterfacecontroller.md)
  Returns the last visible interface controller.
### Managing the execution state
- [var applicationState: WKApplicationState](./wkextension/applicationstate.md)
  The runtime state of the Watch app.
- [enum WKApplicationState](./wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](./wkextension/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./wkextension/schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](./wkextension/isfrontmosttimeoutextended.md)
  A Boolean value that determines whether the app extends its time as the frontmost app.
### Managing the user interface
- [var isAutorotating: Bool](./wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](./wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [var globalTintColor: UIColor](./wkextension/globaltintcolor.md)
  The watchOS app’s global tint color.
- [func enableWaterLock()](./wkextension/enablewaterlock%28%29.md)
  Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.
### Managing the snapshot
- [func scheduleSnapshotRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./wkextension/schedulesnapshotrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh your app’s snapshot.
### Observing messages from the notification center
- [static var applicationDidFinishLaunchingNotification: NSNotification.Name](./wkextension/applicationdidfinishlaunchingnotification.md)
  A message indicating that the launch process finished and the extension is ready to run.
- [static var applicationDidBecomeActiveNotification: NSNotification.Name](./wkextension/applicationdidbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [static var applicationWillResignActiveNotification: NSNotification.Name](./wkextension/applicationwillresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [static var applicationWillEnterForegroundNotification: NSNotification.Name](./wkextension/applicationwillenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [static var applicationDidEnterBackgroundNotification: NSNotification.Name](./wkextension/applicationdidenterbackgroundnotification.md)
  A message indicating that the watchOS app transitioned from the foreground to the background.
### Registering for remote notifications
- [func registerForRemoteNotifications()](./wkextension/registerforremotenotifications%28%29.md)
  Register to receive remote notifications from the Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](./wkextension/unregisterforremotenotifications%28%29.md)
  Unregister for all remote notifications received from Apple Push Notification service (APNs).
- [var isRegisteredForRemoteNotifications: Bool](./wkextension/isregisteredforremotenotifications.md)
  A Boolean value that indicates if the app has successfully registered for remote notifications.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### App structure
- [Setting up a watchOS project](../watchOS-Apps/setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](./wkapplication.md)
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](./wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [protocol WKExtensionDelegate](./wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](./wkapplicationmain%28_,_,_%29.md)
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [class WKInterfaceDevice](./wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](../BundleResources/information-property-list/wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension)*