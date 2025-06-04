# setTextColor(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the color to apply to plain text strings.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))

## Overview

The value set by this method represents the default color applied to text. This color is used unless you explicitly override it in an attributed string using the [`NSForegroundColorAttributeName`](https://developer.apple.com/documentation/UIKit/NSForegroundColorAttributeName) attribute.

## Parameters

- `color`: The custom color to be applied to the label’s text. Specifying   removes the custom color and returns the text to the color specified in the storyboard file. The default label color is white.

## See Also

- [func setText(String?)](settext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settext(_:)))
- [func setAttributedText(NSAttributedString?)](setattributedtext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:))*