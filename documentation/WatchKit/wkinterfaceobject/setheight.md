# setHeight(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the absolute height (in points) of the object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setHeight(_ height: CGFloat)
```

#### Discussion

You cannot use this method to alter the height of tables or the thickness of horizontal separator items. Changing the height of a [`WKInterfaceImage`](wkinterfaceimage.md) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill).

Changes to the height of an object are animatable.

## Parameters

- `height`: The new height of the object. Specifying a value of   causes the item to have no height.

## See Also

- [func setWidth(CGFloat)](wkinterfaceobject/setwidth(_:).md)
  Sets the absolute width (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativewidth(_:withadjustment:).md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](wkinterfaceobject/sizetofitwidth.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](wkinterfaceobject/sizetofitheight.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:))*