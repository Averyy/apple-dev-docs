# isPencilInputExpected

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates the user is likely to use Apple Pencil and handwriting instead of the keyboard to enter text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class var isPencilInputExpected: Bool { get }
```

#### Discussion

If set to [`true`](https://developer.apple.com/documentation/swift/true), adjust the layout of UI elements that aren’t optimal for direct handwriting input. This allows more room for interaction with Apple Pencil. For example, small or resizable text fields can temporarily change their height to receive input from Apple Pencil, while preserving padding along the bottom of the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscribbleinteraction/ispencilinputexpected)*