# timeRange

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The time range of the reported observation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var timeRange: CMTimeRange? { get }
```

#### Discussion

When evaluating a sequence of image buffers, use this property to determine each observation’s start time and duration. If a request doesn’t support time ranges, or the time range is unknown, the value of this property is `nil`.

## See Also

- [var uuid: UUID](visionobservation/uuid.md)
  A unique alphanumeric value that the framework assigns the observation.
- [var confidence: Float](visionobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [var description: String](visionobservation/description.md)
  A textual representation of this instance.
- [var originatingRequestDescriptor: RequestDescriptor?](visionobservation/originatingrequestdescriptor.md)
  The descriptor of the request that produces the observation.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionobservation/timerange)*