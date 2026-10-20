# applicationDidEnterBackground()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app has transitioned from the foreground to the background.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2

## Declaration

```swift
optional func applicationDidEnterBackground()
```

```objc
- (void) applicationDidEnterBackground;
```

## Mentions

- [Handling Common State Transitions](../handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

#### Discussion

Override this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state if it’s purged from memory. You have only a few seconds to complete these actions and return.

The system typically suspends your app shortly after this method returns; therefore, don’t call any asynchronous methods from your [`applicationDidEnterBackground()`](./applicationdidenterbackground%28%29.md) implementation. Asynchronous methods may not be able to complete before the app is suspended.

Additionally, the system may purge suspended apps at any time to make room for other apps. You aren’t notified when an app is purged from memory. The [`applicationDidEnterBackground()`](./applicationdidenterbackground%28%29.md) method is your last chance to perform any cleanup before the app terminates.

> **Note**:  When creating an app that uses the SwiftUI [`App`](../../SwiftUI/app.md) protocol to manage your life cycle, use the [`onChange(of:perform:)`](../../SwiftUI/view/onchange%28of,perform%29.md) modifier and the [`scenePhase`](../../SwiftUI/environmentvalues/scenephase.md) environment value to monitor life cycle changes when possible. For more information, see [Building a watchOS app](../../watchOS-Apps/building_a_watchos_app.md).

## See Also

### Monitoring state changes
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](./applicationdidfinishlaunching%28%29.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](./applicationdidbecomeactive%28%29.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](./applicationwillresignactive%28%29.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](./applicationwillenterforeground%28%29.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func deviceOrientationDidChange()](./deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground())*