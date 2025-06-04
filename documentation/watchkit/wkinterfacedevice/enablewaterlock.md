# enableWaterLock()

**Framework**: WatchKit  
**Kind**: method

Disables the Apple Watch touch screen to prevent accidental taps while submerged.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func enableWaterLock()
```

#### Discussion

The following rules apply when using Water Lock:

- You must call the [`enableWaterLock()`](wkinterfacedevice/enablewaterlock().md) method from the main thread.
- You can only enable Water Lock when the app is running in the foreground during an active workout or location session.
- The app must be running on a supported device (the [`WKInterfaceDevice`](wkinterfacedevice.md) object’s [`waterResistanceRating`](wkinterfacedevice/waterresistancerating.md) property must be [`WKWaterResistanceRating.wr50`](wkwaterresistancerating/wr50.md)).
- Water Lock remains active until the user unlocks it. You can’t programmatically unlock the watch.

## See Also

- [var waterResistanceRating: WKWaterResistanceRating](wkinterfacedevice/waterresistancerating.md)
  The Apple Watch water-resistance rating.
- [enum WKWaterResistanceRating](wkwaterresistancerating.md)
  Values indicating the water-resistance rating.
- [var isWaterLockEnabled: Bool](wkinterfacedevice/iswaterlockenabled.md)
  A Boolean value that indicates whether the water lock is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock())*