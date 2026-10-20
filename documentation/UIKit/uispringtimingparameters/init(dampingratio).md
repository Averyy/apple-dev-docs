# init(dampingRatio:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a timing parameters object with the specified damping ratio.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(dampingRatio ratio: CGFloat)
```

```objc
- (instancetype) initWithDampingRatio:(CGFloat) ratio;
```

#### Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

#### Discussion

This method sets the initial velocity of any animated properties to `0.0`.

## Parameters

- `ratio`: The damping ratio for controlling the spring’s behavior. For more damping and less oscillation, specify a value of `1`. For less damping and more oscillation, specify values closer to `0`.

## See Also

### Initializing a spring timing parameters object
- [init()](./init%28%29.md)
  Creates a default timing parameters object.
- [init(dampingRatio: CGFloat, initialVelocity: CGVector)](./init%28dampingratio,initialvelocity%29.md)
  Creates a timing parameters object with the specified damping ratio and initial velocity.
- [init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity: CGVector)](./init%28mass,stiffness,damping,initialvelocity%29.md)
  Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a timing parameters object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(dampingratio:))*