# initialVelocity

**Framework**: UIKit  
**Kind**: property

The target property’s rate of change at the start of a spring animation, enabling a smooth transition into the animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var initialVelocity: CGVector { get }
```

#### Discussion

To create a smooth transition from an object in motion into a spring animation, initialize the spring timing parameters with an initial velocity. One common use of this property is to animate a view to a final resting position at the end of a pan gesture.

For view position animations, both components of the initial velocity vector are considered. Each component specifies the initial rate of change along the respective `x` and `y` axes, normalized to the total distance of the animation. To calculate an initial velocity vector:

1. Start with a velocity of the view in points per second. For example, when moving a view using a [`UIPanGestureRecognizer`](uipangesturerecognizer.md), you can use [`velocity(in:)`](uipangesturerecognizer/velocity(in:).md) for this starting value.
2. Calculate the `x` and `y` distance, in points, from the view’s current position to the final position.
3. Set the `dx` component of the initial velocity vector to the `x` velocity divided by the `x` distance. If the `x` distance is `0`, set `dx` to `0`.
4. Set the `dy` component to the `y` velocity divided by the `y` distance. If the `y` distance is `0`, set `dy` to `0`.

The following example shows a function that performs this calculation using a velocity from the pan gesture recognizer and the view’s current and final positions.

```swift
func initialAnimationVelocity(for gestureVelocity: CGPoint, from currentPosition: CGPoint, to finalPosition: CGPoint) -> CGVector {
    var animationVelocity = CGVector.zero
    let xDistance = finalPosition.x - currentPosition.x
    let yDistance = finalPosition.y - currentPosition.y
    if xDistance != 0 {
        animationVelocity.dx = gestureVelocity.x / xDistance
    }
    if yDistance != 0 {
        animationVelocity.dy = gestureVelocity.y / yDistance
    }
    return animationVelocity
}
```

The following example shows how a view controller can create a property animator with spring timing parameters. The view controller passes the result of `initialAnimationVelocity` to the spring timing parameters’ initializer. In this example, `draggedView` is an outlet of the view controller. The value of `destination` is the final resting position of `draggedView`.

```swift
let panRecognizer: UIPanGestureRecognizer = ... // pan recognizer attached to draggedView
let velocity = panRecognizer.velocity(in: view)
let initialVelocity = initialAnimationVelocity(for: velocity, from: draggedView.center, to: destination)

let parameters = UISpringTimingParameters(dampingRatio: dampingRatio, initialVelocity: initialVelocity)
let animator = UIViewPropertyAnimator(duration: animationDuration, timingParameters: parameters)

animator.addAnimations {
    self.draggedView.center = destination
}
```

For other types of animations where the property value has a single dimension, such as a view’s `alpha`, only the `dx` component is considered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/initialvelocity)*