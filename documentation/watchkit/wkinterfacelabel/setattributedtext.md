# setAttributedText(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the label text to the specified attributed string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAttributedText(_ attributedText: NSAttributedString?)
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md)

#### Discussion

This method changes the label text to the new value, replacing the old text if any. Any font and style attributes applied to the string take precedence over default values. If you do not explicitly specify font or styling information, the default values are used instead. For example, if you do not specify a text color explicitly, the default text color is used.

Attributed strings may not contain any [`NSTextAttachment`](https://developer.apple.com/documentation/UIKit/NSTextAttachment) objects as part of their content.

## Parameters

- `attributedText`: The formatted text string to be displayed in the label. Specifying   clears the current text from the label.

## See Also

- [func setText(String?)](wkinterfacelabel/settext(_:).md)
  Sets the label text to the specified string.
- [func setTextColor(UIColor?)](wkinterfacelabel/settextcolor(_:).md)
  Sets the color to apply to plain text strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:))*