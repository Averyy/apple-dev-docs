# applicationWillResignActive()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the system is about to deactivate the watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func applicationWillResignActive()
```

## Overview

WatchKit calls this method after your app launches and before it exits. Use this method to pause any active tasks. For example, you could use it to stop any active timers. An app in the inactive state should do minimal work while it waits to transition to the active or not running state.

If your app has unsaved user data, you can save it here to ensure that it isn’t lost. However, it’s a good idea to save user data at appropriate points throughout the execution of your app, usually in response to user actions. Don’t rely on specific app state transitions to save all of your app’s critical data.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

 When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive())*