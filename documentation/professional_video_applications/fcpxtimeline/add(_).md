# add(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Registers a workflow extension object as an observer for Final Cut Pro timeline changes.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
func add(_ observer: any FCPXTimelineObserver)
```

```objc
- (void) addTimelineObserver:(NSObject<FCPXTimelineObserver> *) observer;
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

## Discussion

You can choose any object in your extension to act as an observer; you typically use the extension view controller. Make sure that the observer object conforms to the [`FCPXTimelineObserver`](../fcpxtimelineobserver.md) protocol.

**Swift**:

```swift
host.timeline?.add(self)
```

**Objective-C**:

```objc
[host.timeline addTimelineObserver(NSObject<FCPXTimelineObserver>*)self];
```

Final Cut Pro notifies a registered observer of a change in the Final Cut Pro timeline through one of the [`FCPXTimelineObserver`](../fcpxtimelineobserver.md) protocol methods the observer implements. For example, to get notifications of changes in the current sequence, implement the [`activeSequenceChanged()`](../fcpxtimelineobserver/activesequencechanged%28%29.md) method. Pair each invocation of the [`add(_:)`](./add%28_%29.md) method with a corresponding call to [`remove(_:)`](./remove%28_%29.md) method.

## Parameters

- `observer`: An object to register as an observer.

## See Also

### Observing the Final Cut Pro Timeline
- [func movePlayhead(to: CMTime) -> CMTime](./moveplayhead%28to%29.md)
  Sets the Final Cut Pro timeline playhead to a specified time.
- [func playheadTime() -> CMTime](./playheadtime%28%29.md)
  Returns the current playhead position in the Final Cut Pro timeline.
- [func remove(any FCPXTimelineObserver)](./remove%28_%29.md)
  Stops an observer object from receiving notifications for changes in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxtimeline/add(_:))*