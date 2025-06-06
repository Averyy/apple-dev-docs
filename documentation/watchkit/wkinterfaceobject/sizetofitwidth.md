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

#### Discussion

This method is equivalent of using the Size to Fit Content option in Interface Builder. It sizes the object so that its width matches the width of its content. For example, calling this method on a label sets the width of the label to the width of its text. The width of an object never exceeds the width of its container.

Changes to the width of an object are animatable.

## See Also

- [func setWidth(CGFloat)](wkinterfaceobject/setwidth(_:).md)
  Sets the absolute width (in points) of the object.
- [func setHeight(CGFloat)](wkinterfaceobject/setheight(_:).md)
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativewidth(_:withadjustment:).md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](wkinterfaceobject/setrelativeheight(_:withadjustment:).md)
  Sets the height of the object relative to its container.
- [func sizeToFitHeight()](wkinterfaceobject/sizetofitheight.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sizetofitwidth())*