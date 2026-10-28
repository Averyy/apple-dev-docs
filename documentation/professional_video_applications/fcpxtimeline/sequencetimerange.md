# sequenceTimeRange

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The time range of an active sequence in the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
var sequenceTimeRange: CMTimeRange { get }
```

```objc
@property (nonatomic, readonly) CMTimeRange sequenceTimeRange;
```

## Discussion

The `sequenceTimeRange` property has a time range that includes a start time and the duration of a sequence.

## See Also

### Fetching Details of an Active Sequence
- [var activeSequence: FCPXSequence?](./activesequence.md)
  The sequence played in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline/sequencetimerange)*