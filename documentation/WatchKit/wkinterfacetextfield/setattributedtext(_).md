# setAttributedText(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the styled text displayed by the text field.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setAttributedText(_ attributedText: NSAttributedString?)
```

```objc
- (void) setAttributedText:(NSAttributedString *) attributedText;
```

## Parameters

- `attributedText`: The styled text displayed in the text field. Specifying `nil` clears the current text.

## See Also

### Setting the Text
- [func setText(String?)](./settext%28_%29.md)
  Sets the text displayed by the text field.
- [func setTextColor(UIColor?)](./settextcolor%28_%29.md)
  Sets the text’s color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setattributedtext(_:))*