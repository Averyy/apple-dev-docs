# WKAccessibilityIsReduceMotionEnabled()

**Framework**: Watchkit  
**Kind**: func

Returns a Boolean value indicating whether reduced motion is enabled.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func WKAccessibilityIsReduceMotionEnabled() -> Bool
```

## Overview

You can use this function to customize your application’s UI when reduced motion is enabled. Note that you can also listen for the [`WKAccessibilityReduceMotionStatusDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/2915218-wkaccessibilityreducemotionstatu) (Swift) or [`WKAccessibilityReduceMotionStatusDidChangeNotification`](https://developer.apple.com/documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification) (Objective-C) notification to find out when VoiceOver starts and stops.

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled())*