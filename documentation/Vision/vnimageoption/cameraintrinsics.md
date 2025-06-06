# cameraIntrinsics

**Framework**: Vision  
**Kind**: property

An option to specify the camera intrinstics.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let cameraIntrinsics: VNImageOption
```

#### Discussion

The camera intrinsics matrix is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) instance containing a [`matrix_float3x3`](https://developer.apple.com/documentation/simd/matrix_float3x3), which is a column-major matrix:

![The camera intrinsics matrix with focal length along the main diagonal](https://docs-assets.developer.apple.com/published/af0173b4c72c1996604b206571a6ae6d/media-2954520%402x.png)

`fx` and `fy` are the focal length in pixels. For square pixels, they have the same value.

`ox` and `oy` are the coordinates of the principal point.  The origin is the upper-left corner of the frame.

## See Also

- [static let properties: VNImageOption](vnimageoption/properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let ciContext: VNImageOption](vnimageoption/cicontext.md)
  An option key to specify the context to use in the handler’s Core Image operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption/cameraintrinsics)*