# isCancelled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether an interactive transition was canceled.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isCancelled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCancelled) BOOL cancelled;
```

## See Also

### Getting the transition state
- [var initiallyInteractive: Bool](./initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isAnimated: Bool](./isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/iscancelled)*