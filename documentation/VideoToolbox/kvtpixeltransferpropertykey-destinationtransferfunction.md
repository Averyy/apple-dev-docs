# kVTPixelTransferPropertyKey_DestinationTransferFunction

**Framework**: Video Toolbox  
**Kind**: var

The color transfer function to be used for destination image buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTPixelTransferPropertyKey_DestinationTransferFunction: CFString
```

#### Discussion

Specifying this value may lead to performance degradation, as a color matching operation may need to be performed between the source and the destination.

See [`kCMFormatDescriptionExtension_TransferFunction`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_TransferFunction-swift.var) in `CMFormatDescription.h` for possible values.

## See Also

- [let kVTPixelTransferPropertyKey_ScalingMode: CFString](kvtpixeltransferpropertykey_scalingmode.md)
  Scaling mode for images during transfer between source and destination buffers.
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
- [let kVTPixelTransferPropertyKey_DestinationICCProfile: CFString](kvtpixeltransferpropertykey_destinationiccprofile.md)
  The International Color Consortium (ICC) profile for destination image buffers.
- [let kVTPixelTransferPropertyKey_DestinationYCbCrMatrix: CFString](kvtpixeltransferpropertykey_destinationycbcrmatrix.md)
  The color matrix to be used for YCbCr to RGB conversions involving the destination image buffers.
- [let kVTPixelTransferPropertyKey_RealTime: CFString](kvtpixeltransferpropertykey_realtime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationtransferfunction)*