# pixelAspectRatio()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the pixel aspect ratio for which the on-screen control applies.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func pixelAspectRatio() -> Double
```

```objc
- (double) pixelAspectRatio;
```

#### Return Value

The pixel aspect ratio of the on-screen control.

## See Also

### Canvas Information
- [func canvasZoom() -> Double](./canvaszoom%28%29.md)
  Returns the zoom factor the user has set the canvas
- [func canvasPixelAspectRatio() -> Double](./canvaspixelaspectratio%28%29.md)
  Returns the pixel aspect ratio of the canvas.
- [func objectBounds() -> NSRect](./objectbounds%28%29.md)
  Returns the bounds of the object that the on-screen control applies to.
- [func objectToScreenTransform() -> FxMatrix44!](./objecttoscreentransform%28%29.md)
  Returns a 4x4 matrix describing the transformation from object normalized space


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/pixelaspectratio())*