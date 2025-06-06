# textWillChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the input delegate when text is about to change in the document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func textWillChange(_ textInput: (any UITextInput)?)
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

- [func selectionWillChange((any UITextInput)?)](uitextinputdelegate/selectionwillchange(_:).md)
  Tells the input delegate when the selection is about to change in the document.
- [func textDidChange((any UITextInput)?)](uitextinputdelegate/textdidchange(_:).md)
  Tells the input delegate when text has changed in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/textwillchange(_:))*