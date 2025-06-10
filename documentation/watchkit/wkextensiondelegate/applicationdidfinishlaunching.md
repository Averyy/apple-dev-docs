# applicationDidFinishLaunching()

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the launch process is almost done and the extension is almost ready to run.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func applicationDidFinishLaunching()
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
- [Handling Common State Transitions](handling-common-state-transitions.md)

#### Discussion

WatchKit calls this method after the launch cycle has finished and before your app’s interface is active. Use this method to complete your WatchKit extension’s initialization and prepare it to run. For example, a page-based app could use this method to call the [`reloadRootControllers(withNames:contexts:)`](wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:).md) method to specify the initial set of interface controllers to display.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidBecomeActive()](wkextensiondelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkextensiondelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkextensiondelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](wkextensiondelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching())*