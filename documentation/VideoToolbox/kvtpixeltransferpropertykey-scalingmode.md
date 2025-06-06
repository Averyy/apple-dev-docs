# kVTPixelTransferPropertyKey_ScalingMode

**Framework**: Videotoolbox  
**Kind**: var

Scaling mode for images during transfer between source and destination buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTPixelTransferPropertyKey_ScalingMode: CFString
```

#### Discussion

Depending on the scaling mode, scaling may take into account:

- The full image buffer width and height of the source and destination
- The clean aperture attachment ([`kCVImageBufferCleanApertureKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferCleanApertureKey)) on the source image buffer
- The pixel aspect ratio attachment ([`kCVImageBufferPixelAspectRatioKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferPixelAspectRatioKey)) on the source image buffer
- The destination clean aperture ([`kVTPixelTransferPropertyKey_DestinationCleanAperture`](kvtpixeltransferpropertykey_destinationcleanaperture.md))
- The destination pixel aspect ratio ([`kVTPixelTransferPropertyKey_DestinationPixelAspectRatio`](kvtpixeltransferpropertykey_destinationpixelaspectratio.md))

The destination image buffer’s clean aperture and pixel aspect ratio attachments are not taken into account, and are overwritten.

## See Also

- [Scaling Mode Constants](scaling-mode-constants.md)
  Supported constant values for the [`kVTPixelTransferPropertyKey_ScalingMode`](kvtpixeltransferpropertykey_scalingmode.md) key.
- [let kVTPixelTransferPropertyKey_DestinationCleanAperture: CFString](kvtpixeltransferpropertykey_destinationcleanaperture.md)
  The clean aperture for destination image buffers.
- [let kVTPixelTransferPropertyKey_DestinationPixelAspectRatio: CFString](kvtpixeltransferpropertykey_destinationpixelaspectratio.md)
  The pixel aspect ratio for destination image buffers.
- [let kVTPixelTransferPropertyKey_DownsamplingMode: CFString](kvtpixeltransferpropertykey_downsamplingmode.md)
  The specific chroma downsampling technique to be used.
- [Downsampling Mode Constants](downsampling-mode-constants.md)
  Supported constant values for the [`kVTPixelTransferPropertyKey_DownsamplingMode`](kvtpixeltransferpropertykey_downsamplingmode.md) key.
- [let kVTPixelTransferPropertyKey_DestinationColorPrimaries: CFString](kvtpixeltransferpropertykey_destinationcolorprimaries.md)
  The color primaries to be used for destination image buffers.
- [let kVTPixelTransferPropertyKey_DestinationTransferFunction: CFString](kvtpixeltransferpropertykey_destinationtransferfunction.md)
  The color transfer function to be used for destination image buffers.
- [let kVTPixelTransferPropertyKey_DestinationICCProfile: CFString](kvtpixeltransferpropertykey_destinationiccprofile.md)
  The International Color Consortium (ICC) profile for destination image buffers.
- [let kVTPixelTransferPropertyKey_DestinationYCbCrMatrix: CFString](kvtpixeltransferpropertykey_destinationycbcrmatrix.md)
  The color matrix to be used for YCbCr to RGB conversions involving the destination image buffers.
- [let kVTPixelTransferPropertyKey_RealTime: CFString](kvtpixeltransferpropertykey_realtime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_scalingmode)*