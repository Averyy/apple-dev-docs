# UITextDropProposal.Action.replaceSelection

**Framework**: UIKit  
**Kind**: case

A text drop action style specifying that if the target text view contains a selection, dropped text replaces it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case replaceSelection
```

#### Discussion

If the text view does not contain a selection, dropped text is inserted at the provided location, without altering the surrounding text.

## See Also

- [UITextDropProposal.Action.insert](uitextdropproposal/action/insert.md)
  A text drop action style specifying that text is inserted at the provided location, without altering the surrounding text.
- [UITextDropProposal.Action.replaceAll](uitextdropproposal/action/replaceall.md)
  A text drop action style specifying that the dropped text replaces all text in the target text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdropproposal/action/replaceselection)*