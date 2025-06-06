# pixelBuffer

**Framework**: Core Image  
**Kind**: instp

The CoreVideo pixel buffer this image was created from, if applicable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

#### Discussion

If this image was create using the [`init(cvPixelBuffer:)`](ciimage/1438072-init.md) initializer, this property’s value is the [`CVPixelBuffer`](https://developer.apple.com/documentation/corevideo/cvpixelbuffer) object that provides the image’s underlying image data. Do not modify the contents of this pixel buffer; doing so will cause undefined rendering results.

Otherwise, this property’s value is `nil`—in this case you can obtain a pixel buffer by rendering the image with the [`CIContext`](cicontext.md) [`render(_:to:)`](cicontext/1437853-render.md) method.

## See Also

- [var cgImage: CGImage?](ciimage/1687603-cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var depthData: AVDepthData?](ciimage/2902251-depthdata.md)
  [`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata) representation of the depth image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/2976440-portraiteffectsmatte.md)
  [`AVPortraitEffectsMatte`](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte) representation of portrait effects.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/3242781-semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1687604-pixelbuffer)*