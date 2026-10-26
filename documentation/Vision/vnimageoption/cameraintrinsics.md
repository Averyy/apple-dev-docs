# cameraIntrinsics

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

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

```c
extern VNImageOption const VNImageOptionCameraIntrinsics;
```

#### Discussion

The camera intrinsics matrix is a [`CFData`](../../CoreFoundation/cfdata.md) instance containing a [`matrix_float3x3`](../../simd/matrix_float3x3.md), which is a column-major matrix:

![The camera intrinsics matrix with focal length along the main diagonal](https://developer.apple.com/tutorials/images/Vision/media-2954520@2x.png)

`fx` and `fy` are the focal length in pixels. For square pixels, they have the same value.

`ox` and `oy` are the coordinates of the principal point.  The origin is the upper-left corner of the frame.

## See Also

### Options Dictionary Keys
- [static let properties: VNImageOption](./properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let ciContext: VNImageOption](./cicontext.md)
  An option key to specify the context to use in the handler’s Core Image operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption/cameraintrinsics)*