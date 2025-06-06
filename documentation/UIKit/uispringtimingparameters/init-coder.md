# init(coder:)

**Framework**: UIKit  
**Kind**: init

Creates a timing parameters object from data in an unarchiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## See Also

- [init()](uispringtimingparameters/init.md)
  Creates a default timing parameters object.
- [convenience init(dampingRatio: CGFloat)](uispringtimingparameters/init(dampingratio:).md)
  Creates a timing parameters object with the specified damping ratio.
- [init(dampingRatio: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(dampingratio:initialvelocity:).md)
  Creates a timing parameters object with the specified damping ratio and initial velocity.
- [init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity: CGVector)](uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:).md)
  Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(coder:))*