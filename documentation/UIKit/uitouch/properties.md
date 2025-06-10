# UITouch.Properties

**Framework**: UIKit  
**Kind**: struct

A bit mask of touch properties that may get updated.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct Properties
```

## Topics

### Constants
- [static var force: UITouch.Properties](uitouch/properties/force.md)
  A touch property, representing force, in a bit mask.
- [static var azimuth: UITouch.Properties](uitouch/properties/azimuth.md)
  A touch property, representing azimuth, in a bit mask.
- [static var altitude: UITouch.Properties](uitouch/properties/altitude.md)
  A touch property, representing altitude, in a bit mask.
- [static var location: UITouch.Properties](uitouch/properties/location.md)
  A touch property, representing location, in a bit mask.
- [static var roll: UITouch.Properties](uitouch/properties/roll.md)
  A touch property, representing barrel-roll angle, in a bit mask.
### Initializers
- [init(rawValue: Int)](uitouch/properties/init(rawvalue:).md)
  Creates a structure that represents the properties of a touch object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var estimatedProperties: UITouch.Properties](uitouch/estimatedproperties.md)
  A set of touch properties whose values contain only estimates.
- [var estimatedPropertiesExpectingUpdates: UITouch.Properties](uitouch/estimatedpropertiesexpectingupdates.md)
  The set of touch properties for which updated values are expected in the future.
- [var estimationUpdateIndex: NSNumber?](uitouch/estimationupdateindex.md)
  An index number that lets you correlate an updated touch with the original touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/properties)*