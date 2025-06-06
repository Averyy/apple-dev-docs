# init(mass:stiffness:damping:initialVelocity:)

**Framework**: UIKit  
**Kind**: init

Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity velocity: CGVector)
```

#### Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

#### Discussion

The damping ratio for the spring is computed from the formula `damping` / (2 * sqrt (`stiffness` * `mass`)).

## Parameters

- `mass`: The effective mass of the animated property. This value must be greater than  .
- `stiffness`: The spring stiffness coefficient. Higher values correspond to a stiffer spring that yields a greater amount of force for moving objects.
- `damping`: The damping force to apply to the spring’s motion. This value is used to compute the damping ratio.
- `velocity`: For details about how to calculate this velocity, see  .

## See Also

- [init()](uispringtimingparameters/init.md)
  Creates a default timing parameters object.
- [convenience init(dampingRatio: CGFloat)](uispringtimingparameters/init(dampingratio:).md)
  Creates a timing parameters object with the specified damping ratio.
- [init(dampingRatio: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(dampingratio:initialvelocity:).md)
  Creates a timing parameters object with the specified damping ratio and initial velocity.
- [init?(coder: NSCoder)](uispringtimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:))*