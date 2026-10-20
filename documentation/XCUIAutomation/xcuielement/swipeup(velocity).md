# swipeUp(velocity:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a swipe-up gesture with a velocity you specify.

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
func swipeUp(velocity: XCUIGestureVelocity)
```

```objc
- (void) swipeUpWithVelocity:(XCUIGestureVelocity) velocity;
```

## Parameters

- `velocity`: The speed at which to perform the swipe-up gesture, expressed in pixels per second.

## See Also

### Performing gestures
- [func swipeLeft()](./swipeleft%28%29.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](./swipeleft%28velocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](./swiperight%28%29.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](./swiperight%28velocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](./swipeup%28%29.md)
  Sends a swipe-up gesture.
- [func swipeDown()](./swipedown%28%29.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](./swipedown%28velocity%29.md)
  Sends a swipe-down gesture with a velocity you specify.
- [func pinch(withScale: CGFloat, velocity: CGFloat)](./pinch%28withscale,velocity%29.md)
  Sends a pinching gesture with two touches.
- [func rotate(CGFloat, withVelocity: CGFloat)](./rotate%28_,withvelocity%29.md)
  Sends a rotation gesture with two touches.
- [struct XCUIGestureVelocity](../xcuigesturevelocity.md)
  A value that describes how fast a gesture moves across the screen, in pixels per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/swipeup(velocity:))*