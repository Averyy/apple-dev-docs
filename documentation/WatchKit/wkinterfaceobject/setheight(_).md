# setHeight(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the absolute height (in points) of the object.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setHeight(_ height: CGFloat)
```

```objc
- (void) setHeight:(CGFloat) height;
```

#### Discussion

You cannot use this method to alter the height of tables or the thickness of horizontal separator items. Changing the height of a [`WKInterfaceImage`](../wkinterfaceimage.md) object causes the image’s content scaling mode to change to [`UIView.ContentMode.scaleToFill`](../../UIKit/uiview/contentmode-swift.enum/scaletofill.md).

Changes to the height of an object are animatable.

## Parameters

- `height`: The new height of the object. Specifying a value of `0.0` causes the item to have no height.

## See Also

### Changing an Object’s Size
- [func setWidth(CGFloat)](./setwidth%28_%29.md)
  Sets the absolute width (in points) of the object.
- [func setRelativeWidth(CGFloat, withAdjustment: CGFloat)](./setrelativewidth%28_,withadjustment%29.md)
  Sets the width of the object relative to its container.
- [func setRelativeHeight(CGFloat, withAdjustment: CGFloat)](./setrelativeheight%28_,withadjustment%29.md)
  Sets the height of the object relative to its container.
- [func sizeToFitWidth()](./sizetofitwidth%28%29.md)
  Sets the width of the object to fit its current content.
- [func sizeToFitHeight()](./sizetofitheight%28%29.md)
  Sets the height of the object so that it fills the available vertical space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setheight(_:))*