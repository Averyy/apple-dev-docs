# isEditable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the text view contains editable text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional var isEditable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isEditable) BOOL editable;
```

#### Discussion

Text views are normally editable, and the default value of this property is [`true`](../../Swift/true.md) if you don’t provide an implementation. When implementing a custom text view, you might implement this property and return [`false`](../../Swift/false.md) to prevent outside agents from modifying the content of your view. For example, you might disable editing to prevent the system’s writing tools panel from pasting content into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/iseditable)*