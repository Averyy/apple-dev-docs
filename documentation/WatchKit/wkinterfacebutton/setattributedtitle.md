# setAttributedTitle(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the button title to the specified attributed string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAttributedTitle(_ attributedTitle: NSAttributedString?)
```

#### Discussion

This method sets the content of the button to the specified text, replacing the previous text. The text is drawn using the style information in `attributedTitle`. If the button has a background image, the text is drawn on top of that image.

If you use styled text in your buttons, you must provide localized versions of the text yourself. Attributed strings may not contain any NSTextAttachment objects as part of their content.

## Parameters

- `attributedTitle`: The formatted text string to be displayed in the button. Specifying   clears the current text from the button.

## See Also

- [func setTitle(String?)](wkinterfacebutton/settitle(_:).md)
  Sets the button title to the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setattributedtitle(_:))*