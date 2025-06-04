# deviceOrientationDidChange()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the device’s orientation has changed.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor optional func deviceOrientationDidChange()
```

## Overview

WatchKit calls this method when the [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) object’s  [`wristLocation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation), [`crownOrientation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation), or [`isAutorotated`](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated) properties change.

## See Also

- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange())*