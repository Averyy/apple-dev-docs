# VNDetectHorizonRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNDetectHorizonRequest : VNImageBasedRequest
```

## Topics

### Accessing the Results
- [var results: [VNHorizonObservation]?](./vndetecthorizonrequest/results.md)
  The results of the horizon detection request.
### Identifying Request Revisions
- [var VNDetectHorizonRequestRevision1: Int](./vndetecthorizonrequestrevision1.md)
  A constant for specifying revision 1 of the horizon detection request.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Horizon detection
- [class VNHorizonObservation](./vnhorizonobservation.md)
  The horizon angle information that an image-analysis request detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthorizonrequest)*