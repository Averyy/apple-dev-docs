# selectionWillChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the input delegate when the selection is about to change in the document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func selectionWillChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

- [func textWillChange((any UITextInput)?)](uitextinputdelegate/textwillchange(_:).md)
  Tells the input delegate when text is about to change in the document.
- [func selectionDidChange((any UITextInput)?)](uitextinputdelegate/selectiondidchange(_:).md)
  Tells the input delegate when the selection has changed in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectionwillchange(_:))*