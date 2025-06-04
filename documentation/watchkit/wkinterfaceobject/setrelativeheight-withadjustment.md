# setRelativeHeight(_:withAdjustment:)

**Framework**: Watchkit  
**Kind**: method

Sets the height of the object relative to its container.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)
```

## Overview

You can’t use this method to alter the height of tables or separator items. Changes to the height of an object are animatable.

## Parameters

- `height`: The height of the object relative to its immediate container. This value represents the percentage of the container’s height. This value must be between   and  , and values outside of that range are clamped to the minimum or maximum value.
- `adjustment`: The amount (in points) to add or subtract from the relative height. Positive values increase the height of the item and negative values decrease it.

## See Also

- [func setWidth(CGFloat)](setwidth(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:)))
- [func setHeight(CGFloat)](setheight(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:)))
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
- [func sizeToFitWidth()](sizetofitwidth().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth()))
- [func sizeToFitHeight()](sizetofitheight().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:))*