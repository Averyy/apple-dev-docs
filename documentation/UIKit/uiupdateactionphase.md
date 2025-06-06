# UIUpdateActionPhase

**Framework**: UIKit  
**Kind**: class

An object that defines specific phases of the UI update process.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UIUpdateActionPhase
```

#### Overview

Each UI update consists of several phases that run in a consistent order, and the [`UIUpdateActionPhase`](uiupdateactionphase.md) object defines constants that represent these phases. When using a [`UIUpdateLink`](uiupdatelink.md), you can use these constants to decide which phase of the UI update process you want its actions to run in.

There are two : standard and low-latency. The standard phase group runs for each UI update. This phase group includes these phases, which run in the following order:

1. [`beforeEventDispatch`](uiupdateactionphase/beforeeventdispatch.md)
2. [`afterEventDispatch`](uiupdateactionphase/aftereventdispatch.md)
3. [`beforeCADisplayLinkDispatch`](uiupdateactionphase/beforecadisplaylinkdispatch.md)
4. [`afterCADisplayLinkDispatch`](uiupdateactionphase/aftercadisplaylinkdispatch.md)
5. [`beforeCATransactionCommit`](uiupdateactionphase/beforecatransactioncommit.md)
6. [`afterCATransactionCommit`](uiupdateactionphase/aftercatransactioncommit.md)

The low-latency phase group is optional, and it’s off by default. It runs only if you explicitly request low-latency event dispatch using [`wantsLowLatencyEventDispatch`](uiupdatelink/wantslowlatencyeventdispatch.md). The low-latency phase group includes these phases, which run in the following order (after the standard phases):

1. [`beforeLowLatencyEventDispatch`](uiupdateactionphase/beforelowlatencyeventdispatch.md)
2. [`afterLowLatencyEventDispatch`](uiupdateactionphase/afterlowlatencyeventdispatch.md)
3. [`beforeLowLatencyCATransactionCommit`](uiupdateactionphase/beforelowlatencycatransactioncommit.md)
4. [`afterLowLatencyCATransactionCommit`](uiupdateactionphase/afterlowlatencycatransactioncommit.md)

When a phase group runs, all phases inside the group run. Phases run one after another in the specified order without exiting back into the run loop.

## Topics

### Phases
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIUpdateLink](uiupdatelink.md)
  An object you use to observe, participate in, and affect the UI update process.
- [class UIUpdateInfo](uiupdateinfo.md)
  An object that contains detailed information about the current UI update state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateactionphase)*