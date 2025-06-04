# applicationDidEnterBackground()

**Framework**: WatchKit  
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

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))

#### Discussion

Override this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state if it’s purged from memory. You have only a few seconds to complete these actions and return.

The system typically suspends your app shortly after this method returns; therefore, don’t call any asynchronous methods from your [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) implementation. Asynchronous methods may not be able to complete before the app is suspended.

Additionally, the system may purge suspended apps at any time to make room for other apps. You aren’t notified when an app is purged from memory. The [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) method is your last chance to perform any cleanup before the app terminates.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

 When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()))
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()))
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()))
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()))
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange()))
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground())*