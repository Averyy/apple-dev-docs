# kVTPixelTransferPropertyKey_DestinationPixelAspectRatio

**Framework**: Video Toolbox  
**Kind**: var

The pixel aspect ratio for destination image buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTPixelTransferPropertyKey_DestinationPixelAspectRatio: CFString
```

#### Discussion

The value of this property is a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) object with same keys as used in the [`kCVImageBufferPixelAspectRatioKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferPixelAspectRatioKey) dictionary.

This property is ignored in [`kVTScalingMode_Normal`](kvtscalingmode_normal.md).  This property defaults to `NULL`, meaning 1:1 (for [`kVTScalingMode_CropSourceToCleanAperture`](kvtscalingmode_cropsourcetocleanaperture.md)) or no change in pixel aspect ratio (for [`kVTScalingMode_Letterbox`](kvtscalingmode_letterbox.md) and [`kVTScalingMode_Trim`](kvtscalingmode_trim.md)).

## See Also

- [let kVTPixelTransferPropertyKey_ScalingMode: CFString](kvtpixeltransferpropertykey_scalingmode.md)
  Scaling mode for images during transfer between source and destination buffers.
- [Scaling Mode Constants](scaling-mode-constants.md)
  Supported constant values for the [`kVTPixelTransferPropertyKey_ScalingMode`](kvtpixeltransferpropertykey_scalingmode.md) key.
- [let kVTPixelTransferPropertyKey_DestinationCleanAperture: CFString](kvtpixeltransferpropertykey_destinationcleanaperture.md)
  The clean aperture for destination image buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationpixelaspectratio)*