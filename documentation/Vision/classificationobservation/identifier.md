# identifier

**Framework**: Vision  
**Kind**: property

The classification label that identifies the type of observation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let identifier: String
```

#### Discussion

An example classification could be a string like ‘cat’ or ‘hotdog’. The model used for the classification defines the domain of strings that may result. Usually, these strings aren’t localized technical labels not meant for direct presentation to the user.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var hasPrecisionRecallCurve: Bool](classificationobservation/hasprecisionrecallcurve.md)
  A Boolean value that indicates whether the observation contains precision and recall curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation/identifier)*