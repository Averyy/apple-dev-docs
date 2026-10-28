# zoomFactor

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The zoom factor for the live video in the camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var zoomFactor: Double { get set }
```

## Discussion

Set this property to a value between the [`minZoomFactor`](./minzoomfactor.md) and [`maxZoomFactor`](./maxzoomfactor.md) properties.

## See Also

### Zooming
- [var minZoomFactor: Double](./minzoomfactor.md)
  The minimum zoom factor that the camera supports.
- [var maxZoomFactor: Double](./maxzoomfactor.md)
  The maximum zoom factor that the camera supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/zoomfactor)*