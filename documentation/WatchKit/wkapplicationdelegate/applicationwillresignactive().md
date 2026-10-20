# applicationWillResignActive()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system is about to deactivate the watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func applicationWillResignActive()
```

```objc
- (void) applicationWillResignActive;
```

#### Discussion

WatchKit calls this method after your app launches and before it exits. Use this method to pause any active tasks. For example, you could use it to stop any active timers. An app in the inactive state should do minimal work while it waits to transition to the active or not running state.

If your app has unsaved user data, you can save it here to ensure that it isn’t lost. However, it’s a good idea to save user data at appropriate points throughout the execution of your app, usually in response to user actions. Don’t rely on specific app state transitions to save all of your app’s critical data.

> **Note**:  When creating an app that uses the SwiftUI [`App`](../../SwiftUI/app.md) protocol to manage your life cycle, use the [`onChange(of:perform:)`](../../SwiftUI/view/onchange%28of,perform%29.md) modifier and the [`scenePhase`](../../SwiftUI/environmentvalues/scenephase.md) environment value to monitor life cycle changes when possible. For more information, see [Building a watchOS app](../../watchOS-Apps/building_a_watchos_app.md).

## See Also

### Monitoring state changes
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](./main%28%29.md)
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](./applicationdidfinishlaunching%28%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](./applicationdidbecomeactive%28%29.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillEnterForeground()](./applicationwillenterforeground%28%29.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](./applicationdidenterbackground%28%29.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](./deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive())*