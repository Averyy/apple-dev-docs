# UIRemoteNotificationType

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants indicating the types of notifications the app may display to the user.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`UNAuthorizationOptions`](../UserNotifications/unauthorizationoptions.md) for user notifications and [`registerForRemoteNotifications()`](./uiapplication/registerforremotenotifications%28%29.md) for receiving remote notifications instead.

## Declaration

```swift
struct UIRemoteNotificationType
```

```c
enum UIRemoteNotificationType : NSUInteger;
```

#### Overview

One or more of the values in the `UIRemoteNotificationType` bit mask are passed to iOS as the argument of the [`registerForRemoteNotifications(matching:)`](./uiapplication/registerforremotenotifications%28matching%29.md) method. Thereafter, iOS filters notifications for the app based on these values. You can always get the current notification types by calling the [`enabledRemoteNotificationTypes()`](./uiapplication/enabledremotenotificationtypes%28%29.md) method.

## Topics

### Constants
- [static var badge: UIRemoteNotificationType](./uiremotenotificationtype/badge.md)
  The app accepts notifications that badge the app icon.
- [static var sound: UIRemoteNotificationType](./uiremotenotificationtype/sound.md)
  The app accepts alert sounds as notifications.
- [static var alert: UIRemoteNotificationType](./uiremotenotificationtype/alert.md)
  The app accepts alert messages as notifications.
- [static var newsstandContentAvailability: UIRemoteNotificationType](./uiremotenotificationtype/newsstandcontentavailability.md)
  The app accepts notifications that start the downloading of issue assets for Newsstand apps.
### Initializers
- [init(rawValue: UInt)](./uiremotenotificationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Deprecated methods
- [func requestSceneSessionActivation(UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)?)](./uiapplication/requestscenesessionactivation%28_,useractivity,options,errorhandler%29.md)
  Asks the system to activate an existing scene, or create a new scene and associate it with your app.
- [func beginIgnoringInteractionEvents()](./uiapplication/beginignoringinteractionevents%28%29.md)
  Tells the receiver to suspend the handling of touch-related events.
- [func endIgnoringInteractionEvents()](./uiapplication/endignoringinteractionevents%28%29.md)
  Tells the receiver to resume the handling of touch-related events.
- [func setMinimumBackgroundFetchInterval(TimeInterval)](./uiapplication/setminimumbackgroundfetchinterval%28_%29.md)
  Specifies the minimum amount of time that must elapse between background fetch operations.
- [func scheduleLocalNotification(UILocalNotification)](./uiapplication/schedulelocalnotification%28_%29.md)
  Schedules a local notification for delivery at its encapsulated date and time.
- [func presentLocalNotificationNow(UILocalNotification)](./uiapplication/presentlocalnotificationnow%28_%29.md)
  Presents a local notification immediately.
- [func cancelLocalNotification(UILocalNotification)](./uiapplication/cancellocalnotification%28_%29.md)
  Cancels the delivery of the specified scheduled local notification.
- [func cancelAllLocalNotifications()](./uiapplication/cancelalllocalnotifications%28%29.md)
  Cancels the delivery of all scheduled local notifications.
- [func setKeepAliveTimeout(TimeInterval, handler: (() -> Void)?) -> Bool](./uiapplication/setkeepalivetimeout%28_,handler%29.md)
  Configures a periodic handler for VoIP apps in older versions of iOS.
- [let UIMinimumKeepAliveTimeout: TimeInterval](./uiminimumkeepalivetimeout.md)
  The minimum amount of time (measured in seconds) an app may run a critical background task in the background.
- [func clearKeepAliveTimeout()](./uiapplication/clearkeepalivetimeout%28%29.md)
  Removes a previously installed periodic handler block.
- [func setStatusBarHidden(Bool, with: UIStatusBarAnimation)](./uiapplication/setstatusbarhidden%28_,with%29.md)
  Hides or shows the status bar, optionally animating the transition.
- [func setStatusBarStyle(UIStatusBarStyle, animated: Bool)](./uiapplication/setstatusbarstyle%28_,animated%29.md)
  Sets the style of the status bar, optionally animating the transition to the new style.
- [func setStatusBarOrientation(UIInterfaceOrientation, animated: Bool)](./uiapplication/setstatusbarorientation%28_,animated%29.md)
  Sets the app’s status bar to the specified orientation, optionally animating the transition.
- [func registerUserNotificationSettings(UIUserNotificationSettings)](./uiapplication/registerusernotificationsettings%28_%29.md)
  Registers your preferred options for notifying the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiremotenotificationtype)*