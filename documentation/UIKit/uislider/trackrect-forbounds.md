# trackRect(forBounds:)

**Framework**: UIKit  
**Kind**: method

Returns the drawing rectangle for the slider’s track.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func trackRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The computed drawing rectangle for the track. This rectangle corresponds to the entire length of the track between the minimum and maximum value images.

#### Discussion

You do not call this method directly. Instead, you override it when you want to customize the track rectangle, returning a different rectangle. The returned rectangle is used to scale the track and thumb images during drawing.

## Parameters

- `bounds`: The bounding rectangle of the slider.

## See Also

- [func maximumValueImageRect(forBounds: CGRect) -> CGRect](uislider/maximumvalueimagerect(forbounds:).md)
  Returns the drawing rectangle for the maximum value image.
- [func minimumValueImageRect(forBounds: CGRect) -> CGRect](uislider/minimumvalueimagerect(forbounds:).md)
  Returns the drawing rectangle for the minimum value image.
- [func thumbRect(forBounds: CGRect, trackRect: CGRect, value: Float) -> CGRect](uislider/thumbrect(forbounds:trackrect:value:).md)
  Returns the drawing rectangle for the slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/trackrect(forbounds:))*