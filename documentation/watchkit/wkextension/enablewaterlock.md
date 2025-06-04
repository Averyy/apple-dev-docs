# enableWaterLock()

**Framework**: WatchKit  
**Kind**: method

Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
func enableWaterLock()
```

#### Discussion

The following rules apply when using Water Lock:

- You must call the [`enableWaterLock()`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock()) method from the main thread.
- You can only enable Water Lock when the app is running in the foreground during an active workout or location session.
- The app must be running on a supported device (the [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) object’s [`waterResistanceRating`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/waterresistancerating) property must be set to [`WKWaterResistanceRating.wr50`](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/wr50)).
- Water Lock remains active until the user unlocks it. You can’t programmatically unlock the watch.

## See Also

- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/globaltintcolor))
  The watchOS app’s global tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/enablewaterlock())*