# objectBounds()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the bounds of the object that the on-screen control applies to.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func objectBounds() -> NSRect
```

```objc
- (NSRect) objectBounds;
```

## Return Value

The rectangle of the on-screen control.

## See Also

### Canvas Information
- [func canvasZoom() -> Double](./canvaszoom%28%29.md)
  Returns the zoom factor the user has set the canvas
- [func canvasPixelAspectRatio() -> Double](./canvaspixelaspectratio%28%29.md)
  Returns the pixel aspect ratio of the canvas.
- [func pixelAspectRatio() -> Double](./pixelaspectratio%28%29.md)
  Returns the pixel aspect ratio for which the on-screen control applies.
- [func objectToScreenTransform() -> FxMatrix44!](./objecttoscreentransform%28%29.md)
  Returns a 4x4 matrix describing the transformation from object normalized space


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/objectbounds())*