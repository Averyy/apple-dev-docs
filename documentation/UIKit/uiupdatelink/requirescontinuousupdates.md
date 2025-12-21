# requiresContinuousUpdates

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the UI update link needs continuous UI updates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var requiresContinuousUpdates: Bool { get set }
```

#### Discussion

By default, the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which means the UI update link acts as a passive observer of UI updates. The system only calls its actions while producing a UI update in response to some kind of event, such as a gesture or layer change.

Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to request that the system produces UI updates continuously. You might opt in to this behavior if you want your actions to run at consistent intervals regardless of other input to the system.

## See Also

- [var wantsLowLatencyEventDispatch: Bool](uiupdatelink/wantslowlatencyeventdispatch.md)
  A Boolean value that determines whether the UI update link requests dispatch of low-latency eligible events.
- [var wantsImmediatePresentation: Bool](uiupdatelink/wantsimmediatepresentation.md)
  A Boolean value that determines whether the UI update link requests immediate frame presentation.
- [var preferredFrameRateRange: CAFrameRateRange](uiupdatelink/preferredframeraterange.md)
  The range of frame rates the UI update link prefers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/requirescontinuousupdates)*