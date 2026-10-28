# setAttributedText(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the label text to the specified attributed string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAttributedText(_ attributedText: NSAttributedString?)
```

```objc
- (void) setAttributedText:(NSAttributedString *) attributedText;
```

## Mentions

- [Connecting Your User Interface to Your Code](../connecting-your-user-interface-to-your-code.md)

## Discussion

This method changes the label text to the new value, replacing the old text if any. Any font and style attributes applied to the string take precedence over default values. If you do not explicitly specify font or styling information, the default values are used instead. For example, if you do not specify a text color explicitly, the default text color is used.

Attributed strings may not contain any [`NSTextAttachment`](../../UIKit/nstextattachment.md) objects as part of their content.

## Parameters

- `attributedText`: The formatted text string to be displayed in the label. Specifying `nil` clears the current text from the label.

## See Also

### Setting the Label Text
- [func setText(String?)](./settext%28_%29.md)
  Sets the label text to the specified string.
- [func setTextColor(UIColor?)](./settextcolor%28_%29.md)
  Sets the color to apply to plain text strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:))*