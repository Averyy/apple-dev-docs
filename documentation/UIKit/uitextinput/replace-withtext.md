# replace(_:withText:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Replaces the text in a document that is in the specified range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func replace(_ range: UITextRange, withText text: String)
```

## Parameters

- `range`: A range of text in a document.
- `text`: A string to replace the text in  .

## See Also

- [func text(in: UITextRange) -> String?](uitextinput/text(in:).md)
  Returns the text in the specified range.
- [func shouldChangeText(in: UITextRange, replacementText: String) -> Bool](uitextinput/shouldchangetext(in:replacementtext:).md)
  Asks whether to replace the text in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/replace(_:withtext:))*