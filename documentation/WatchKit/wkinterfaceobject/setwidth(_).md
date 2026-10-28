# setWidth(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the absolute width (in points) of the object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setWidth(_ width: CGFloat)
```

```objc
- (void) setWidth:(CGFloat) width;
```

## Discussion

You cannot use this method to alter the width of tables or the thickness of vertical separator items. Changing the width of a [`WKInterfaceImage`](../wkinterfaceimage.md) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](../../UIKit/uiview/contentmode-swift.enum/scaletofill.md).

Changes to the width of an object are animatable.

## Parameters

- `width`: The new width of the object. Specifying a value of `0.0` causes the item to have no width.

## See Also

### Changing an Object’s Size
- [func setHeight(CGFloat)](./setheight%28_%29.md)
  Sets the absolute height (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](./setrelativewidth%28_,withadjustment%29.md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](./setrelativeheight%28_,withadjustment%29.md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](./sizetofitwidth%28%29.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](./sizetofitheight%28%29.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setwidth(_:))*