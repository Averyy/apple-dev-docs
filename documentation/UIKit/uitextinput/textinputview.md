# textInputView

**Framework**: UIKit  
**Kind**: property

An affiliated view that provides a coordinate system for all geometric values in the protocol.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var textInputView: UIView { get }
```

#### Discussion

The view that both draws the text and provides a coordinate system for all geometric values in this protocol. (This is typically an instance of the [`UITextInput`](uitextinput.md)-adopting class.) If this property is unimplemented, the first view in the responder chain is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/textinputview)*