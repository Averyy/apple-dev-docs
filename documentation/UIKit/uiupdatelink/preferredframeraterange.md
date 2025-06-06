# preferredFrameRateRange

**Framework**: UIKit  
**Kind**: property

The range of frame rates the UI update link prefers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var preferredFrameRateRange: CAFrameRateRange { get set }
```

#### Discussion

By default, the value of this property is [`default`](https://developer.apple.com/documentation/QuartzCore/CAFrameRateRange/default), which doesn’t request any specific frame rate range.

## See Also

- [var requiresContinuousUpdates: Bool](uiupdatelink/requirescontinuousupdates.md)
  A Boolean value that determines whether the UI update link needs continuous UI updates.
- [var wantsLowLatencyEventDispatch: Bool](uiupdatelink/wantslowlatencyeventdispatch.md)
  A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [var wantsImmediatePresentation: Bool](uiupdatelink/wantsimmediatepresentation.md)
  A Boolean value that determines whether the UI update link requests immediate frame presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/preferredframeraterange)*