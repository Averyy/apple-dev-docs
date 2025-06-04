# setTextColor(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the text’s color.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

#### Discussion

This method defines the default color of the entire string. The text field uses this color unless you explicitly override it in an attributed string using the [`NSForegroundColorAttributeName`](https://developer.apple.com/documentation/UIKit/NSForegroundColorAttributeName) attribute.

## Parameters

- `color`: The color to be applied to the text field’s text. Specifying   removes the color and returns the text to the color specified in the storyboard file. The default color is white.

## See Also

- [func setText(String?)](wkinterfacetextfield/settext(_:).md)
  Sets the text displayed by the text field.
- [func setAttributedText(NSAttributedString?)](wkinterfacetextfield/setattributedtext(_:).md)
  Sets the styled text displayed by the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settextcolor(_:))*