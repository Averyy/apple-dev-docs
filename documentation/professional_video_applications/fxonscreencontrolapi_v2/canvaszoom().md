# canvasZoom()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the zoom factor the user has set the canvas

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func canvasZoom() -> Double
```

```objc
- (double) canvasZoom;
```

## Return Value

Returns the zoom factor the user has set for the canvas. The unit is a percentage.

## See Also

### Canvas Information
- [func canvasPixelAspectRatio() -> Double](./canvaspixelaspectratio%28%29.md)
  Returns the pixel aspect ratio of the canvas.
- [func pixelAspectRatio() -> Double](./pixelaspectratio%28%29.md)
  Returns the pixel aspect ratio for which the on-screen control applies.
- [func objectBounds() -> NSRect](./objectbounds%28%29.md)
  Returns the bounds of the object that the on-screen control applies to.
- [func objectToScreenTransform() -> FxMatrix44!](./objecttoscreentransform%28%29.md)
  Returns a 4x4 matrix describing the transformation from object normalized space


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/canvaszoom())*