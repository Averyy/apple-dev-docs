# FxRectsAreEqual(_:_:)

**Framework**: Professional Video Applications  
**Kind**: func  
**Role**: Function

Compares two rectangle structures and determines if they are equal.

**Availability**:
- FxPlug 4.2.2+

## Declaration

```swift
func FxRectsAreEqual(_ thisRect: FxRect, _ thatRect: FxRect) -> Bool
```

```c
bool FxRectsAreEqual(FxRect thisRect, FxRect thatRect);
```

#### Return Value

A Boolean indicating if the two rectangles are equal.

## Parameters

- `thisRect`: An [`FxRect`](./fxrect.md).
- `thatRect`: An [`FxRect`](./fxrect.md).

## See Also

### Determining input and output bounds
- [func sourceTileRect(UnsafeMutablePointer<FxRect>, sourceImageIndex: Int, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./fxtileableeffect/sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md)
  Calculate the input rectangle needed for the given image input and the output tile to be rendered.
- [func destinationImageRect(UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at: CMTime) throws](./fxtileableeffect/destinationimagerect%28_,sourceimages,destinationimage,pluginstate,at%29.md)
  Calculates the bounds of the output image determined by the various inputs and plug-in state at the given render time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxrectsareequal(_:_:))*