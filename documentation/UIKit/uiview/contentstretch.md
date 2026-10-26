# contentStretch

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that defines the stretchable and nonstretchable regions of a view.

**Availability**:
- iOS 3.0+ - Deprecated in 6.0
- iPadOS 3.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: To achieve the same effect, use [`resizableImage(withCapInsets:)`](../uiimage/resizableimage%28withcapinsets%29.md) instead.

## Declaration

```objc
@property (nonatomic) CGRect contentStretch;
```

#### Discussion

You use this property to control how a view’s content is stretched to fill its bounds when the view is resized. Content stretching is often used to animate the resizing of a view. For example, buttons and other controls use stretching to maintain crisp borders while allowing the middle portions of the control to stretch and fill the available space.

> **Note**:  For stretching image-based content, it is simpler to use a [`UIImageView`](../uiimageview.md) object with a stretchable image instead of setting this property. You can create a stretchable image using the [`stretchableImage(withLeftCapWidth:topCapHeight:)`](../uiimage/stretchableimage%28withleftcapwidth,topcapheight%29.md) method of [`UIImage`](../uiimage.md).

The values you specify for this rectangle must be normalized to the range `0.0` to `1.0`. These values are then scaled to the size of the view’s content to obtain the appropriate pixel values. The default value for this rectangle has an origin of `(0.0, 0.0)` and a size of `(1.0, 1.0)`. This reflects a rectangle whose stretchable portion encompasses the entire content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/contentstretch)*