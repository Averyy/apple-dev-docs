# setAlpha(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the opacity of the interface object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setAlpha(_ alpha: CGFloat)
```

## Overview

Use this property to make an object fully or partially transparent. A partially transparent object allows the color or background image associated with the containing group or interface controller show through. A fully transparent object cannot be seen but continues to occupy space in your interface.

Changes to the alpha value of an object are animatable.

## Parameters

- `alpha`: A floating-point number in the range   to  , where   represents totally transparent and   represents totally opaque.

## See Also

- [func setHidden(Bool)](sethidden(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethidden(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setalpha(_:))*