# textStyling(at:in:)

**Framework**: UIKit  
**Kind**: method

Returns a dictionary with properties that specify how to style the text at a certain location in a document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textStyling(at position: UITextPosition, in direction: UITextStorageDirection) -> [NSAttributedString.Key : Any]?
```

#### Return Value

A dictionary whose elements are one or more of the key-value pairs defining text color, font, and background color. See [`Style dictionary keys`](style-dictionary-keys.md) for descriptions of these key-value pairs.

#### Discussion

Text styling information can affect, for example, the appearance of a correction rectangle.

## Parameters

- `position`: An object that indicates a location in the text of a document.
- `direction`: The direction of the styling attributes in text storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/textstyling(at:in:))*