# isInteractive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the transition is currently interactive.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isInteractive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isInteractive) BOOL interactive;
```

#### Discussion

Every interactive transition has at least one noninteractive segment — namely, when it’s completing. In addition, you can design an interactive transition to have intermediate segments that are noninteractive.

If the [`initiallyInteractive`](./initiallyinteractive.md) property is set to [`false`](../../Swift/false.md), the value of this property can be [`true`](../../Swift/true.md) only when the [`isInterruptible`](./isinterruptible.md) property is also [`true`](../../Swift/true.md).

## See Also

### Getting the transition state
- [var initiallyInteractive: Bool](./initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isAnimated: Bool](./isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](./isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinteractive)*