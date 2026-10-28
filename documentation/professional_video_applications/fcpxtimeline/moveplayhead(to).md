# movePlayhead(to:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Sets the Final Cut Pro timeline playhead to a specified time.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
func movePlayhead(to newTime: CMTime) -> CMTime
```

```objc
- (CMTime) movePlayheadTo:(CMTime) newTime;
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

## Return Value

The new playhead position in the Final Cut Pro timeline.

## Discussion

Workflow extensions can use this method to move the playhead to a new location in the Final Cut Pro timeline. The movement of the playhead is limited to the valid time range of the current timeline sequence. Use the [`sequenceTimeRange`](./sequencetimerange.md) property to find the time range of a sequence in the Final Cut Pro timeline.

## Parameters

- `newTime`: Specifies a new timeline position.

## See Also

### Observing the Final Cut Pro Timeline
- [func add(any FCPXTimelineObserver)](./add%28_%29.md)
  Registers a workflow extension object as an observer for Final Cut Pro timeline changes.
- [func playheadTime() -> CMTime](./playheadtime%28%29.md)
  Returns the current playhead position in the Final Cut Pro timeline.
- [func remove(any FCPXTimelineObserver)](./remove%28_%29.md)
  Stops an observer object from receiving notifications for changes in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline/moveplayhead(to:))*