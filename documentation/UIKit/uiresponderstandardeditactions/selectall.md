# selectAll(_:)

**Framework**: UIKit  
**Kind**: method

Selects all of the content in the current responder.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func selectAll(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Select All command from an editing menu. The command selects all content in the responder. For example, a text view selects all of its text and displays an appropriate selection interface.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func select(Any?)](uiresponderstandardeditactions/select(_:).md)
  Selects the content in your responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/selectall(_:))*