# setWidth(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the absolute width (in points) of the object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setWidth(_ width: CGFloat)
```

#### Discussion

You cannot use this method to alter the width of tables or the thickness of vertical separator items. Changing the width of a [`WKInterfaceImage`](wkinterfaceimage.md) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill).

Changes to the width of an object are animatable.

## Parameters

- `width`: The new width of the object. Specifying a value of   causes the item to have no width.

## See Also

- [func setHeight(CGFloat)](wkinterfaceobject/setheight(_:).md)
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativewidth(_:withadjustment:).md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](wkinterfaceobject/sizetofitwidth.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](wkinterfaceobject/sizetofitheight.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:))*