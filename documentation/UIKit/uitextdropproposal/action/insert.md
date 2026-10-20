# UITextDropProposal.Action.insert

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case insert
```

```c
UITextDropActionInsert
```

#### Discussion

The action ignores any selection present in the target text view.

## See Also

### Text drop actions
- [UITextDropProposal.Action.replaceAll](./replaceall.md)
  A text drop action style specifying that the dropped text replaces all text in the target text view.
- [UITextDropProposal.Action.replaceSelection](./replaceselection.md)
  A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/action/insert)*