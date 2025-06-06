# Scaling Mode Constants

**Framework**: Videotoolbox

Supported constant values for the [`kVTPixelTransferPropertyKey_ScalingMode`](kvtpixeltransferpropertykey_scalingmode.md) key.

## Topics

### Scaling Modes
- [let kVTScalingMode_Normal: CFString](kvtscalingmode_normal.md)
  The full width and height of the source image buffer is stretched to the full width and height of the destination image buffer.
- [let kVTScalingMode_CropSourceToCleanAperture: CFString](kvtscalingmode_cropsourcetocleanaperture.md)
  The source image buffer’s clean aperture is scaled to the destination clean aperture.
- [let kVTScalingMode_Letterbox: CFString](kvtscalingmode_letterbox.md)
  The source image buffer’s clean aperture is scaled to a rectangle fitted inside the  destination clean aperture that preserves the source picture aspect ratio.
- [let kVTScalingMode_Trim: CFString](kvtscalingmode_trim.md)
  The source image buffer’s clean aperture is scaled to a rectangle that completely fills the destination clean aperture and preserves the source picture aspect ratio.

## See Also

- [let kVTPixelTransferPropertyKey_ScalingMode: CFString](kvtpixeltransferpropertykey_scalingmode.md)
  Scaling mode for images during transfer between source and destination buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/scaling-mode-constants)*