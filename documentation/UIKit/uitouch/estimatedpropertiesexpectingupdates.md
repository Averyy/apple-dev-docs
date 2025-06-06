# estimatedPropertiesExpectingUpdates

**Framework**: UIKit  
**Kind**: property

The set of touch properties for which updated values are expected in the future.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var estimatedPropertiesExpectingUpdates: UITouch.Properties { get }
```

#### Discussion

This property contains a bitmask of constants indicating which touch properties could not be reported immediately, and for which an update is expected later. When this property contains a non empty set, you can expect UIKit to call the [`touchesEstimatedPropertiesUpdated(_:)`](uiresponder/touchesestimatedpropertiesupdated(_:).md) method of your responder or gesture recognizer at a later time with the updated values for the given properties. Attach the value in the [`estimationUpdateIndex`](uitouch/estimationupdateindex.md) property to your app’s copy of the touch data. When UIKit calls the [`touchesEstimatedPropertiesUpdated(_:)`](uiresponder/touchesestimatedpropertiesupdated(_:).md) method later, use the estimation update index of the new touch to locate and update your app’s copy of the touch data.

When this property contains an empty set, no more updates are expected. In that scenario, the estimated or updated value is the final value.

## See Also

- [var estimatedProperties: UITouch.Properties](uitouch/estimatedproperties.md)
  A set of touch properties whose values contain only estimates.
- [UITouch.Properties](uitouch/properties.md)
  A bit mask of touch properties that may get updated.
- [var estimationUpdateIndex: NSNumber?](uitouch/estimationupdateindex.md)
  An index number that lets you correlate an updated touch with the original touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/estimatedpropertiesexpectingupdates)*