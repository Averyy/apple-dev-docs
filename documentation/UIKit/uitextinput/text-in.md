# text(in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the text in the specified range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func text(in range: UITextRange) -> String?
```

#### Return Value

A substring of a document that falls within the specified range.

## Parameters

- `range`: A range of text in a document.

## See Also

- [func replace(UITextRange, withText: String)](uitextinput/replace(_:withtext:).md)
  Replaces the text in a document that is in the specified range.
- [func shouldChangeText(in: UITextRange, replacementText: String) -> Bool](uitextinput/shouldchangetext(in:replacementtext:).md)
  Asks whether to replace the text in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/text(in:))*