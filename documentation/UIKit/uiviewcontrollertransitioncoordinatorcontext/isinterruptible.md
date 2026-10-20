# isInterruptible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the transition animations can be interrupted.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isInterruptible: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isInterruptible;
```

## See Also

### Getting the transition state
- [var initiallyInteractive: Bool](./initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isInteractive: Bool](./isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isAnimated: Bool](./isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinterruptible)*