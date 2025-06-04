# applicationDidBecomeActiveNotification

**Framework**: WatchKit  
**Kind**: property

A message indicating that the watchOS app is visible and processing events.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class let applicationDidBecomeActiveNotification: NSNotification.Name
```

#### Discussion

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [class let applicationDidFinishLaunchingNotification: NSNotification.Name](applicationdidfinishlaunchingnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidfinishlaunchingnotification))
  A message indicating that the launch process finished and the extension is ready to run.
- [class let applicationWillResignActiveNotification: NSNotification.Name](applicationwillresignactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillresignactivenotification))
  A message indicating that the system is about to deactivate the watchOS app.
- [class let applicationWillEnterForegroundNotification: NSNotification.Name](applicationwillenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillenterforegroundnotification))
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [class let applicationDidEnterBackgroundNotification: NSNotification.Name](applicationdidenterbackgroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidenterbackgroundnotification))
  A message indicating that the watchOS app transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidbecomeactivenotification)*