# setHeight(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the absolute height (in points) of the object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setHeight(_ height: CGFloat)
```

## Overview

You cannot use this method to alter the height of tables or the thickness of horizontal separator items. Changing the height of a [`WKInterfaceImage`](https://developer.apple.com/documentation/watchkit/wkinterfaceimage) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum/scaleToFill).

Changes to the height of an object are animatable.

## Parameters

- `height`: The new height of the object. Specifying a value of   causes the item to have no height.

## See Also

- [func setWidth(CGFloat)](setwidth(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:)))
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](setrelativeheight(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:)))
- [func sizeToFitWidth()](sizetofitwidth().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth()))
- [func sizeToFitHeight()](sizetofitheight().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:))*