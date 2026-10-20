# setAttributedTitle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the switch title to the specified attributed string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAttributedTitle(_ attributedTitle: NSAttributedString?)
```

```objc
- (void) setAttributedTitle:(NSAttributedString *) attributedTitle;
```

#### Discussion

This method sets the content of the switch to the specified text, replacing the previous text. The text is drawn using the style information in `attributedTitle`.

If you use styled text in your switches, you must provide localized versions of the text yourself. Attributed strings may not contain any [`NSTextAttachment`](../../UIKit/nstextattachment.md) objects as part of their content.

## Parameters

- `attributedTitle`: The formatted text string to be displayed in the switch. Specifying `nil` clears the current text from the switch.

## See Also

### Setting the Switch’s Title
- [func setTitle(String?)](./settitle%28_%29.md)
  Sets the switch title to the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setattributedtitle(_:))*