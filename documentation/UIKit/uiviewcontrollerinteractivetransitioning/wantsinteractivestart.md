# wantsInteractiveStart

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the transition is interactive when it starts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var wantsInteractiveStart: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the transition is interactive from the moment it starts. The property is [`false`](https://developer.apple.com/documentation/Swift/false) when the transition starts off as noninteractive. However, even a transition that starts off as noninteractive may become interactive later if it implements the [`interruptibleAnimator(using:)`](uiviewcontrolleranimatedtransitioning/interruptibleanimator(using:).md) method of the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol.

## See Also

- [func startInteractiveTransition(any UIViewControllerContextTransitioning)](uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:).md)
  Called when the system needs to set up the interactive portions of a view controller transition and start the animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/wantsinteractivestart)*