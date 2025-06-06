# pinch(withScale:velocity:)

**Framework**: Xcuiautomation  
**Kind**: method

Sends a pinching gesture with two touches.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func pinch(withScale scale: CGFloat, velocity: CGFloat)
```

#### Discussion

The system makes a best effort to synthesize the requested scale and velocity, but absolute accuracy isn’t guaranteed. Some values may not be possible based on the size of the element’s frame, and they result in test failures.

## Parameters

- `scale`: The scale of the pinch gesture.  Use a scale between 0 and 1 to “pinch close” or zoom out and a scale greater than 1 to “pinch open” or zoom in.
- `velocity`: The velocity of the pinch in scale factor per second.

## See Also

- [func swipeLeft()](xcuielement/swipeleft.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](xcuielement/swipeleft(velocity:).md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](xcuielement/swiperight.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](xcuielement/swiperight(velocity:).md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](xcuielement/swipeup.md)
  Sends a swipe-up gesture.
- [func swipeUp(velocity: XCUIGestureVelocity)](xcuielement/swipeup(velocity:).md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeDown()](xcuielement/swipedown.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](xcuielement/swipedown(velocity:).md)
  Sends a swipe-down gesture with a velocity you specify.
- [func rotate(CGFloat, withVelocity: CGFloat)](xcuielement/rotate(_:withvelocity:).md)
  Sends a rotation gesture with two touches.
- [struct XCUIGestureVelocity](xcuigesturevelocity.md)
  A value that describes how fast a gesture moves across the screen, in pixels per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/pinch(withscale:velocity:))*