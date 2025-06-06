# minimumValueImageRect(forBounds:)

**Framework**: UIKit  
**Kind**: method

Returns the drawing rectangle for the minimum value image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func minimumValueImageRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The computed drawing rectangle for the image.

#### Discussion

You do not call this method directly. Instead, you override it when you want to customize the rectangle in which the minimum value image is drawn, returning a different rectangle. If you make x-axis adjustments, be sure to take into account the automatic flipping of [`minimumValueImage`](uislider/minimumvalueimage.md) in a right-to-left user interface; the minimum image is always shown at the leading end of the slider’s track. See the [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for further information about supporting right-to-left languages.

## Parameters

- `bounds`: The bounding rectangle of the slider.

## See Also

- [func maximumValueImageRect(forBounds: CGRect) -> CGRect](uislider/maximumvalueimagerect(forbounds:).md)
  Returns the drawing rectangle for the maximum value image.
- [func trackRect(forBounds: CGRect) -> CGRect](uislider/trackrect(forbounds:).md)
  Returns the drawing rectangle for the slider’s track.
- [func thumbRect(forBounds: CGRect, trackRect: CGRect, value: Float) -> CGRect](uislider/thumbrect(forbounds:trackrect:value:).md)
  Returns the drawing rectangle for the slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/minimumvalueimagerect(forbounds:))*