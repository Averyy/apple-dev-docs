# initiallyInteractive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the transition started as an interactive transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var initiallyInteractive: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL initiallyInteractive;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the transition was initiated interactively and the [`isAnimated`](./isanimated.md) property is also set to [`true`](../../Swift/true.md); otherwise, the value is [`false`](../../Swift/false.md). The value of this property doesn’t change during the course of a transition. To determine whether the transition is currently interactive, use the [`isInteractive`](./isinteractive.md) method instead.

## See Also

### Getting the transition state
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isAnimated: Bool](./isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive)*