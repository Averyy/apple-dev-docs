# init(textInput:)

**Framework**: UIKit  
**Kind**: init

Returns an object initialized with the document object that directly communicates with the text input system.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(textInput: any UIResponder & UITextInput)
```

#### Return Value

An instance of a subclass of [`UITextInputStringTokenizer`](uitextinputstringtokenizer.md), or `nil` if the object couldn’t be created.

#### Discussion

The subclass of [`UITextInputStringTokenizer`](uitextinputstringtokenizer.md) shouldn’t retain `textInput`; the tokenizer should always have a lifetime bounded by that of the [`UITextInput`](uitextinput.md)-conforming object and a retaining reference would create a retain cycle.

## Parameters

- `textInput`: The document object in the application that adopts the   protocol for the purposes of communicating with the text input system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer/init(textinput:))*