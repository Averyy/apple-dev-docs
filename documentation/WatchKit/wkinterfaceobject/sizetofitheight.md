# sizeToFitHeight()

**Framework**: WatchKit  
**Kind**: method

Sets the height of the object so that it fills the available vertical space.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func sizeToFitHeight()
```

#### Discussion

This method is equivalent of using the Size to Fit Content option in Interface Builder. It sizes the object so that its height matches the height of its content. For example, calling this method on a label sets the height of the label to the height of its text. The height of an object never exceeds the height of its container.

Changes to the height of an object are animatable.

## See Also

- [func setWidth(CGFloat)](wkinterfaceobject/setwidth(_:).md)
  Sets the absolute width (in points) of the object.
- [func setHeight(CGFloat)](wkinterfaceobject/setheight(_:).md)
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativewidth(_:withadjustment:).md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](wkinterfaceobject/sizetofitwidth.md)
  Sets the width of the object to fit its current content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitheight())*