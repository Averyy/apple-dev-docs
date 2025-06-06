# init(textInput:delegate:)

**Framework**: UIKit  
**Kind**: init

Creates a new text selection display interaction object for the specified text view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(textInput: any UITextInput, delegate: any UITextSelectionDisplayInteractionDelegate)
```

## Parameters

- `textInput`: The text input view that receives this interaction view.
- `delegate`: An optional delegate object to manage the selection UI views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/init(textinput:delegate:))*