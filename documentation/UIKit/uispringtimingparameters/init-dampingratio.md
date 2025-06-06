# init(dampingRatio:)

**Framework**: UIKit  
**Kind**: init

Creates a timing parameters object with the specified damping ratio.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(dampingRatio ratio: CGFloat)
```

#### Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

#### Discussion

This method sets the initial velocity of any animated properties to `0.0`.

## Parameters

- `ratio`: The damping ratio for controlling the spring’s behavior. For more damping and less oscillation, specify a value of  . For less damping and more oscillation, specify values closer to  .

## See Also

- [init()](uispringtimingparameters/init.md)
  Creates a default timing parameters object.
- [init(dampingRatio: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(dampingratio:initialvelocity:).md)
  Creates a timing parameters object with the specified damping ratio and initial velocity.
- [init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:).md)
  Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [init?(coder: NSCoder)](uispringtimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(dampingratio:))*