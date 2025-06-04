# applicationDidEnterBackground()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the app has transitioned from the foreground to the background.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func applicationDidEnterBackground()
```

## Overview

Override this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state if it’s purged from memory. You have only a few seconds to complete these actions and return.

The system typically suspends your app shortly after this method returns; therefore, don’t call any asynchronous methods from your [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()) implementation. Asynchronous methods may not be able to complete before the system suspends the app.

Additionally, the system may purge suspended apps at any time to make room for other apps. You aren’t notified when the system purges an app from memory. The [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()) method is your last chance to perform any cleanup before the app terminates.

> **Note**:  When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

 When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground())*