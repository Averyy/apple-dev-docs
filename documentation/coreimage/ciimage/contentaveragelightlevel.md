# contentAverageLightLevel

**Framework**: Core Image  
**Kind**: property

Returns the content average light level of the image.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var contentAverageLightLevel: Float { get }
```

#### Discussion

If the image average light level is unknown, then the value 0.0 will be returned.

If the image headroom is known, then a value greater than or equal to 0.0 will be returned.

The image average light level may known when a CIImage is first initialized. If the a CIImage is initialized with a:

- `CGImage` : then the headroom will be determined by `CGImageGetContentAverageLightLevel()`.
- `CVPixelBuffer` : then the headroom will be determined by `kCVImageBufferContentLightLevelInfoKey`.

If the image is the result of applying a [`CIFilter`](cifilter-swift.class.md) or [`CIKernel`](cikernel.md), this property will return `0.0`.

There are exceptions to this.  Applying a [`CIWarpKernel`](ciwarpkernel.md) or certain [`CIFilter`](cifilter-swift.class.md) (e.g. `CIGaussianBlur`, `CILanczosScaleTransform`, `CIAreaAverage` and some others) to an image will result in a [`CIImage`](ciimage.md) instance with the same `contentAverageLightLevel` property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/contentaveragelightlevel)*