# UITextDocumentProxy

**Framework**: UIKit  
**Kind**: protocol

An object that provides textual context to a custom keyboard.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextDocumentProxy : UIKeyInput
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Overview

Through conformance to the [`UIKeyInput`](uikeyinput.md) protocol, a text document proxy enables a custom keyboard (which is based on the [`UIInputViewController`](uiinputviewcontroller.md) class) to insert and delete text, to adjust the position of the insertion point, and to determine whether a text input object is empty. The text document proxy uses the keyboard’s [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) property to do this.

For more about using a text document proxy, see [`UIInputViewController`](uiinputviewcontroller.md) and [`Creating a custom keyboard`](creating-a-custom-keyboard.md).

## Topics

### Getting the text-input mode
- [var documentInputMode: UITextInputMode?](uitextdocumentproxy/documentinputmode.md)
  The text-input mode for the keyboard.
### Obtaining textual context around the insertion point
- [var documentContextAfterInput: String?](uitextdocumentproxy/documentcontextafterinput.md)
  Textual context after the insertion point in the current text input object.
- [var documentContextBeforeInput: String?](uitextdocumentproxy/documentcontextbeforeinput.md)
  Textual context before the insertion point in the current text input object.
### Adjusting the insertion point position
- [func adjustTextPosition(byCharacterOffset: Int)](uitextdocumentproxy/adjusttextposition(bycharacteroffset:).md)
  Moves the insertion point forward or backward in the current text input object.
### Getting the selected text
- [var selectedText: String?](uitextdocumentproxy/selectedtext.md)
  The currently selected text in the document.
### Managing marked text
- [func setMarkedText(String, selectedRange: NSRange)](uitextdocumentproxy/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it’s part of an active input session.
- [func unmarkText()](uitextdocumentproxy/unmarktext.md)
  Unmarks the currently marked text.
### Distinguishing changes in the document
- [var documentIdentifier: UUID](uitextdocumentproxy/documentidentifier.md)
  The unique identifier for the document.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIKeyInput](uikeyinput.md)
- [UITextInputTraits](uitextinputtraits.md)

## See Also

- [protocol UIInputViewAudioFeedback](uiinputviewaudiofeedback.md)
  A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdocumentproxy)*