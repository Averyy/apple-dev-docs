# setText(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the label text to the specified string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setText(_ text: String?)
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))

#### Discussion

This method changes the string displayed by the label to the new value. When using this method to set the text, the default font and styling information for the text is derived from the storyboard file. You can change the default text color using the [`setTextColor(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:)) method.

Changing the text of the label causes the label to resize itself to accommodate the new string. If the string is too large to fit the available space, WatchKit truncates the text.

## Parameters

- `text`: The text to be displayed in the label. Specifying   clears the current text from the label.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setTextColor(UIColor?)](settextcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:)))
  Sets the color to apply to plain text strings.
- [func setAttributedText(NSAttributedString?)](setattributedtext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)))
  Sets the label text to the specified attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settext(_:))*