# swipeDown(withVelocity:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a swipe-down gesture with a velocity you specify.

**Availability**:
- watchOS
- Xcode 16.3+

> **Deprecated**: Use [`swipeDown(velocity:)`](./swipedown%28velocity%29.md) instead.

## Declaration

```swift
@MainActor
@nonobjc @preconcurrency func swipeDown(withVelocity velocity: XCUIGestureVelocity)
```

## Parameters

- `velocity`: The speed at which to perform the swipe-down gesture, expressed in pixels per second.

## See Also

### Deprecated methods
- [func swipeUp(withVelocity: XCUIGestureVelocity)](./swipeup%28withvelocity%29.md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeLeft(withVelocity: XCUIGestureVelocity)](./swipeleft%28withvelocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight(withVelocity: XCUIGestureVelocity)](./swiperight%28withvelocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/swipedown(withvelocity:))*