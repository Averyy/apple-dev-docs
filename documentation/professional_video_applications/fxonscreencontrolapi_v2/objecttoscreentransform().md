# objectToScreenTransform()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a 4x4 matrix describing the transformation from object normalized space

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func objectToScreenTransform() -> FxMatrix44!
```

```objc
- (FxMatrix44 *) objectToScreenTransform;
```

#### Return Value

An Raw Matrix Data Format describing the transformation from object normalized space (0-1 in both width and height) to screen space.

## See Also

### Canvas Information
- [func canvasZoom() -> Double](./canvaszoom%28%29.md)
  Returns the zoom factor the user has set the canvas
- [func canvasPixelAspectRatio() -> Double](./canvaspixelaspectratio%28%29.md)
  Returns the pixel aspect ratio of the canvas.
- [func pixelAspectRatio() -> Double](./pixelaspectratio%28%29.md)
  Returns the pixel aspect ratio for which the on-screen control applies.
- [func objectBounds() -> NSRect](./objectbounds%28%29.md)
  Returns the bounds of the object that the on-screen control applies to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v2/objecttoscreentransform())*