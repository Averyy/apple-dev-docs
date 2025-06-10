# createCGImage(_:from:format:colorSpace:deferred:calculateHDRStats:)

**Framework**: Core Image  
**Kind**: method

Creates a Core Graphics image from a region of a Core Image image instance with an option for calculating HDR statistics.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool, calculateHDRStats: Bool) -> CGImage?
```

#### Return Value

 Returns a new `CGImage` instance. You are responsible for releasing the returned image when you no longer need it. The returned value will be `null` if the extent is empty or too big.

## Parameters

- `image`: A   image instance for which to create a  .
- `fromRect`: The   region of the   to use.   This region relative to the cartesean coordinate system of  .   This region will be intersected with integralized and intersected with  .
- `format`: A   to specify the pixel format of the created  .   For example, if   is specified, then the created   will   be 16 bits-per-component and opaque.
- `colorSpace`: The   for the output image.   This color space must have either   or   and 
 and be compatible with the specified pixel format.
- `deferred`: Controls when Core Image renders  .
- `calculateHDRStats`: Controls if Core Image calculates HDR statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:deferred:calculatehdrstats:))*