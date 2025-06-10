# press(forDuration:thenDragTo:withVelocity:thenHoldForDuration:)

**Framework**: XCUIAutomation  
**Kind**: method

Initiates a press-and-hold gesture, drags to another coordinate with a velocity you specify, and holds for a duration you specify.

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
func press(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate, withVelocity velocity: XCUIGestureVelocity, thenHoldForDuration holdDuration: TimeInterval)
```

#### Discussion

This method is available in iOS and for Touch Bar interactions in macOS.

## Parameters

- `duration`: The duration of the initial press-and-hold gesture.
- `otherCoordinate`: The coordinate over which to finish the drag.
- `velocity`: The speed at which to move from the initial press position to the other element, expressed in pixels per second.
- `holdDuration`: The duration for which to hold over the other coordinate after dragging.

## See Also

- [func tap()](xcuicoordinate/tap.md)
  Sends a tap event at the coordinate.
- [func doubleTap()](xcuicoordinate/doubletap.md)
  Sends a double-tap event at the coordinate.
- [func press(forDuration: TimeInterval)](xcuicoordinate/press(forduration:).md)
  Initiates a press-and-hold gesture at the coordinate, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](xcuicoordinate/press(forduration:thendragto:).md)
  Initiates a press-and-hold gesture at the coordinate, then drags to another coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/press(forduration:thendragto:withvelocity:thenholdforduration:))*