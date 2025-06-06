# animationEnded(_:)

**Framework**: UIKit  
**Kind**: method

Tells your animator object that the transition animations have finished.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func animationEnded(_ transitionCompleted: Bool)
```

#### Discussion

UIKit calls this method at the end of a transition to let you know the results. Use this method to perform any final cleanup operations required by your transition animator when the transition finishes.

## Parameters

- `transitionCompleted`: Contains the value   if the transition completed successfully and the new view controller is now displayed or   if the transition was canceled and the original view controller is still visible.

## See Also

- [func animateTransition(using: any UIViewControllerContextTransitioning)](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md)
  Tells your animator object to perform the transition animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/animationended(_:))*