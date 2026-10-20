# applicationDidEnterBackgroundNotification

**Framework**: WatchKit  
**Kind**: property  
**Role**: Type Property

A message indicating that the watchOS app transitioned from the foreground to the background.

**Availability**:
- watchOS 7.0+ - Deprecated in 9.2 (renamed: WKApplication.didEnterBackgroundNotification)

## Declaration

```swift
@MainActor
@preconcurrency static var applicationDidEnterBackgroundNotification: NSNotification.Name { get }
```

#### Discussion

When creating an app that uses the SwiftUI [`App`](../../SwiftUI/app.md) protocol to manage your life cycle, use the [`onChange(of:perform:)`](../../SwiftUI/view/onchange%28of,perform%29.md) modifier and the [`scenePhase`](../../SwiftUI/environmentvalues/scenephase.md) environment value to monitor life cycle changes when possible. For more information, see [Building a watchOS app](../../watchOS-Apps/building_a_watchos_app.md).

## See Also

### Observing messages from the notification center
- [static var applicationDidFinishLaunchingNotification: NSNotification.Name](./applicationdidfinishlaunchingnotification.md)
  A message indicating that the launch process finished and the extension is ready to run.
- [static var applicationDidBecomeActiveNotification: NSNotification.Name](./applicationdidbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [static var applicationWillResignActiveNotification: NSNotification.Name](./applicationwillresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [static var applicationWillEnterForegroundNotification: NSNotification.Name](./applicationwillenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidenterbackgroundnotification)*