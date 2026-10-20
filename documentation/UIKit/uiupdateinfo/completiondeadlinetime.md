# completionDeadlineTime

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The time interval that represents the time by which an app needs to finish submitting changes to the render server.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var completionDeadlineTime: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval completionDeadlineTime;
```

#### Discussion

Missing this completion deadline results in a presentation delay.

## See Also

### Getting information about timing
- [var modelTime: TimeInterval](./modeltime.md)
  The time interval that represents a reference point for the current time of the UI update.
- [var estimatedPresentationTime: TimeInterval](./estimatedpresentationtime.md)
  The time interval that represents an estimate for when current UI update changes become visible onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdateinfo/completiondeadlinetime)*