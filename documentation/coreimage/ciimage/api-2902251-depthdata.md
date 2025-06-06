# depthData

**Framework**: Core Image  
**Kind**: instp

[`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata) representation of the depth image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var depthData: AVDepthData? { get }
```

#### Discussion

Returns an [`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata) if the [`CIImage`](ciimage.md) was created with [`imageWithData:`](ciimage/1547029-imagewithdata.md) or [`imageWithContentsOfURL:`](ciimage/1547027-imagewithcontentsofurl.md) and one of the options [`auxiliaryDepth`](ciimageoption/2890795-auxiliarydepth.md) or [`auxiliaryDisparity`](ciimageoption/2890794-auxiliarydisparity.md), otherwise [`nil`](https://developer.apple.com/documentation/objectivec/nil-2gl).

## See Also

- [var cgImage: CGImage?](ciimage/1687603-cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](ciimage/1687604-pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/2976440-portraiteffectsmatte.md)
  [`AVPortraitEffectsMatte`](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte) representation of portrait effects.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/3242781-semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/2902251-depthdata)*