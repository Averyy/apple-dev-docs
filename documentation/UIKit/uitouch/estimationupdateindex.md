# estimationUpdateIndex

**Framework**: UIKit  
**Kind**: property

An index number that lets you correlate an updated touch with the original touch.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var estimationUpdateIndex: NSNumber? { get }
```

#### Discussion

This property contains a unique marker for the current touch data. When the touch contains estimated properties, save this index along with the rest of the touch data to your app’s data structures. When the system reports the actual touch values later, use this index to locate the original data in your app’s data structures and replace the estimated values you stored previously. For example, when a touch contains estimated properties, you might use this property as a key in a dictionary whose value is the object you use to store the touch data.

The value of this property increases monotonically for each touch that contains estimated properties. The value of this property is `nil` when the touch object does not contain either estimated or updated properties.

## See Also

- [var estimatedProperties: UITouch.Properties](uitouch/estimatedproperties.md)
  A set of touch properties whose values contain only estimates.
- [var estimatedPropertiesExpectingUpdates: UITouch.Properties](uitouch/estimatedpropertiesexpectingupdates.md)
  The set of touch properties for which updated values are expected in the future.
- [UITouch.Properties](uitouch/properties.md)
  A bit mask of touch properties that may get updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/estimationupdateindex)*