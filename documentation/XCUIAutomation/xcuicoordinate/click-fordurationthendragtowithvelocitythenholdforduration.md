# click(forDuration:thenDragTo:withVelocity:thenHoldForDuration:)

**Framework**: Xcuiautomation  
**Kind**: method

Clicks and holds for a duration, drags at a velocity, and holds over the other coordinate for a duration, all of which you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func click(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate, withVelocity velocity: XCUIGestureVelocity, thenHoldForDuration holdDuration: TimeInterval)
```

## Parameters

- `duration`: The duration of the initial click and hold.
- `otherCoordinate`: The coordinate over which to finish the drag gesture.
- `velocity`: The speed at which to move from the initial click position to the other coordinate, expressed in pixels per second.
- `holdDuration`: The duration for which to hold over the other coordinate after dragging.

## See Also

- [func click()](xcuicoordinate/click.md)
  Sends a click event at the coordinate.
- [func click(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](xcuicoordinate/click(forduration:thendragto:).md)
  Clicks and holds for a duration you specify, then drags to the other coordinate.
- [func doubleClick()](xcuicoordinate/doubleclick.md)
  Sends a double-click event at the coordinate.
- [func rightClick()](xcuicoordinate/rightclick.md)
  Sends a Control-click event at the coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/click(forduration:thendragto:withvelocity:thenholdforduration:))*