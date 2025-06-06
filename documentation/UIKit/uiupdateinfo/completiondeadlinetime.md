# completionDeadlineTime

**Framework**: UIKit  
**Kind**: property

The time interval that represents the time by which an app needs to finish submitting changes to the render server.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var completionDeadlineTime: TimeInterval { get }
```

#### Discussion

Missing this completion deadline results in a presentation delay.

## See Also

- [var modelTime: TimeInterval](uiupdateinfo/modeltime.md)
  The time interval that represents a reference point for the current time of the UI update.
- [var estimatedPresentationTime: TimeInterval](uiupdateinfo/estimatedpresentationtime.md)
  The time interval that represents an estimate for when current UI update changes become visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/completiondeadlinetime)*