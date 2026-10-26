# inputWidth(_:height:pixelAspectRatio:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the width, height, and pixel aspect ratio of the input to the filter or transition for which the on-screen control is applied.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func inputWidth(_ inputWidth: UnsafeMutablePointer<Int>!, height inputHeight: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)
```

```objc
- (void) inputWidth:(NSUInteger *) inputWidth height:(NSUInteger *) inputHeight pixelAspectRatio:(double *) pixelAspectRatio;
```

## Parameters

- `inputWidth`: A pointer to the input width of the object.
- `inputHeight`: A pointer to the input height of the object.
- `pixelAspectRatio`: A pointer to the input pixel aspect ratio of the object.

## See Also

### Input and Output Item Geometry
- [func objectWidth(UnsafeMutablePointer<Int>!, height: UnsafeMutablePointer<Int>!, pixelAspectRatio: UnsafeMutablePointer<Double>!)](./objectwidth%28_,height,pixelaspectratio%29.md)
  Returns the width, height, and pixel aspect ratio of the object for which the on-screen control is applied.
- [func inputBounds() -> NSRect](./inputbounds%28%29.md)
  Returns the bounds of the input to the filter or transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/inputwidth(_:height:pixelaspectratio:))*