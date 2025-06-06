# regionOfInterest(for:in:)

**Framework**: Core Image  
**Kind**: instm

Returns the region of interest for the filter chain that generates the image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func regionOfInterest(for image: CIImage, in rect: CGRect) -> CGRect
```

#### Return_value

A rectangle in the coordinate space of the input image (the `im` parameter).

#### Discussion

The region of interest is the rectangle containing pixel data in a source image (the `im` parameter) necessary to produce a corresponding rectangle in the output image. If the image is not the output of a filter (or of a chain or graph of several [`CIFilter`](cifilter.md) objects), or the image in the `im` parameter is not an input to that filter, the rectangle returned is the same as that in the `r` parameter.

For example,

- If the image is the output of a filter that doubles the size of its input image, the rectangle returned will be half the size of that in the `r` parameter. (Upscaling causes every pixel in the input image to correspond to multiple pixels in the output image.)
- If the image is the output of a blur filter, the rectangle returned will be slightly larger than that in the `r` parameter. (In a blur filter, each pixel in the output image is produced using information from the corresponding pixel and those immediately surrounding it in the input image.)

## Parameters

- `im`: Another image that is part of the filter chain that generates the image.
- `r`: A rectangle in the image’s coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/1437994-regionofinterest)*