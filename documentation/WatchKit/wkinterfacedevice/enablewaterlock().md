# enableWaterLock()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Disables the Apple Watch touch screen to prevent accidental taps while submerged.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func enableWaterLock()
```

```objc
- (void) enableWaterLock;
```

#### Discussion

The following rules apply when using Water Lock:

- You must call the [`enableWaterLock()`](./enablewaterlock%28%29.md) method from the main thread.
- You can only enable Water Lock when the app is running in the foreground during an active workout or location session.
- The app must be running on a supported device (the [`WKInterfaceDevice`](../wkinterfacedevice.md) object’s [`waterResistanceRating`](./waterresistancerating.md) property must be [`WKWaterResistanceRating.wr50`](../wkwaterresistancerating/wr50.md)).
- Water Lock remains active until the user unlocks it. You can’t programmatically unlock the watch.

## See Also

### Accessing Water Resistance and Lock
- [var waterResistanceRating: WKWaterResistanceRating](./waterresistancerating.md)
  The Apple Watch water-resistance rating.
- [enum WKWaterResistanceRating](../wkwaterresistancerating.md)
  Values indicating the water-resistance rating.
- [var isWaterLockEnabled: Bool](./iswaterlockenabled.md)
  A Boolean value that indicates whether the water lock is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock())*