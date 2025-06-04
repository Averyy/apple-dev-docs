# WKAccessibilityIsVoiceOverRunning()

**Framework**: Watchkit  
**Kind**: func

Returns a Boolean value indicating whether VoiceOver is running.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func WKAccessibilityIsVoiceOverRunning() -> Bool
```

## Overview

[`true`](https://developer.apple.com/documentation/swift/true) if VoiceOver is currently running or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

## Discussion

You can use this function to customize your application’s UI specifically for VoiceOver users. For example, you might want UI elements that usually disappear quickly to persist onscreen for VoiceOver users. Note that you can also listen for the [`WKAccessibilityVoiceOverStatusChanged`](https://developer.apple.com/documentation/watchkit/wkaccessibilityvoiceoverstatuschanged) notification to find out when VoiceOver starts and stops.

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning())*