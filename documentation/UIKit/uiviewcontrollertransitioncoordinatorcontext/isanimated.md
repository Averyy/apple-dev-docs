# isAnimated

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the transition is explicitly animated.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isAnimated: Bool { get }
```

#### Discussion

The value of this property is [`false`](https://developer.apple.com/documentation/swift/false) for custom transitions — transitions where the view controller’s [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property is set to [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md) — even when the transition is started by a call to the [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method. In nearly all other cases, the value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var initiallyInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isCancelled: Bool](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isanimated)*