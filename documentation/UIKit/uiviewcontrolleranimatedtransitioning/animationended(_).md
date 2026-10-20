# animationEnded(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells your animator object that the transition animations have finished.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func animationEnded(_ transitionCompleted: Bool)
```

```objc
- (void) animationEnded:(BOOL) transitionCompleted;
```

#### Discussion

UIKit calls this method at the end of a transition to let you know the results. Use this method to perform any final cleanup operations required by your transition animator when the transition finishes.

## Parameters

- `transitionCompleted`: Contains the value [`true`](../../Swift/true.md) if the transition completed successfully and the new view controller is now displayed or [`false`](../../Swift/false.md) if the transition was canceled and the original view controller is still visible.

## See Also

### Performing a transition
- [func animateTransition(using: any UIViewControllerContextTransitioning)](./animatetransition%28using%29.md)
  Tells your animator object to perform the transition animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/animationended(_:))*