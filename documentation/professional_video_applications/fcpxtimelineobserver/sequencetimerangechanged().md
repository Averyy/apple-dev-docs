# sequenceTimeRangeChanged()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

A callback method that gets invoked when the time range of an active sequence changes in the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
optional func sequenceTimeRangeChanged()
```

```objc
- (void) sequenceTimeRangeChanged;
```

#### Discussion

Inside this method implementation, obtain the new time range by using the [`sequenceTimeRange`](../fcpxtimeline/sequencetimerange.md) property. By observing for the changes in the time range of an active sequence, an extension can verify whether the data it has for the sequence is in sync with what is presented in Final Cut Pro.

## See Also

### Handling Final Cut Pro Timeline Changes
- [func activeSequenceChanged()](./activesequencechanged%28%29.md)
  A callback method that gets invoked when there is a change in the current timeline sequence.
- [func playheadTimeChanged()](./playheadtimechanged%28%29.md)
  A callback method that gets invoked when the playhead position changes in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimelineobserver/sequencetimerangechanged())*