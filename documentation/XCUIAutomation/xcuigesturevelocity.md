# XCUIGestureVelocity

**Framework**: XCUIAutomation  
**Kind**: struct

A value that describes how fast a gesture moves across the screen, in pixels per second.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
struct XCUIGestureVelocity
```

## Topics

### Creating a gesture velocity
- [init(CGFloat)](xcuigesturevelocity/init(_:).md)
  Creates a gesture velocity, expressed as a float.
- [init(integerLiteral: Int)](xcuigesturevelocity/init(integerliteral:).md)
  Creates a gesture velocity with an integer value.
- [init(floatLiteral: XCUIGestureVelocity.FloatLiteralType)](xcuigesturevelocity/init(floatliteral:).md)
  Creates a gesture velocity with a float value.
- [init(rawValue: CGFloat)](xcuigesturevelocity/init(rawvalue:).md)
  Creates a gesture velocity with a raw value, expressed as a float.
- [XCUIGestureVelocity.IntegerLiteralType](xcuigesturevelocity/integerliteraltype.md)
  A type that specifies a gesture velocity with an integer literal.
- [XCUIGestureVelocity.FloatLiteralType](xcuigesturevelocity/floatliteraltype.md)
  The native type that specifies the gesture velocity value.
### Using typical gesture velocities
- [static let `default`: XCUIGestureVelocity](xcuigesturevelocity/default.md)
  A value representing a default gesture velocity.
- [static let fast: XCUIGestureVelocity](xcuigesturevelocity/fast.md)
  A value representing a fast gesture velocity.
- [static let slow: XCUIGestureVelocity](xcuigesturevelocity/slow.md)
  A value representing a slow gesture velocity.
### Default Implementations
- [Equatable Implementations](xcuigesturevelocity/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](xcuigesturevelocity/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](xcuigesturevelocity/expressiblebyintegerliteral-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func pinch(withScale: CGFloat, velocity: CGFloat)](xcuielement/pinch(withscale:velocity:).md)
  Sends a pinching gesture with two touches.
- [func rotate(CGFloat, withVelocity: CGFloat)](xcuielement/rotate(_:withvelocity:).md)
  Sends a rotation gesture with two touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuigesturevelocity)*