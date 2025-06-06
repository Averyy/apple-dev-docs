# delegate

**Framework**: UIKit  
**Kind**: property

The custom object you use to provide PDF data for a screenshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIScreenshotServiceDelegate)? { get set }
```

#### Discussion

Assign an object to this property early in the life cycle of your window scene. The object must conform to the [`UIScreenshotServiceDelegate`](uiscreenshotservicedelegate.md) protocol.

## See Also

- [protocol UIScreenshotServiceDelegate](uiscreenshotservicedelegate.md)
  Methods you use to generate PDF data that accompanies a user-requested screenshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreenshotservice/delegate)*