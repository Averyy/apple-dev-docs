# applicationDidFinishLaunching()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the launch process is almost done and the app is almost ready to run.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func applicationDidFinishLaunching()
```

```objc
- (void) applicationDidFinishLaunching;
```

#### Discussion

WatchKit calls this method after the launch cycle has finished and before your app’s interface is active. Use this method to complete your watchOS apps initialization and prepare it to run. For example, a page-based app could use this method to call the [`reloadRootControllers(withNames:contexts:)`](../wkinterfacecontroller/reloadrootcontrollers%28withnames,contexts%29.md) method to specify the initial set of interface controllers to display.

> **Note**:  When creating an app that uses the SwiftUI [`App`](../../SwiftUI/app.md) protocol to manage your life cycle, use the [`onChange(of:perform:)`](../../SwiftUI/view/onchange%28of,perform%29.md) modifier and the [`scenePhase`](../../SwiftUI/environmentvalues/scenephase.md) environment value to monitor life cycle changes when possible. For more information, see [Building a watchOS app](../../watchOS-Apps/building_a_watchos_app.md).

## See Also

### Monitoring state changes
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](./main%28%29.md)
  Provides the top-level entry point for an app.
- [func applicationDidBecomeActive()](./applicationdidbecomeactive%28%29.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](./applicationwillresignactive%28%29.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](./applicationwillenterforeground%28%29.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](./applicationdidenterbackground%28%29.md)
  Tells the delegate that the app has transitioned from the foreground to the background.
- [func deviceOrientationDidChange()](./deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching())*