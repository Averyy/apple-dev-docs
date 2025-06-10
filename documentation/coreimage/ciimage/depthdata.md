# depthData

**Framework**: Core Image  
**Kind**: property

Depth data associated with the image.

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

Returns an [`AVDepthData`](https://developer.apple.com/documentation/AVFoundation/AVDepthData) if the [`CIImage`](ciimage.md) was created with [`imageWithData:`](ciimage/imagewithdata:.md) or [`imageWithContentsOfURL:`](ciimage/imagewithcontentsofurl:.md) and one of the options [`auxiliaryDepth`](ciimageoption/auxiliarydepth.md) or [`auxiliaryDisparity`](ciimageoption/auxiliarydisparity.md), otherwise [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

## See Also

- [var cgImage: CGImage?](ciimage/cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](ciimage/pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/depthdata)*