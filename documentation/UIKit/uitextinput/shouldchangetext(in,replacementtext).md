# shouldChangeText(in:replacementText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks whether to replace the text in the specified range.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func shouldChangeText(in range: UITextRange, replacementText text: String) -> Bool
```

```objc
- (BOOL) shouldChangeTextInRange:(UITextRange *) range replacementText:(NSString *) text;
```

#### Return Value

[`true`](../../Swift/true.md) if the text should be changed or [`false`](../../Swift/false.md) if it should not.

#### Discussion

Prior to replacing text, this method is called to give your delegate a chance to accept or reject the edits. If you do not implement this method, the return value defaults to [`true`](../../Swift/true.md).

## Parameters

- `range`: A range of text in a document.
- `text`: The proposed text to replace the text in `range`.

## See Also

### Replacing and returning text
- [func text(in: UITextRange) -> String?](./text%28in%29.md)
  Returns the text in the specified range.
- [func replace(UITextRange, withText: String)](./replace%28_,withtext%29.md)
  Replaces the text in a document that is in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/shouldchangetext(in:replacementtext:))*