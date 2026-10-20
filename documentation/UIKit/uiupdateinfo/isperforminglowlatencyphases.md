# isPerformingLowLatencyPhases

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the UI update is in the low-latency phases.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var isPerformingLowLatencyPhases: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPerformingLowLatencyPhases) BOOL performingLowLatencyPhases;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) between the [`beforeLowLatencyEventDispatch`](../uiupdateactionphase/beforelowlatencyeventdispatch.md) and [`afterLowLatencyCATransactionCommit`](../uiupdateactionphase/afterlowlatencycatransactioncommit.md) UI update phases. Keep any code you run in this part of the UI update as minimal as possible, especially when [`isImmediatePresentationExpected`](./isimmediatepresentationexpected.md) is `true`. Defer any processing that isn’t critical for the current UI update until [`afterLowLatencyCATransactionCommit`](../uiupdateactionphase/afterlowlatencycatransactioncommit.md).

## See Also

### Working with low-latency updates
- [var isImmediatePresentationExpected: Bool](./isimmediatepresentationexpected.md)
  A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [var isLowLatencyEventDispatchConfirmed: Bool](./islowlatencyeventdispatchconfirmed.md)
  A Boolean value that indicates whether the system runs low-latency phases for the UI update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/isperforminglowlatencyphases)*