# UITouch.Properties

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UITouchProperties : NSInteger;
```

## Topics

### Constants
- [static var force: UITouch.Properties](./properties/force.md)
  A touch property, representing force, in a bit mask.
- [static var azimuth: UITouch.Properties](./properties/azimuth.md)
  A touch property, representing azimuth, in a bit mask.
- [static var altitude: UITouch.Properties](./properties/altitude.md)
  A touch property, representing altitude, in a bit mask.
- [static var location: UITouch.Properties](./properties/location.md)
  A touch property, representing location, in a bit mask.
- [static var roll: UITouch.Properties](./properties/roll.md)
  A touch property, representing barrel-roll angle, in a bit mask.
### Initializers
- [init(rawValue: Int)](./properties/init%28rawvalue%29.md)
  Creates a structure that represents the properties of a touch object.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing estimated touch attributes
- [var estimatedProperties: UITouch.Properties](./estimatedproperties.md)
  A set of touch properties whose values contain only estimates.
- [var estimatedPropertiesExpectingUpdates: UITouch.Properties](./estimatedpropertiesexpectingupdates.md)
  The set of touch properties for which updated values are expected in the future.
- [var estimationUpdateIndex: NSNumber?](./estimationupdateindex.md)
  An index number that lets you correlate an updated touch with the original touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/properties)*