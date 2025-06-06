# interruptibleAnimator(using:)

**Framework**: UIKit  
**Kind**: method

Returns the interruptible animator to use during the transition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func interruptibleAnimator(using transitionContext: any UIViewControllerContextTransitioning) -> any UIViewImplicitlyAnimating
```

#### Return Value

An animator object that supports the modification of its running animations.

#### Discussion

Implement this method when you want to perform your transitions using an interruptible animator object, such as a [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) object. You must return the same animator object for the duration of the transition.

## Parameters

- `transitionContext`: The context object containing information to use during the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/interruptibleanimator(using:))*