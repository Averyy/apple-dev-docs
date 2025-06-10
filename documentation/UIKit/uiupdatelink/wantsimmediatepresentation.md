# wantsImmediatePresentation

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the UI update link requests immediate frame presentation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var wantsImmediatePresentation: Bool { get set }
```

#### Discussion

By default, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system requests immediate rendering of the display frame after the last [`CATransaction`](https://developer.apple.com/documentation/QuartzCore/CATransaction) commit for the current UI update. Opting in to this behavior can help reduce latency between input and display because the rendered display frame presents one frame duration sooner. This behavior is primarily useful for pencil-drawing apps where low input-to-display latency is critical for an optimal user experience.

> ❗ **Important**:  If you opt in to this behavior, keep the complexity of the code you submit to the render server to a minimum. When an app requests immediate frame presentation, but doesn’t keep rendering complexity minimal, frames don’t submit for presentation in time. Dropped frames cause hitches and provide a suboptimal user experience. If you request immediate presentation, make sure to profile your app thoroughly. For more information, read [`Understanding user interface responsiveness`](https://developer.apple.com/documentation/Xcode/understanding-user-interface-responsiveness).

## See Also

- [var requiresContinuousUpdates: Bool](uiupdatelink/requirescontinuousupdates.md)
  A Boolean value that determines whether the UI update link needs continuous UI updates.
- [var wantsLowLatencyEventDispatch: Bool](uiupdatelink/wantslowlatencyeventdispatch.md)
  A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [var preferredFrameRateRange: CAFrameRateRange](uiupdatelink/preferredframeraterange.md)
  The range of frame rates the UI update link prefers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/wantsimmediatepresentation)*