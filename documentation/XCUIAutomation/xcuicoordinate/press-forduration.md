# press(forDuration:)

**Framework**: XCUIAutomation  
**Kind**: method

Initiates a press-and-hold gesture at the coordinate, holding for the duration you specify.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func press(forDuration duration: TimeInterval)
```

## Parameters

- `duration`: The duration of the press, in seconds.

## See Also

- [func tap()](xcuicoordinate/tap.md)
  Sends a tap event at the coordinate.
- [func doubleTap()](xcuicoordinate/doubletap.md)
  Sends a double-tap event at the coordinate.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](xcuicoordinate/press(forduration:thendragto:).md)
  Initiates a press-and-hold gesture at the coordinate, then drags to another coordinate.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuicoordinate/press(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Initiates a press-and-hold gesture, drags to another coordinate with a velocity you specify, and holds for a duration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/press(forduration:))*