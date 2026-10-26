# objectWidth(_:height:pixelAspectRatio:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the width, height, and pixel aspect ratio of the object for which the on-screen control is applied.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func objectWidth(_ outputWidth: UnsafeMutablePointer<Int>!, height outputHeight: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)
```

```objc
- (void) objectWidth:(NSUInteger *) outputWidth height:(NSUInteger *) outputHeight pixelAspectRatio:(double *) pixelAspectRatio;
```

## Parameters

- `outputWidth`: A pointer to the width of the object.
- `outputHeight`: A pointer to the height of the object.
- `pixelAspectRatio`: A pointer to the pixel aspect ratio of the object.

## See Also

### Input and Output Item Geometry
- [func inputWidth(UnsafeMutablePointer<Int>!, height: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)](./inputwidth%28_,height,pixelaspectratio%29.md)
  Returns the width, height, and pixel aspect ratio of the input to the filter or transition for which the on-screen control is applied.
- [func inputBounds() -> NSRect](./inputbounds%28%29.md)
  Returns the bounds of the input to the filter or transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/objectwidth(_:height:pixelaspectratio:))*