# remove(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Stops an observer object from receiving notifications for changes in the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
func remove(_ observer: any FCPXTimelineObserver)
```

```objc
- (void) removeTimelineObserver:(NSObject<FCPXTimelineObserver> *) observer;
```

#### Discussion

Once this method is invoked, the observer no longer gets notified of further Final Cut Pro timeline changes.

You must use this method to cancel an observer added using the [`add(_:)`](./add%28_%29.md) method.

**Swift**:

```swift
host.timeline?.remove(self)
```

**Objective-C**:

```objc
[host.timeline removeTimelineObserver(id<FCPXTimelineObserver>)self];

```

## Parameters

- `observer`: The object to remove as an observer.

## See Also

### Observing the Final Cut Pro Timeline
- [func add(any FCPXTimelineObserver)](./add%28_%29.md)
  Registers a workflow extension object as an observer for Final Cut Pro timeline changes.
- [func movePlayhead(to: CMTime) -> CMTime](./moveplayhead%28to%29.md)
  Sets the Final Cut Pro timeline playhead to a specified time.
- [func playheadTime() -> CMTime](./playheadtime%28%29.md)
  Returns the current playhead position in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline/remove(_:))*