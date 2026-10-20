# click(forDuration:thenDragTo:withVelocity:thenHoldForDuration:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Clicks and holds for a duration, drags at a velocity, and holds over the other coordinate for a duration, all of which you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- Xcode 16.3+

## Declaration

```swift
func click(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate, withVelocity velocity: XCUIGestureVelocity, thenHoldForDuration holdDuration: TimeInterval)
```

```objc
- (void) clickForDuration:(NSTimeInterval) duration thenDragToCoordinate:(XCUICoordinate *) otherCoordinate withVelocity:(XCUIGestureVelocity) velocity thenHoldForDuration:(NSTimeInterval) holdDuration;
```

## Parameters

- `duration`: The duration of the initial click and hold.
- `otherCoordinate`: The coordinate over which to finish the drag gesture.
- `velocity`: The speed at which to move from the initial click position to the other coordinate, expressed in pixels per second.
- `holdDuration`: The duration for which to hold over the other coordinate after dragging.

## See Also

### Clicking
- [func click()](./click%28%29.md)
  Sends a click event at the coordinate.
- [func click(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](./click%28forduration,thendragto%29.md)
  Clicks and holds for a duration you specify, then drags to the other coordinate.
- [func doubleClick()](./doubleclick%28%29.md)
  Sends a double-click event at the coordinate.
- [func rightClick()](./rightclick%28%29.md)
  Sends a Control-click event at the coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/click(forduration:thendragto:withvelocity:thenholdforduration:))*