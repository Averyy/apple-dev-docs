# applicationDidEnterBackground()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the app has transitioned from the foreground to the background.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
optional func applicationDidEnterBackground()
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)

#### Discussion

Override this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state if it’s purged from memory. You have only a few seconds to complete these actions and return.

The system typically suspends your app shortly after this method returns; therefore, don’t call any asynchronous methods from your [`applicationDidEnterBackground()`](wkextensiondelegate/applicationdidenterbackground().md) implementation. Asynchronous methods may not be able to complete before the app is suspended.

Additionally, the system may purge suspended apps at any time to make room for other apps. You aren’t notified when an app is purged from memory. The [`applicationDidEnterBackground()`](wkextensiondelegate/applicationdidenterbackground().md) method is your last chance to perform any cleanup before the app terminates.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

 When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](wkextensiondelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](wkextensiondelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkextensiondelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkextensiondelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground())*