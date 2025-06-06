# textInput

**Framework**: UIKit  
**Kind**: property

The text input object that manages the selection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var textInput: (any UITextInput)? { get }
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

Use this property to refer to the text input view that manages the text selection. You specify this view when you create the [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/textinput)*