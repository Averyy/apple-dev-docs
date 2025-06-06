# modelTime

**Framework**: UIKit  
**Kind**: property

The time interval that represents a reference point for the current time of the UI update.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var modelTime: TimeInterval { get }
```

#### Discussion

This time provides a reference point for driving time-based model changes, like animations or physics. This property attempts to maintain constant latency between model changes and their onscreen presentation. It uses the same units as [`CACurrentMediaTime()`](https://developer.apple.com/documentation/QuartzCore/CACurrentMediaTime()). Numerically, this time is close to the start of the UI update, but its precise relation to the UI update start time might change, depending on frame rate and other UI update parameters.

## See Also

- [var completionDeadlineTime: TimeInterval](uiupdateinfo/completiondeadlinetime.md)
  The time interval that represents the time by which an app needs to finish submitting changes to the render server.
- [var estimatedPresentationTime: TimeInterval](uiupdateinfo/estimatedpresentationtime.md)
  The time interval that represents an estimate for when current UI update changes become visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/modeltime)*