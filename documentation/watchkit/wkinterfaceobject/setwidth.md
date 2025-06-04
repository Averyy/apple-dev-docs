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

You cannot use this method to alter the width of tables or the thickness of vertical separator items. Changing the width of a [`WKInterfaceImage`](https://developer.apple.com/documentation/watchkit/wkinterfaceimage) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill).

Changes to the width of an object are animatable.

## Parameters

- `width`: The new width of the object. Specifying a value of   causes the item to have no width.

## See Also

- [func setHeight(CGFloat)](setheight(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:)))
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](setrelativeheight(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:)))
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](sizetofitwidth().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth()))
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](sizetofitheight().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight()))
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:))*