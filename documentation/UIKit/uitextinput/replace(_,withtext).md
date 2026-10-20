# replace(_:withText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Replaces the text in a document that is in the specified range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func replace(_ range: UITextRange, withText text: String)
```

```objc
- (void) replaceRange:(UITextRange *) range withText:(NSString *) text;
```

## Parameters

- `range`: A range of text in a document.
- `text`: A string to replace the text in `range`.

## See Also

### Replacing and returning text
- [func text(in: UITextRange) -> String?](./text%28in%29.md)
  Returns the text in the specified range.
- [func shouldChangeText(in: UITextRange, replacementText: String) -> Bool](./shouldchangetext%28in,replacementtext%29.md)
  Asks whether to replace the text in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/replace(_:withtext:))*