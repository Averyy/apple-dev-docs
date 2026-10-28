# isAnimated

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the transition is explicitly animated.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isAnimated: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAnimated) BOOL animated;
```

## Discussion

The value of this property is [`false`](../../Swift/false.md) for custom transitions — transitions where the view controller’s [`modalPresentationStyle`](../uiviewcontroller/modalpresentationstyle.md) property is set to [`UIModalPresentationStyle.custom`](../uimodalpresentationstyle/custom.md) — even when the transition is started by a call to the [`animateTransition(using:)`](../uiviewcontrolleranimatedtransitioning/animatetransition%28using%29.md) method. In nearly all other cases, the value of this property is [`true`](../../Swift/true.md).

## See Also

### Getting the transition state
- [var initiallyInteractive: Bool](./initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isanimated)*