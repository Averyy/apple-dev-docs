# sizeToFitHeight()

**Framework**: Watchkit  
**Kind**: method

Sets the height of the object so that it fills the available vertical space.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func sizeToFitHeight()
```

## Overview

This method is equivalent of using the Size to Fit Content option in Interface Builder. It sizes the object so that its height matches the height of its content. For example, calling this method on a label sets the height of the label to the height of its text. The height of an object never exceeds the height of its container.

Changes to the height of an object are animatable.

## See Also

- [func setWidth(CGFloat)](setwidth(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:)))
- [func setHeight(CGFloat)](setheight(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:)))
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](setrelativeheight(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:)))
- [func sizeToFitWidth()](sizetofitwidth().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight())*