# hasPrecisionRecallCurve

**Framework**: Vision  
**Kind**: property

A Boolean value that indicates whether the observation contains precision and recall curves.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var hasPrecisionRecallCurve: Bool { get }
```

#### Discussion

If this property is `true`, then you can call precision and recall-related methods in this observation.

If this property is `false`, then the precision and recall-related methods don’t return meaningful data.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let identifier: String](classificationobservation/identifier.md)
  The classification label that identifies the type of observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/classificationobservation/hasprecisionrecallcurve)*