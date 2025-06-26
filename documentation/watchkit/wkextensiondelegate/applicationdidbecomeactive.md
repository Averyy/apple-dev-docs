# applicationDidBecomeActive()

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the watchOS app is visible and processing events.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func applicationDidBecomeActive()
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)

#### Discussion

WatchKit calls this method to let you know that your app transitioned from the inactive to the active state. Use this method to start any tasks that were paused or not yet started while the app was inactive. For example, you could use it to start timers. You can also use it to gather information needed to configure your app’s initial user interface.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](wkextensiondelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationWillResignActive()](wkextensiondelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkextensiondelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](wkextensiondelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive())*