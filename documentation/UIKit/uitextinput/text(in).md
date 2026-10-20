# text(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the text in the specified range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func text(in range: UITextRange) -> String?
```

```objc
- (NSString *) textInRange:(UITextRange *) range;
```

#### Return Value

A substring of a document that falls within the specified range.

## Parameters

- `range`: A range of text in a document.

## See Also

### Replacing and returning text
- [func replace(UITextRange, withText: String)](./replace%28_,withtext%29.md)
  Replaces the text in a document that is in the specified range.
- [func shouldChangeText(in: UITextRange, replacementText: String) -> Bool](./shouldchangetext%28in,replacementtext%29.md)
  Asks whether to replace the text in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/text(in:))*