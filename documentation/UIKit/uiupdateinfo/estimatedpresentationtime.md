# estimatedPresentationTime

**Framework**: UIKit  
**Kind**: property

The time interval that represents an estimate for when current UI update changes become visible onscreen.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var estimatedPresentationTime: TimeInterval { get }
```

#### Discussion

This time is an estimate, so the actual time when changes become visible might differ.

## See Also

- [var modelTime: TimeInterval](uiupdateinfo/modeltime.md)
  The time interval that represents a reference point for the current time of the UI update.
- [var completionDeadlineTime: TimeInterval](uiupdateinfo/completiondeadlinetime.md)
  The time interval that represents the time by which an app needs to finish submitting changes to the render server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/estimatedpresentationtime)*