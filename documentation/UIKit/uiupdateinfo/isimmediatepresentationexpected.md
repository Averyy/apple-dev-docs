# isImmediatePresentationExpected

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system presents UI updates immediately upon completion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var isImmediatePresentationExpected: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isImmediatePresentationExpected) BOOL immediatePresentationExpected;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the system presents UI updates immediately upon completion. Use this information to determine whether to minimize the complexity of the code you run during the UI update. Defer any processing that isn’t critical for the current UI update until after the UI update finishes.

This value can change during the UI update.

## See Also

### Working with low-latency updates
- [var isLowLatencyEventDispatchConfirmed: Bool](./islowlatencyeventdispatchconfirmed.md)
  A Boolean value that indicates whether the system runs low-latency phases for the UI update.
- [var isPerformingLowLatencyPhases: Bool](./isperforminglowlatencyphases.md)
  A Boolean value that indicates whether the UI update is in the low-latency phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/isimmediatepresentationexpected)*