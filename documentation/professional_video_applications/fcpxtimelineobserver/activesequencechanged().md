# activeSequenceChanged()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

A callback method that gets invoked when there is a change in the current timeline sequence.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
optional func activeSequenceChanged()
```

```objc
- (void) activeSequenceChanged;
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

#### Discussion

Implement this method in your workflow extension observer object to receive notifications when an active sequence changes in the Final Cut Pro timeline. Inside the implementation, use the [`activeSequence`](../fcpxtimeline/activesequence.md) property to obtain details of the new sequence. Access the container object of the new sequence using the [`container`](../fcpxobject/container.md) property.

**Swift**:

```swift
let container = sequence.container
```

**Objective-C**:

```objc
FCPXObject* container = [sequence container];
```

## See Also

### Handling Final Cut Pro Timeline Changes
- [func playheadTimeChanged()](./playheadtimechanged%28%29.md)
  A callback method that gets invoked when the playhead position changes in the Final Cut Pro timeline.
- [func sequenceTimeRangeChanged()](./sequencetimerangechanged%28%29.md)
  A callback method that gets invoked when the time range of an active sequence changes in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimelineobserver/activesequencechanged())*