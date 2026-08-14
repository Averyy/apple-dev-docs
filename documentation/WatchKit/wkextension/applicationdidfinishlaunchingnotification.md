# applicationDidFinishLaunchingNotification

**Framework**: WatchKit  
**Kind**: property

A message indicating that the launch process finished and the extension is ready to run.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency static var applicationDidFinishLaunchingNotification: NSNotification.Name { get }
```

#### Discussion

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/swiftui/app) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/swiftui/environmentvalues/scenephase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchos-apps/building_a_watchos_app).

## See Also

- [static var applicationDidBecomeActiveNotification: NSNotification.Name](wkextension/applicationdidbecomeactivenotification.md)
  A message indicating that the watchOS app is visible and processing events.
- [static var applicationWillResignActiveNotification: NSNotification.Name](wkextension/applicationwillresignactivenotification.md)
  A message indicating that the system is about to deactivate the watchOS app.
- [static var applicationWillEnterForegroundNotification: NSNotification.Name](wkextension/applicationwillenterforegroundnotification.md)
  A message indicating that the watchOS app is about to transition from the background to the foreground.
- [static var applicationDidEnterBackgroundNotification: NSNotification.Name](wkextension/applicationdidenterbackgroundnotification.md)
  A message indicating that the watchOS app transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidfinishlaunchingnotification)*