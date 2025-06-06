# setRelativeWidth(_:withAdjustment:)

**Framework**: Watchkit  
**Kind**: method

Sets the width of the object relative to its container.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)
```

#### Discussion

You cannot use this method to alter the height of tables or separator items. Changes to the width of an object are animatable.

## Parameters

- `width`: The width of the object relative to its immediate container. This value represents the percentage of the container’s width. This value must be between   and  , and values outside of that range are clamped to the minimum or maximum value.
- `adjustment`: The amount (in points) to add or subtract from the relative width. Positive values increase the width of the item and negative values decrease it.

## See Also

- [func setWidth(CGFloat)](wkinterfaceobject/setwidth(_:).md)
  Sets the absolute width (in points) of the object.
- [func setHeight(CGFloat)](wkinterfaceobject/setheight(_:).md)
  Sets the absolute height (in points) of the object.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](wkinterfaceobject/sizetofitwidth.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](wkinterfaceobject/sizetofitheight.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:))*