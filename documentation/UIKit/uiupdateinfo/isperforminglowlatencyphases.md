# isPerformingLowLatencyPhases

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the UI update is in the low-latency phases.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var isPerformingLowLatencyPhases: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) between the [`beforeLowLatencyEventDispatch`](uiupdateactionphase/beforelowlatencyeventdispatch.md) and [`afterLowLatencyCATransactionCommit`](uiupdateactionphase/afterlowlatencycatransactioncommit.md) UI update phases. Keep any code you run in this part of the UI update as minimal as possible, especially when [`isImmediatePresentationExpected`](uiupdateinfo/isimmediatepresentationexpected.md) is `true`. Defer any processing that isn’t critical for the current UI update until [`afterLowLatencyCATransactionCommit`](uiupdateactionphase/afterlowlatencycatransactioncommit.md).

## See Also

- [var isImmediatePresentationExpected: Bool](uiupdateinfo/isimmediatepresentationexpected.md)
  A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [var isLowLatencyEventDispatchConfirmed: Bool](uiupdateinfo/islowlatencyeventdispatchconfirmed.md)
  A Boolean value that indicates whether the system runs low-latency phases for the UI update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/isperforminglowlatencyphases)*