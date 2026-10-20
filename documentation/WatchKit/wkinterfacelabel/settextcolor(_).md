# setTextColor(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the color to apply to plain text strings.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

```objc
- (void) setTextColor:(UIColor *) color;
```

## Mentions

- [Connecting Your User Interface to Your Code](../connecting-your-user-interface-to-your-code.md)

#### Discussion

The value set by this method represents the default color applied to text. This color is used unless you explicitly override it in an attributed string using the [`NSForegroundColorAttributeName`](../../UIKit/nsforegroundcolorattributename.md) attribute.

## Parameters

- `color`: The custom color to be applied to the label’s text. Specifying `nil` removes the custom color and returns the text to the color specified in the storyboard file. The default label color is white.

## See Also

### Setting the Label Text
- [func setText(String?)](./settext%28_%29.md)
  Sets the label text to the specified string.
- [func setAttributedText(NSAttributedString?)](./setattributedtext%28_%29.md)
  Sets the label text to the specified attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:))*