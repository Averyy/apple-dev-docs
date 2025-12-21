# contentHeadroom

**Framework**: Core Image  
**Kind**: property

Returns the content headroom of the image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var contentHeadroom: Float { get }
```

#### Discussion

If the image headroom is unknown, then the value 0.0 will be returned.

If the image headroom is known, then a value greater than or equal to 1.0 will be returned. A value of 1.0 will be returned if the image is SDR. A value greater than 1.0 will be returned if the image is HDR.

The image headroom may known when a CIImage is first initialized. If the a CIImage is initialized using:

- `NSURL` or `NSData` : the headroom may be determined by associated metadata or deduced from pixel format or colorSpace information.
- `CGImage` : headroom may be determined by `CGImageGetHeadroomInfo()` or deduced from pixel format or colorSpace information.
- `IOSurface` : then the headroom will be determined by `kIOSurfaceContentHeadroom`. or deduced from pixel format or colorSpace information.
- `CVPixelBuffer` : then the headroom will be determined by `kCVImageBufferContentLightLevelInfoKey`. or deduced from pixel format or colorSpace information.
- `BitmapData` : headroom may be deduced from pixel format or colorSpace information.

If the image is the result of applying a [`CIFilter`](cifilter-swift.class.md) or [`CIKernel`](cikernel.md), this method will return `0.0`.

There are exceptions to this.  Applying a `CIWarpKernel`` or certain ``CIFilter-class``  (e.g. `CIGaussianBlur`, `CILanczosScaleTransform`, `CIAreaAverage`and some others)  to an image will result in a ``CIImage`` instance with the same`contentHeadroom` property value.

## See Also

- [var isOpaque: Bool](ciimage/isopaque.md)
  Returns YES if the image is known to have and alpha value of `1.0` over the entire image extent.
- [var metalTexture: (any MTLTexture)?](ciimage/metaltexture.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/contentheadroom)*