# afterLowLatencyCATransactionCommit

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A phase that runs after a Core Animation transaction commit for a low-latency event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class var afterLowLatencyCATransactionCommit: UIUpdateActionPhase { get }
```

```objc
@property (class, nonatomic, readonly) UIUpdateActionPhase * afterLowLatencyCATransactionCommit;
```

## Discussion

This phase runs after [`flush()`](../../QuartzCore/catransaction/flush%28%29.md) for a low-latency event. Any changes you make to the Core Animation layer tree during this phase or later appear onscreen with the next UI update instead of the current one.

This phase is off by default. You can request it to run by setting [`wantsLowLatencyEventDispatch`](../uiupdatelink/wantslowlatencyeventdispatch.md) to `true`.

## See Also

### Phases
- [class var afterUpdateScheduled: UIUpdateActionPhase](./afterupdatescheduled.md)
  A phase that runs after the scheduling of a UI update.
- [class var beforeEventDispatch: UIUpdateActionPhase](./beforeeventdispatch.md)
  A phase that runs before standard event handlers.
- [class var afterEventDispatch: UIUpdateActionPhase](./aftereventdispatch.md)
  A phase that runs after standard event handlers.
- [class var beforeCADisplayLinkDispatch: UIUpdateActionPhase](./beforecadisplaylinkdispatch.md)
  A phase that runs before Core Animation display link callbacks.
- [class var afterCADisplayLinkDispatch: UIUpdateActionPhase](./aftercadisplaylinkdispatch.md)
  A phase that runs after Core Animation display link callbacks.
- [class var beforeCATransactionCommit: UIUpdateActionPhase](./beforecatransactioncommit.md)
  A phase that runs before a Core Animation transaction commit.
- [class var afterCATransactionCommit: UIUpdateActionPhase](./aftercatransactioncommit.md)
  A phase that runs after a Core Animation transaction commit.
- [class var beforeLowLatencyEventDispatch: UIUpdateActionPhase](./beforelowlatencyeventdispatch.md)
  A phase that runs before low-latency event handlers.
- [class var afterLowLatencyEventDispatch: UIUpdateActionPhase](./afterlowlatencyeventdispatch.md)
  A phase that runs after low-latency event handlers.
- [class var beforeLowLatencyCATransactionCommit: UIUpdateActionPhase](./beforelowlatencycatransactioncommit.md)
  A phase that runs before a Core Animation transaction commit for a low-latency event.
- [class var afterUpdateComplete: UIUpdateActionPhase](./afterupdatecomplete.md)
  A phase that runs at the end of a UI update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateactionphase/afterlowlatencycatransactioncommit)*