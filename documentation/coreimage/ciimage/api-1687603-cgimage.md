# cgImage

**Framework**: Core Image  
**Kind**: instp

The CoreGraphics image object this image was created from, if applicable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cgImage: CGImage? { get }
```

#### Discussion

If this image was created using the [`init(cgImage:)`](ciimage/1437986-init.md) or [`init(contentsOf:)`](ciimage/1437908-init.md) initializer, this property’s value is the [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage) object that provides the image’s underlying image data. Otherwise, this property’s value is `nil`—in this case you can obtain a CoreGraphics image by rendering the image with the [`CIContext`](cicontext.md) [`createCGImage(_:from:)`](cicontext/1437784-createcgimage.md) method.

## See Also

- [var pixelBuffer: CVPixelBuffer?](ciimage/1687604-pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](ciimage/2902251-depthdata.md)
  [`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata) representation of the depth image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/2976440-portraiteffectsmatte.md)
  [`AVPortraitEffectsMatte`](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte) representation of portrait effects.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/3242781-semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1687603-cgimage)*