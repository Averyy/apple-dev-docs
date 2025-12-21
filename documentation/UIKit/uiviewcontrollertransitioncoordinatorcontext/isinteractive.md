# isInteractive

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the transition is currently interactive.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isInteractive: Bool { get }
```

#### Discussion

Every interactive transition has at least one noninteractive segment — namely, when it’s completing. In addition, you can design an interactive transition to have intermediate segments that are noninteractive.

If the [`initiallyInteractive`](uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.md) property is set to [`false`](https://developer.apple.com/documentation/Swift/false), the value of this property can be [`true`](https://developer.apple.com/documentation/Swift/true) only when the [`isInterruptible`](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md) property is also [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var initiallyInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isAnimated: Bool](uiviewcontrollertransitioncoordinatorcontext/isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinteractive)*