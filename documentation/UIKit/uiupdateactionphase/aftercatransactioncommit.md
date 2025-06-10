# afterCATransactionCommit

**Framework**: UIKit  
**Kind**: property

A phase that runs after a Core Animation transaction commit.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class var afterCATransactionCommit: UIUpdateActionPhase { get }
```

#### Discussion

This phase runs after [`flush()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/flush()). By default, any changes you make to the Core Animation layer tree during this phase or later appear onscreen with the next UI update instead of the current one. However, if you opt in to low-latency event dispatch with [`wantsLowLatencyEventDispatch`](uiupdatelink/wantslowlatencyeventdispatch.md), any changes you make to the Core Animation layer tree before or during the [`beforeLowLatencyCATransactionCommit`](uiupdateactionphase/beforelowlatencycatransactioncommit.md) phase appear onscreen with the current UI update.

> ❗ **Important**:  Although you can send the latest Core Animation layer changes to the render server right away by calling [`commit()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/commit()) or [`flush()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/flush()) manually, doing so isn’t recommended. Calling these methods manually might send unrelated changes to the render server prematurely.

## See Also

- [class var afterUpdateScheduled: UIUpdateActionPhase](uiupdateactionphase/afterupdatescheduled.md)
  A phase that runs after the scheduling of a UI update.
- [class var beforeEventDispatch: UIUpdateActionPhase](uiupdateactionphase/beforeeventdispatch.md)
  A phase that runs before standard event handlers.
- [class var afterEventDispatch: UIUpdateActionPhase](uiupdateactionphase/aftereventdispatch.md)
  A phase that runs after standard event handlers.
- [class var beforeCADisplayLinkDispatch: UIUpdateActionPhase](uiupdateactionphase/beforecadisplaylinkdispatch.md)
  A phase that runs before Core Animation display link callbacks.
- [class var afterCADisplayLinkDispatch: UIUpdateActionPhase](uiupdateactionphase/aftercadisplaylinkdispatch.md)
  A phase that runs after Core Animation display link callbacks.
- [class var beforeCATransactionCommit: UIUpdateActionPhase](uiupdateactionphase/beforecatransactioncommit.md)
  A phase that runs before a Core Animation transaction commit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateactionphase/aftercatransactioncommit)*