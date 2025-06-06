# textDidChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the input delegate when text has changed in the document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func textDidChange(_ textInput: (any UITextInput)?)
```

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

- [func selectionDidChange((any UITextInput)?)](uitextinputdelegate/selectiondidchange(_:).md)
  Tells the input delegate when the selection has changed in the document.
- [func textWillChange((any UITextInput)?)](uitextinputdelegate/textwillchange(_:).md)
  Tells the input delegate when text is about to change in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/textdidchange(_:))*