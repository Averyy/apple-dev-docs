# initiallyInteractive

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the transition started as an interactive transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var initiallyInteractive: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the transition was initiated interactively and the [`isAnimated`](uiviewcontrollertransitioncoordinatorcontext/isanimated.md) property is also set to [`true`](https://developer.apple.com/documentation/swift/true); otherwise, the value is [`false`](https://developer.apple.com/documentation/swift/false). The value of this property doesn’t change during the course of a transition. To determine whether the transition is currently interactive, use the [`isInteractive`](uiviewcontrollertransitioncoordinatorcontext/isinteractive.md) method instead.

## See Also

- [var isInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isAnimated: Bool](uiviewcontrollertransitioncoordinatorcontext/isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive)*