# thumbRect(forBounds:trackRect:value:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the slider’s thumb image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func thumbRect(forBounds bounds: CGRect, trackRect rect: CGRect, value: Float) -> CGRect
```

```objc
- (CGRect) thumbRectForBounds:(CGRect) bounds trackRect:(CGRect) rect value:(float) value;
```

## Return Value

The computed drawing rectangle for the thumb image.

## Discussion

You do not call this method directly. Instead, you override it when you want to customize the thumb image’s drawing rectangle, returning a different rectangle. The rectangle you return must reflect the size of your thumb image and its current position on the slider’s track.

## Parameters

- `bounds`: The bounding rectangle of the slider.
- `rect`: The drawing rectangle for the slider’s track, as returned by the [`trackRect(forBounds:)`](./trackrect%28forbounds%29.md) method.
- `value`: The current value of the slider.

## See Also

### Overrides for subclasses
- [func maximumValueImageRect(forBounds: CGRect) -> CGRect](./maximumvalueimagerect%28forbounds%29.md)
  Returns the drawing rectangle for the maximum value image.
- [func minimumValueImageRect(forBounds: CGRect) -> CGRect](./minimumvalueimagerect%28forbounds%29.md)
  Returns the drawing rectangle for the minimum value image.
- [func trackRect(forBounds: CGRect) -> CGRect](./trackrect%28forbounds%29.md)
  Returns the drawing rectangle for the slider’s track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/thumbrect(forbounds:trackrect:value:))*