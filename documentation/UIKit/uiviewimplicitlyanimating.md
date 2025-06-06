# UIViewImplicitlyAnimating

**Framework**: UIKit  
**Kind**: protocol

An interface for modifying an animation while it’s running.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewImplicitlyAnimating : UIViewAnimating
```

#### Overview

Animator objects used in interruptible view controller transitions adopt the [`UIViewImplicitlyAnimating`](uiviewimplicitlyanimating.md) protocol to modify in-flight transition animations. This protocol also conforms to the [`UIViewAnimating`](uiviewanimating.md) protocol, which specifies methods for starting and stopping animations and for updating their state.

The [`UIViewPropertyAnimator`](uiviewpropertyanimator.md) class adopts this protocol and implements all of its methods. You can adopt this protocol in your own classes to implement custom animator objects. When adopting this protocol, it’s recommended that you implement all of the methods.

## Topics

### Modifying animations
- [func addAnimations(() -> Void)](uiviewimplicitlyanimating/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addAnimations(() -> Void, delayFactor: CGFloat)](uiviewimplicitlyanimating/addanimations(_:delayfactor:).md)
  Adds the specified animation block to the animator with a delay.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uiviewimplicitlyanimating/addcompletion(_:).md)
  Adds the specified completion block to the animator.
- [func continueAnimation(withTimingParameters: (any UITimingCurveProvider)?, durationFactor: CGFloat)](uiviewimplicitlyanimating/continueanimation(withtimingparameters:durationfactor:).md)
  Adjusts the final timing and duration of a paused animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIViewAnimating](uiviewanimating.md)
### Conforming Types
- [UIViewPropertyAnimator](uiviewpropertyanimator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating)*