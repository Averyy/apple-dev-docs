# setTextColor(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the text’s color.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setTextColor(_ color: UIColor?)
```

## Overview

This method defines the default color of the entire string. The text field uses this color unless you explicitly override it in an attributed string using the [`NSForegroundColorAttributeName`](https://developer.apple.com/documentation/UIKit/NSForegroundColorAttributeName) attribute.

## Parameters

- `color`: The color to be applied to the text field’s text. Specifying   removes the color and returns the text to the color specified in the storyboard file. The default color is white.

## See Also

- [func setText(String?)](settext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settext(_:)))
- [func setAttributedText(NSAttributedString?)](setattributedtext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setattributedtext(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settextcolor(_:))*