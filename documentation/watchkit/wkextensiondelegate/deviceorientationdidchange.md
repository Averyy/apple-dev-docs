# deviceOrientationDidChange()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the device’s orientation has changed.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor optional func deviceOrientationDidChange()
```

## Overview

This method is called when the [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) object’s  [`wristLocation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation), [`crownOrientation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation), or [`isAutorotated`](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated) properties change.

## See Also

- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()))
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()))
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange())*