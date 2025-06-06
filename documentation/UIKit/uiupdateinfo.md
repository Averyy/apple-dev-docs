# UIUpdateInfo

**Framework**: UIKit  
**Kind**: class

An object that contains detailed information about the current UI update state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UIUpdateInfo
```

#### Overview

During a UI update, this object provides details about the state of the update. When using a [`UIUpdateLink`](uiupdatelink.md), you can query this UI update information object to learn about the current UI update.

A UI update can service views on different displays simultaneously, which means these views can have a different [`UIUpdateInfo`](uiupdateinfo.md). Get the UI update information for a specific view using [`current(for:)`](uiupdateinfo/current(for:)-34zby.md) or a specific window using [`current(for:)`](uiupdateinfo/current(for:)-6y1z9.md). The UI update information can also change as the current UI update progresses through its phases.

## Topics

### Getting the current UI update information
- [class func current(for: UIView) -> Self?](uiupdateinfo/current(for:)-34zby.md)
  Returns an object that describes the current UI update state for the specified view.
- [class func current(for: UIWindowScene) -> Self?](uiupdateinfo/current(for:)-6y1z9.md)
  Returns an object that describes the current UI update state for the specified window.
### Getting information about timing
- [var modelTime: TimeInterval](uiupdateinfo/modeltime.md)
  The time interval that represents a reference point for the current time of the UI update.
- [var completionDeadlineTime: TimeInterval](uiupdateinfo/completiondeadlinetime.md)
  The time interval that represents the time by which an app needs to finish submitting changes to the render server.
- [var estimatedPresentationTime: TimeInterval](uiupdateinfo/estimatedpresentationtime.md)
  The time interval that represents an estimate for when current UI update changes become visible onscreen.
### Working with low-latency updates
- [var isImmediatePresentationExpected: Bool](uiupdateinfo/isimmediatepresentationexpected.md)
  A Boolean value that indicates whether the system presents UI updates immediately upon completion.
- [var isLowLatencyEventDispatchConfirmed: Bool](uiupdateinfo/islowlatencyeventdispatchconfirmed.md)
  A Boolean value that indicates whether the system runs low-latency phases for the UI update.
- [var isPerformingLowLatencyPhases: Bool](uiupdateinfo/isperforminglowlatencyphases.md)
  A Boolean value that indicates whether the UI update is in the low-latency phases.

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
- [class UIUpdateActionPhase](uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo)*