# sizeToFitWidth()

**Framework**: Watchkit  
**Kind**: method

Sets the width of the object to fit its current content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func sizeToFitWidth()
```

## Overview

This method is equivalent of using the Size to Fit Content option in Interface Builder. It sizes the object so that its width matches the width of its content. For example, calling this method on a label sets the width of the label to the width of its text. The width of an object never exceeds the width of its container.

Changes to the width of an object are animatable.

## See Also

- [func setWidth(CGFloat)](setwidth(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:)))
- [func setHeight(CGFloat)](setheight(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:)))
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](setrelativewidth(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativewidth(_:withadjustment:)))
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](setrelativeheight(_:withadjustment:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setrelativeheight(_:withadjustment:)))
- [func sizeToFitHeight()](sizetofitheight().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth())*