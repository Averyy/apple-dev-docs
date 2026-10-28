# applicationWillEnterForeground()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to transition from the background to the foreground.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2

## Declaration

```swift
optional func applicationWillEnterForeground()
```

```objc
- (void) applicationWillEnterForeground;
```

## Mentions

- [Handling Common State Transitions](../handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

## Discussion

The system calls this method when the app transitions from the background to the foreground. Override this method to undo many of the changes you made to your app upon entering the background. The call to this method is invariably followed by a call to the [`applicationDidBecomeActive()`](./applicationdidbecomeactive%28%29.md) method, as the app moves from the inactive to the active state.

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
- [func applicationDidEnterBackground()](./applicationdidenterbackground%28%29.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](./deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground())*