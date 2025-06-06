# didEnterBackgroundNotification

**Framework**: Watchkit  
**Kind**: property

A message indicating that the watchOS app transitioned from the foreground to the background.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency static let didEnterBackgroundNotification: NSNotification.Name
```

#### Discussion

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [static let didFinishLaunchingNotification: NSNotification.Name](wkapplication/didfinishlaunchingnotification.md)
  A message indicating that the launch process finished and the extension is ready to run.
- [static let didBecomeActiveNotification: NSNotification.Name](wkapplication/didbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [static let willResignActiveNotification: NSNotification.Name](wkapplication/willresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [static let willEnterForegroundNotification: NSNotification.Name](wkapplication/willenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/didenterbackgroundnotification)*