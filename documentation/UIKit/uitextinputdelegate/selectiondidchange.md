# selectionDidChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the input delegate when the selection has changed in the document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func selectionDidChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

- [func textDidChange((any UITextInput)?)](uitextinputdelegate/textdidchange(_:).md)
  Tells the input delegate when text has changed in the document.
- [func selectionWillChange((any UITextInput)?)](uitextinputdelegate/selectionwillchange(_:).md)
  Tells the input delegate when the selection is about to change in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectiondidchange(_:))*