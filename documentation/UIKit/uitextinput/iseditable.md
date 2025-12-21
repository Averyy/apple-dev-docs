# isEditable

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the text view contains editable text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
optional var isEditable: Bool { get }
```

#### Discussion

Text views are normally editable, and the default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if you don’t provide an implementation. When implementing a custom text view, you might implement this property and return [`false`](https://developer.apple.com/documentation/Swift/false) to prevent outside agents from modifying the content of your view. For example, you might disable editing to prevent the system’s writing tools panel from pasting content into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/iseditable)*