# isHandlingWriting

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the user is actively writing in a text view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var isHandlingWriting: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/Swift/true) in between calls to [`scribbleInteractionWillBeginWriting(_:)`](uiscribbleinteractiondelegate/scribbleinteractionwillbeginwriting(_:).md) and [`scribbleInteractionDidFinishWriting(_:)`](uiscribbleinteractiondelegate/scribbleinteractiondidfinishwriting(_:).md) when the user is writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteraction/ishandlingwriting)*