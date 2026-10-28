# maximumValueImageRect(forBounds:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the maximum value image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func maximumValueImageRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) maximumValueImageRectForBounds:(CGRect) bounds;
```

## Return Value

The computed drawing rectangle for the image.

## Discussion

You do not call this method directly. Instead, you override it when you want to customize the rectangle in which the maximum value image is drawn, returning a different rectangle. If you make x-axis adjustments, be sure to take into account the automatic flipping of [`maximumValueImage`](./maximumvalueimage.md) in a right-to-left user interface; the maximum image is always shown at the trailing end of the slider’s track. See the [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for further information about supporting right-to-left languages.

## Parameters

- `bounds`: The bounding rectangle of the slider.

## See Also

### Overrides for subclasses
- [func minimumValueImageRect(forBounds: CGRect) -> CGRect](./minimumvalueimagerect%28forbounds%29.md)
  Returns the drawing rectangle for the minimum value image.
- [func trackRect(forBounds: CGRect) -> CGRect](./trackrect%28forbounds%29.md)
  Returns the drawing rectangle for the slider’s track.
- [func thumbRect(forBounds: CGRect, trackRect: CGRect, value: Float) -> CGRect](./thumbrect%28forbounds,trackrect,value%29.md)
  Returns the drawing rectangle for the slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/maximumvalueimagerect(forbounds:))*