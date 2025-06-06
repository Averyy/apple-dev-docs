# init()

**Framework**: UIKit  
**Kind**: init

Creates a default timing parameters object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init()
```

#### Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

#### Discussion

This method sets the initial velocity of any animated properties to `0.0` and sets the damping ratio to `4.56`.

## See Also

- [convenience init(dampingRatio: CGFloat)](uispringtimingparameters/init(dampingratio:).md)
  Creates a timing parameters object with the specified damping ratio.
- [init(dampingRatio: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(dampingratio:initialvelocity:).md)
  Creates a timing parameters object with the specified damping ratio and initial velocity.
- [init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:).md)
  Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [init?(coder: NSCoder)](uispringtimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init())*