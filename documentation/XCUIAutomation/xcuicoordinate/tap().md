# tap()

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a tap event at the coordinate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
func tap()
```

```objc
- (void) tap;
```

#### Discussion

This method is available in iOS and for Touch Bar interactions in macOS.

## See Also

### Tapping and pressing
- [func doubleTap()](./doubletap%28%29.md)
  Sends a double-tap event at the coordinate.
- [func press(forDuration: TimeInterval)](./press%28forduration%29.md)
  Initiates a press-and-hold gesture at the coordinate, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate)](./press%28forduration,thendragto%29.md)
  Initiates a press-and-hold gesture at the coordinate, then drags to another coordinate.
- [func press(forDuration: TimeInterval, thenDragTo: XCUICoordinate, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./press%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Initiates a press-and-hold gesture, drags to another coordinate with a velocity you specify, and holds for a duration you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/tap())*