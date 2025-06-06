# afterEventDispatch

**Framework**: UIKit  
**Kind**: property

A phase that runs after standard event handlers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class var afterEventDispatch: UIUpdateActionPhase { get }
```

#### Discussion

This phase runs after [`UIEvent`](uievent.md) and [`UIGestureRecognizer`](uigesturerecognizer.md) handlers run for standard events. After that point, the app doesn’t receive new user input events. However, if you request low-latency event dispatch using [`wantsLowLatencyEventDispatch`](uiupdatelink/wantslowlatencyeventdispatch.md), more events might dispatch in the low-latency event dispatch phase.

Use this phase to perform tasks after processing all user input events for the UI update, like starting a parallel rendering thread.

## See Also

- [class var afterUpdateScheduled: UIUpdateActionPhase](uiupdateactionphase/afterupdatescheduled.md)
  A phase that runs after the scheduling of a UI update.
- [class var beforeEventDispatch: UIUpdateActionPhase](uiupdateactionphase/beforeeventdispatch.md)
  A phase that runs before standard event handlers.
- [class var beforeCADisplayLinkDispatch: UIUpdateActionPhase](uiupdateactionphase/beforecadisplaylinkdispatch.md)
  A phase that runs before Core Animation display link callbacks.
- [class var afterCADisplayLinkDispatch: UIUpdateActionPhase](uiupdateactionphase/aftercadisplaylinkdispatch.md)
  A phase that runs after Core Animation display link callbacks.
- [class var beforeCATransactionCommit: UIUpdateActionPhase](uiupdateactionphase/beforecatransactioncommit.md)
  A phase that runs before a Core Animation transaction commit.
- [class var afterCATransactionCommit: UIUpdateActionPhase](uiupdateactionphase/aftercatransactioncommit.md)
  A phase that runs after a Core Animation transaction commit.
- [class var beforeLowLatencyEventDispatch: UIUpdateActionPhase](uiupdateactionphase/beforelowlatencyeventdispatch.md)
  A phase that runs before low-latency event handlers.
- [class var afterLowLatencyEventDispatch: UIUpdateActionPhase](uiupdateactionphase/afterlowlatencyeventdispatch.md)
  A phase that runs after low-latency event handlers.
- [class var beforeLowLatencyCATransactionCommit: UIUpdateActionPhase](uiupdateactionphase/beforelowlatencycatransactioncommit.md)
  A phase that runs before a Core Animation transaction commit for a low-latency event.
- [class var afterLowLatencyCATransactionCommit: UIUpdateActionPhase](uiupdateactionphase/afterlowlatencycatransactioncommit.md)
  A phase that runs after a Core Animation transaction commit for a low-latency event.
- [class var afterUpdateComplete: UIUpdateActionPhase](uiupdateactionphase/afterupdatecomplete.md)
  A phase that runs at the end of a UI update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateactionphase/aftereventdispatch)*