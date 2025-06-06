# statusBarFrame

**Framework**: UIKit  
**Kind**: property

The frame rectangle of the status bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var statusBarFrame: CGRect { get }
```

#### Discussion

The frame rectangle is in the coordinate space of the associated [`UIWindowScene`](uiwindowscene.md) object. If the status bar is hidden, the value of this property is [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistatusbarmanager/statusbarframe)*