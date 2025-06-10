# UIRemoteNotificationType

**Framework**: UIKit  
**Kind**: struct

Constants indicating the types of notifications the app may display to the user.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct UIRemoteNotificationType
```

#### Overview

One or more of the values in the `UIRemoteNotificationType` bit mask are passed to iOS as the argument of the [`registerForRemoteNotifications(matching:)`](uiapplication/registerforremotenotifications(matching:).md) method. Thereafter, iOS filters notifications for the app based on these values. You can always get the current notification types by calling the [`enabledRemoteNotificationTypes()`](uiapplication/enabledremotenotificationtypes().md) method.

## Topics

### Constants
- [static var badge: UIRemoteNotificationType](uiremotenotificationtype/badge.md)
  The app accepts notifications that badge the app icon.
- [static var sound: UIRemoteNotificationType](uiremotenotificationtype/sound.md)
  The app accepts alert sounds as notifications.
- [static var alert: UIRemoteNotificationType](uiremotenotificationtype/alert.md)
  The app accepts alert messages as notifications.
- [static var newsstandContentAvailability: UIRemoteNotificationType](uiremotenotificationtype/newsstandcontentavailability.md)
  The app accepts notifications that start the downloading of issue assets for Newsstand apps.
### Initializers
- [init(rawValue: UInt)](uiremotenotificationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func requestSceneSessionActivation(UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md)
  Asks the system to activate an existing scene, or create a new scene and associate it with your app.
- [func beginIgnoringInteractionEvents()](uiapplication/beginignoringinteractionevents.md)
  Tells the receiver to suspend the handling of touch-related events.
- [func endIgnoringInteractionEvents()](uiapplication/endignoringinteractionevents.md)
  Tells the receiver to resume the handling of touch-related events.
- [func setMinimumBackgroundFetchInterval(TimeInterval)](uiapplication/setminimumbackgroundfetchinterval(_:).md)
  Specifies the minimum amount of time that must elapse between background fetch operations.
- [func scheduleLocalNotification(UILocalNotification)](uiapplication/schedulelocalnotification(_:).md)
  Schedules a local notification for delivery at its encapsulated date and time.
- [func presentLocalNotificationNow(UILocalNotification)](uiapplication/presentlocalnotificationnow(_:).md)
  Presents a local notification immediately.
- [func cancelLocalNotification(UILocalNotification)](uiapplication/cancellocalnotification(_:).md)
  Cancels the delivery of the specified scheduled local notification.
- [func cancelAllLocalNotifications()](uiapplication/cancelalllocalnotifications.md)
  Cancels the delivery of all scheduled local notifications.
- [func setKeepAliveTimeout(TimeInterval, handler: (() -> Void)?) -> Bool](uiapplication/setkeepalivetimeout(_:handler:).md)
  Configures a periodic handler for VoIP apps in older versions of iOS.
- [let UIMinimumKeepAliveTimeout: TimeInterval](uiminimumkeepalivetimeout.md)
  The minimum amount of time (measured in seconds) an app may run a critical background task in the background.
- [func clearKeepAliveTimeout()](uiapplication/clearkeepalivetimeout.md)
  Removes a previously installed periodic handler block.
- [func setStatusBarHidden(Bool, with: UIStatusBarAnimation)](uiapplication/setstatusbarhidden(_:with:).md)
  Hides or shows the status bar, optionally animating the transition.
- [func setStatusBarStyle(UIStatusBarStyle, animated: Bool)](uiapplication/setstatusbarstyle(_:animated:).md)
  Sets the style of the status bar, optionally animating the transition to the new style.
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](uiapplication/setstatusbarorientation(_:animated:).md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerUserNotificationSettings(UIUserNotificationSettings)](uiapplication/registerusernotificationsettings(_:).md)
  Registers your preferred options for notifying the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiremotenotificationtype)*