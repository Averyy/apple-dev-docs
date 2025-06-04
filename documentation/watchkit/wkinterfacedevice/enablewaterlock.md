# enableWaterLock()

**Framework**: Watchkit  
**Kind**: method

Disables the Apple Watch touch screen to prevent accidental taps while submerged.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func enableWaterLock()
```

## Overview

The following rules apply when using Water Lock:

- You must call the [`enableWaterLock()`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock()) method from the main thread.
- You can only enable Water Lock when the app is running in the foreground during an active workout or location session.
- The app must be running on a supported device (the [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) object’s [`waterResistanceRating`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/waterresistancerating) property must be [`WKWaterResistanceRating.wr50`](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/wr50)).
- Water Lock remains active until the user unlocks it. You can’t programmatically unlock the watch.

## See Also

- [var waterResistanceRating: WKWaterResistanceRating](waterresistancerating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/waterresistancerating))
- [enum WKWaterResistanceRating](wkwaterresistancerating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating))
- [var isWaterLockEnabled: Bool](iswaterlockenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/iswaterlockenabled))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock())*