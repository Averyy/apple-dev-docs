# playheadTime()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Returns the current playhead position in the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
func playheadTime() -> CMTime
```

```objc
- (CMTime) playheadTime;
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

#### Discussion

When Final Cut Pro invokes a registered observer to send a notification of a change in the playhead time of an active sequence, use this method to find the new playhead position in the Final Cut Pro timeline. The method returns [`invalid`](../../CoreMedia/cmtime/invalid.md) (Swift) or [`invalid`](../../CoreMedia/cmtime/invalid.md) (Objective-C) if the Final Cut Pro timeline has no valid sequence.

## See Also

### Observing the Final Cut Pro Timeline
- [func add(any FCPXTimelineObserver)](./add%28_%29.md)
  Registers a workflow extension object as an observer for Final Cut Pro timeline changes.
- [func movePlayhead(to: CMTime) -> CMTime](./moveplayhead%28to%29.md)
  Sets the Final Cut Pro timeline playhead to a specified time.
- [func remove(any FCPXTimelineObserver)](./remove%28_%29.md)
  Stops an observer object from receiving notifications for changes in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline/playheadtime())*