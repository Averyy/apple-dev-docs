# main()

**Framework**: Watchkit  
**Kind**: method

Provides the top-level entry point for an app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor @preconcurrency static func main()
```

## Overview

[`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) provides an implementation of the [`main()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()) method that serves as the main entry point for your watchOS app. The system calls the [`main()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()) method to launch your app; you never call it yourself. Your app can have exactly one entry point, which you mark with the `@main` attribute.

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main())*