# preferredFrameRateRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The range of frame rates the UI update link prefers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var preferredFrameRateRange: CAFrameRateRange { get set }
```

```objc
@property (nonatomic) CAFrameRateRange preferredFrameRateRange;
```

## Discussion

By default, the value of this property is [`default`](../../QuartzCore/caframeraterange/default.md), which doesn’t request any specific frame rate range.

## See Also

### Configuring preferences
- [var requiresContinuousUpdates: Bool](./requirescontinuousupdates.md)
  A Boolean value that determines whether the UI update link needs continuous UI updates.
- [var wantsLowLatencyEventDispatch: Bool](./wantslowlatencyeventdispatch.md)
  A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [var wantsImmediatePresentation: Bool](./wantsimmediatepresentation.md)
  A Boolean value that determines whether the UI update link requests immediate frame presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/preferredframeraterange)*