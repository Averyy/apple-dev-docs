# press(forDuration:thenDragTo:)

**Framework**: XCUIAutomation  
**Kind**: method

Initiates a press-and-hold gesture at the coordinate, then drags to another coordinate.

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
func press(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate)
```

#### Discussion

This method is available in iOS and for Touch Bar interactions in macOS.

## Parameters

- `duration`: The duration of the initial press-and-hold gesture.
- `otherCoordinate`: The coordinate to finish the drag gesture over.

## See Also

- [func tap()](xcuicoordinate/tap.md)
  Sends a tap event at the coordinate.
- [func doubleTap()](xcuicoordinate/doubletap.md)
  Sends a double-tap event at the coordinate.
- [func press(forDuration: TimeInterval)](xcuicoordinate/press(forduration:).md)
  Initiates a press-and-hold gesture at the coordinate, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuicoordinate/press(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Initiates a press-and-hold gesture, drags to another coordinate with a velocity you specify, and holds for a duration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/press(forduration:thendragto:))*