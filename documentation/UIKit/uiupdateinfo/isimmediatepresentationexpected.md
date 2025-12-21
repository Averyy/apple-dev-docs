# isImmediatePresentationExpected

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system presents UI updates immediately upon completion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var isImmediatePresentationExpected: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the system presents UI updates immediately upon completion. Use this information to determine whether to minimize the complexity of the code you run during the UI update. Defer any processing that isn’t critical for the current UI update until after the UI update finishes.

This value can change during the UI update.

## See Also

- [var isLowLatencyEventDispatchConfirmed: Bool](uiupdateinfo/islowlatencyeventdispatchconfirmed.md)
  A Boolean value that indicates whether the system runs low-latency phases for the UI update.
- [var isPerformingLowLatencyPhases: Bool](uiupdateinfo/isperforminglowlatencyphases.md)
  A Boolean value that indicates whether the UI update is in the low-latency phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/isimmediatepresentationexpected)*