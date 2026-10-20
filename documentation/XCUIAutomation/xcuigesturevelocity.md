# XCUIGestureVelocity

**Framework**: XCUIAutomation  
**Kind**: struct  
**Role**: Structure

A value that describes how fast a gesture moves across the screen, in pixels per second.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
struct XCUIGestureVelocity
```

```c
typedef CGFloat XCUIGestureVelocity;
```

## Topics

### Creating a gesture velocity
- [init(CGFloat)](./xcuigesturevelocity/init%28_%29.md)
  Creates a gesture velocity, expressed as a float.
- [init(rawValue: CGFloat)](./xcuigesturevelocity/init%28rawvalue%29.md)
  Creates a gesture velocity with a raw value, expressed as a float.
### Using typical gesture velocities
- [static let `default`: XCUIGestureVelocity](./xcuigesturevelocity/default.md)
  A value representing a default gesture velocity.
- [static let fast: XCUIGestureVelocity](./xcuigesturevelocity/fast.md)
  A value representing a fast gesture velocity.
- [static let slow: XCUIGestureVelocity](./xcuigesturevelocity/slow.md)
  A value representing a slow gesture velocity.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Performing gestures
- [func swipeLeft()](./xcuielement/swipeleft%28%29.md)
  Sends a swipe-left gesture.
- [func swipeLeft(velocity: XCUIGestureVelocity)](./xcuielement/swipeleft%28velocity%29.md)
  Sends a swipe-left gesture with a velocity you specify.
- [func swipeRight()](./xcuielement/swiperight%28%29.md)
  Sends a swipe-right gesture.
- [func swipeRight(velocity: XCUIGestureVelocity)](./xcuielement/swiperight%28velocity%29.md)
  Sends a swipe-right gesture with a velocity you specify.
- [func swipeUp()](./xcuielement/swipeup%28%29.md)
  Sends a swipe-up gesture.
- [func swipeUp(velocity: XCUIGestureVelocity)](./xcuielement/swipeup%28velocity%29.md)
  Sends a swipe-up gesture with a velocity you specify.
- [func swipeDown()](./xcuielement/swipedown%28%29.md)
  Sends a swipe-down gesture.
- [func swipeDown(velocity: XCUIGestureVelocity)](./xcuielement/swipedown%28velocity%29.md)
  Sends a swipe-down gesture with a velocity you specify.
- [func pinch(withScale: CGFloat, velocity: CGFloat)](./xcuielement/pinch%28withscale,velocity%29.md)
  Sends a pinching gesture with two touches.
- [func rotate(CGFloat, withVelocity: CGFloat)](./xcuielement/rotate%28_,withvelocity%29.md)
  Sends a rotation gesture with two touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuigesturevelocity)*