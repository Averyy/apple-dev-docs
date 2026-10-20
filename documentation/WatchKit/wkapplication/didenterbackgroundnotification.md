# didEnterBackgroundNotification

**Framework**: WatchKit  
**Kind**: property  
**Role**: Type Property

A message indicating that the watchOS app transitioned from the foreground to the background.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class let didEnterBackgroundNotification: NSNotification.Name
```

```c
extern NSNotificationName const WKApplicationDidEnterBackgroundNotification;
```

#### Discussion

When creating an app that uses the SwiftUI [`App`](../../SwiftUI/app.md) protocol to manage your life cycle, use the [`onChange(of:perform:)`](../../SwiftUI/view/onchange%28of,perform%29.md) modifier and the [`scenePhase`](../../SwiftUI/environmentvalues/scenephase.md) environment value to monitor life cycle changes when possible. For more information, see [Building a watchOS app](../../watchOS-Apps/building_a_watchos_app.md).

## See Also

### Observing messages from the notification center
- [class let didFinishLaunchingNotification: NSNotification.Name](./didfinishlaunchingnotification.md)
  A message indicating that the launch process finished and the extension is ready to run.
- [class let didBecomeActiveNotification: NSNotification.Name](./didbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [class let willResignActiveNotification: NSNotification.Name](./willresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [class let willEnterForegroundNotification: NSNotification.Name](./willenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/didenterbackgroundnotification)*