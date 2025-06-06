# thumbRect(forBounds:trackRect:value:)

**Framework**: UIKit  
**Kind**: method

Returns the drawing rectangle for the slider’s thumb image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func thumbRect(forBounds bounds: CGRect, trackRect rect: CGRect, value: Float) -> CGRect
```

#### Return Value

The computed drawing rectangle for the thumb image.

#### Discussion

You do not call this method directly. Instead, you override it when you want to customize the thumb image’s drawing rectangle, returning a different rectangle. The rectangle you return must reflect the size of your thumb image and its current position on the slider’s track.

## Parameters

- `bounds`: The bounding rectangle of the slider.
- `rect`: The drawing rectangle for the slider’s track, as returned by the   method.
- `value`: The current value of the slider.

## See Also

- [func maximumValueImageRect(forBounds: CGRect) -> CGRect](uislider/maximumvalueimagerect(forbounds:).md)
  Returns the drawing rectangle for the maximum value image.
- [func minimumValueImageRect(forBounds: CGRect) -> CGRect](uislider/minimumvalueimagerect(forbounds:).md)
  Returns the drawing rectangle for the minimum value image.
- [func trackRect(forBounds: CGRect) -> CGRect](uislider/trackrect(forbounds:).md)
  Returns the drawing rectangle for the slider’s track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/thumbrect(forbounds:trackrect:value:))*