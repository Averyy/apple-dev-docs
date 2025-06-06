# confidence

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The level of confidence in the observation’s accuracy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var confidence: Float { get }
```

#### Discussion

The Vision framework normalizes this value to `[0.0, 1.0]` under most circumstances. A value of `0.0` indicates no confidence. A value of `1.0` indicates highest confidence, or the observation doesn’t support or assign meaning to confidence.

## See Also

- [var uuid: UUID](visionobservation/uuid.md)
  A unique alphanumeric value that the framework assigns the observation.
- [var description: String](visionobservation/description.md)
  A textual representation of this instance.
- [var originatingRequestDescriptor: RequestDescriptor?](visionobservation/originatingrequestdescriptor.md)
  The descriptor of the request that produces the observation.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var timeRange: CMTimeRange?](visionobservation/timerange.md)
  The time range of the reported observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionobservation/confidence)*