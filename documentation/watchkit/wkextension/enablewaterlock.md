# enableWaterLock()

**Framework**: Watchkit  
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

- You must call the [`enableWaterLock()`](wkinterfacedevice/enablewaterlock().md) method from the main thread.
- You can only enable Water Lock when the app is running in the foreground during an active workout or location session.
- The app must be running on a supported device (the [`WKInterfaceDevice`](wkinterfacedevice.md) object’s [`waterResistanceRating`](wkinterfacedevice/waterresistancerating.md) property must be set to [`WKWaterResistanceRating.wr50`](wkwaterresistancerating/wr50.md)).
- Water Lock remains active until the user unlocks it. You can’t programmatically unlock the watch.

## See Also

- [var isAutorotating: Bool](wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [var globalTintColor: UIColor](wkextension/globaltintcolor.md)
  The watchOS app’s global tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/enablewaterlock())*