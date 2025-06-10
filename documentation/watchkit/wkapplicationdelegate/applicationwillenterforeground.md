# applicationWillEnterForeground()

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the app is about to transition from the background to the foreground.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func applicationWillEnterForeground()
```

#### Discussion

The system calls this method when the app transitions from the background to the foreground. Override this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [`applicationDidBecomeActive()`](wkapplicationdelegate/applicationdidbecomeactive().md) method, as the app moves from the inactive to the active state.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](wkapplicationdelegate/main.md)
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](wkapplicationdelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](wkapplicationdelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkapplicationdelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationDidEnterBackground()](wkapplicationdelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](wkapplicationdelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground())*