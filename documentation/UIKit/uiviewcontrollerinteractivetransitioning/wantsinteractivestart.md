# wantsInteractiveStart

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the transition is interactive when it starts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional var wantsInteractiveStart: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL wantsInteractiveStart;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the transition is interactive from the moment it starts. The property is [`false`](../../Swift/false.md) when the transition starts off as noninteractive. However, even a transition that starts off as noninteractive may become interactive later if it implements the [`interruptibleAnimator(using:)`](../uiviewcontrolleranimatedtransitioning/interruptibleanimator%28using%29.md) method of the [`UIViewControllerAnimatedTransitioning`](../uiviewcontrolleranimatedtransitioning.md) protocol.

## See Also

### Starting an interactive transition
- [func startInteractiveTransition(any UIViewControllerContextTransitioning)](./startinteractivetransition%28_%29.md)
  Called when the system needs to set up the interactive portions of a view controller transition and start the animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/wantsinteractivestart)*