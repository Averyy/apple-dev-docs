# setTextColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the text’s color.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

```objc
- (void) setTextColor:(UIColor *) color;
```

## Discussion

This method defines the default color of the entire string. The text field uses this color unless you explicitly override it in an attributed string using the [`NSForegroundColorAttributeName`](../../UIKit/nsforegroundcolorattributename.md) attribute.

## Parameters

- `color`: The color to be applied to the text field’s text. Specifying `nil` removes the color and returns the text to the color specified in the storyboard file. The default color is white.

## See Also

### Setting the Text
- [func setText(String?)](./settext%28_%29.md)
  Sets the text displayed by the text field.
- [func setAttributedText(NSAttributedString?)](./setattributedtext%28_%29.md)
  Sets the styled text displayed by the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settextcolor(_:))*