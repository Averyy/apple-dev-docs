# wantsLowLatencyEventDispatch

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var wantsLowLatencyEventDispatch: Bool { get set }
```

```objc
@property (nonatomic) BOOL wantsLowLatencyEventDispatch;
```

#### Discussion

By default, the value of this property is [`false`](../../Swift/false.md), which means dispatch for events that are eligible for low-latency is off.

Set the value to [`true`](../../Swift/true.md) to request dispatch of low-latency eligible events. Only pencil events are low-latency eligible, so this behavior is primarily useful for pencil-drawing or writing apps.

Low-latency eligible events dispatch in the middle of a UI update. This timing gives an app half the amount of time to handle them as standard events. Check the value of [`completionDeadlineTime`](../uiupdateinfo/completiondeadlinetime.md) for the precise completion deadline time.

> ❗ **Important**:  If you opt in to this behavior, keep the complexity of the code you use to handle these events to a minimum. When an app requests low-latency event dispatch, but doesn’t optimize event-handling code, frames don’t submit for presentation in time. Dropped frames cause hitches and provide a suboptimal user experience. If you request dispatch of low-latency eligible events, make sure to profile your app thoroughly. For more information, read [Understanding user interface responsiveness](../../Xcode/understanding-user-interface-responsiveness.md).

## See Also

### Configuring preferences
- [var requiresContinuousUpdates: Bool](./requirescontinuousupdates.md)
  A Boolean value that determines whether the UI update link needs continuous UI updates.
- [var wantsImmediatePresentation: Bool](./wantsimmediatepresentation.md)
  A Boolean value that determines whether the UI update link requests immediate frame presentation.
- [var preferredFrameRateRange: CAFrameRateRange](./preferredframeraterange.md)
  The range of frame rates the UI update link prefers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/wantslowlatencyeventdispatch)*