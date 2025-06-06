# VNDetectHorizonRequest

**Framework**: Vision  
**Kind**: class

An image-analysis request that determines the horizon angle in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNDetectHorizonRequest
```

## Topics

### Accessing the Results
- [var results: [VNHorizonObservation]?](vndetecthorizonrequest/results.md)
  The results of the horizon detection request.
### Identifying Request Revisions
- [let VNDetectHorizonRequestRevision1: Int](vndetecthorizonrequestrevision1.md)
  A constant for specifying revision 1 of the horizon detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VNHorizonObservation](vnhorizonobservation.md)
  The horizon angle information that an image-analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthorizonrequest)*