# init(dampingRatio:initialVelocity:)

**Framework**: UIKit  
**Kind**: init

Creates a timing parameters object with the specified damping ratio and initial velocity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(dampingRatio ratio: CGFloat, initialVelocity velocity: CGVector)
```

#### Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

## Parameters

- `ratio`: The damping ratio to apply to the spring’s motion. To smoothly decelerate the animation without oscillation, specify a value of `1`. Specify values closer to `0` to create less damping and more oscillation.
- `velocity`: The target property’s initial rate of change at the start of the spring animation. If the target property doesn’t change, specify a vector with `dx` and `dy` components of `0`. For details about how to calculate this velocity, see [`initialVelocity`](uispringtimingparameters/initialvelocity.md).

## See Also

- [init()](uispringtimingparameters/init.md)
  Creates a default timing parameters object.
- [convenience init(dampingRatio: CGFloat)](uispringtimingparameters/init(dampingratio:).md)
  Creates a timing parameters object with the specified damping ratio.
- [init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:).md)
  Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [init?(coder: NSCoder)](uispringtimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(dampingratio:initialvelocity:))*