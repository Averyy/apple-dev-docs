# uuid

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A unique alphanumeric value that the framework assigns the observation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
var uuid: UUID { get }
```

## See Also

### Inspecting an observation
- [var confidence: Float](./confidence.md)
  The level of confidence in the observation’s accuracy.
- [var description: String](./description.md)
  A textual representation of this instance.
- [var originatingRequestDescriptor: RequestDescriptor?](./originatingrequestdescriptor.md)
  The descriptor of the request that produces the observation.
- [enum RequestDescriptor](../requestdescriptor.md)
  A type that describes the request and revision combination.
- [var timeRange: CMTimeRange?](./timerange.md)
  The time range of the reported observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionobservation/uuid)*