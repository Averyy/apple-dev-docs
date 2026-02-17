# setAttributedTitle(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the switch title to the specified attributed string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAttributedTitle(_ attributedTitle: NSAttributedString?)
```

#### Discussion

This method sets the content of the switch to the specified text, replacing the previous text. The text is drawn using the style information in `attributedTitle`.

If you use styled text in your switches, you must provide localized versions of the text yourself. Attributed strings may not contain any [`NSTextAttachment`](https://developer.apple.com/documentation/UIKit/NSTextAttachment) objects as part of their content.

## Parameters

- `attributedTitle`: The formatted text string to be displayed in the switch. Specifying   clears the current text from the switch.

## See Also

- [func setTitle(String?)](wkinterfaceswitch/settitle(_:).md)
  Sets the switch title to the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setattributedtitle(_:))*