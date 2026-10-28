# inputBounds()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the bounds of the input to the filter or transition.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func inputBounds() -> NSRect
```

```objc
- (NSRect) inputBounds;
```

## Return Value

The bounds of the input filter or transition.

## See Also

### Input and Output Item Geometry
- [func objectWidth(UnsafeMutablePointer<Int>!, height: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)](./objectwidth%28_,height,pixelaspectratio%29.md)
  Returns the width, height, and pixel aspect ratio of the object for which the on-screen control is applied.
- [func inputWidth(UnsafeMutablePointer<Int>!, height: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)](./inputwidth%28_,height,pixelaspectratio%29.md)
  Returns the width, height, and pixel aspect ratio of the input to the filter or transition for which the on-screen control is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/inputbounds())*