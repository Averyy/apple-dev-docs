# click(forDuration:thenDragTo:)

**Framework**: XCUIAutomation  
**Kind**: method

Clicks and holds for a duration you specify, then drags to the other coordinate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func click(forDuration duration: TimeInterval, thenDragTo otherCoordinate: XCUICoordinate)
```

## Parameters

- `duration`: The duration of the initial click and hold.
- `otherCoordinate`: The coordinate over which to finish the drag gesture.

## See Also

- [func click()](xcuicoordinate/click.md)
  Sends a click event at the coordinate.
- [func click(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuicoordinate/click(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Clicks and holds for a duration, drags at a velocity, and holds over the other coordinate for a duration, all of which you specify.
- [func doubleClick()](xcuicoordinate/doubleclick.md)
  Sends a double-click event at the coordinate.
- [func rightClick()](xcuicoordinate/rightclick.md)
  Sends a Control-click event at the coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/click(forduration:thendragto:))*