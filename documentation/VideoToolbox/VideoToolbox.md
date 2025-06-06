# Video Toolbox

**Framework**: Videotoolbox  
**Kind**: module

Work directly with hardware-accelerated video encoding and decoding capabilities.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

#### Overview

VideoToolbox is a low-level framework that provides direct access to hardware encoders and decoders. It provides services for video compression and decompression, and for conversion between raster image formats stored in CoreVideo pixel buffers. These services are provided in the form of session objects (compression, decompression, and pixel transfer), which are vended as Core Foundation (CF) types. Apps that don’t need direct access to hardware encoders and decoders shouldn’t need to use VideoToolbox directly.

## Topics

### Frame Processing
- [Frame processing](frame-processing.md)
  An interface used to access a range of different video processing features.
### Compression
- [Encoding video for low-latency conferencing](encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTCompressionSession](vtcompressionsession-api-collection.md)
  An object that compresses video data.
- [VTDecompressionSession](vtdecompressionsession-api-collection.md)
  An object that decompresses video data.
- [VTFrameSilo](vtframesilo-api-collection.md)
  An object that stores sample buffers from a multipass encoding session.
- [VTMultiPassStorage](vtmultipassstorage-api-collection.md)
  An object that stores video encoding metadata from a multipass encoding session.
### Transformation
- [VTPixelTransferSession](vtpixeltransfersession-api-collection.md)
  An object converts video data from source pixel buffers to destination pixel buffers.
- [VTPixelRotationSession](vtpixelrotationsession-api-collection.md)
  An object that rotates source pixel buffers to destination pixel buffers.
### RAW Processing
- [class VTRAWProcessingSession](vtrawprocessingsession.md)
  An object that processes frames in camera native formats such as RAW or Bayer.
### Media Extension
- [struct VTExtensionPropertiesKey](vtextensionpropertieskey.md)
  A key in a Media Extension extension properties dictionary.
### HDR Metadata
- [class VTHDRPerFrameMetadataGenerationSession](vthdrperframemetadatagenerationsession.md)
  An object that generates per-frame HDR metadata.
### Codec Support
- [func VTIsHardwareDecodeSupported(CMVideoCodecType) -> Bool](vtishardwaredecodesupported(_:).md)
  Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- [func VTRegisterProfessionalVideoWorkflowVideoEncoders()](vtregisterprofessionalvideoworkflowvideoencoders().md)
  Loads encoders appropriate for the client’s professional video workflows.
- [func VTRegisterProfessionalVideoWorkflowVideoDecoders()](vtregisterprofessionalvideoworkflowvideodecoders().md)
  Loads decoders appropriate for the client’s professional video workflows.
- [func VTRegisterSupplementalVideoDecoderIfAvailable(CMVideoCodecType)](vtregistersupplementalvideodecoderifavailable(_:).md)
  Registers a video decoder for the specified codec type, if one exists on the current system.
- [func VTCopySupportedPropertyDictionaryForEncoder(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, encoderIDOut: UnsafeMutablePointer<CFString?>?, supportedPropertiesOut: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus](vtcopysupportedpropertydictionaryforencoder(width:height:codectype:encoderspecification:encoderidout:supportedpropertiesout:).md)
  Builds a list of supported properties and encoder ID for an encoder.
- [func VTCopyVideoEncoderList(CFDictionary?, UnsafeMutablePointer<CFArray?>) -> OSStatus](vtcopyvideoencoderlist(_:_:).md)
  Builds a list of available video encoders.
- [Video Encoder List Keys](video-encoder-list-keys.md)
  Dictionary key constants to use to retrieve video encoder information.
### Utilities
- [func VTCreateCGImageFromCVPixelBuffer(CVPixelBuffer, options: CFDictionary?, imageOut: UnsafeMutablePointer<CGImage?>) -> OSStatus](vtcreatecgimagefromcvpixelbuffer(_:options:imageout:).md)
  Creates a Core Graphics bitmap image or image mask using the provided pixel buffer.
### Data Types
- [VTSession](vtsession-api-collection.md)
  An abstract object that provides the common interface to configure VideoToolbox session objects.
- [struct VTInt32Point](vtint32point.md)
  A structure that represents a 32-bit integer point value.
- [struct VTInt32Size](vtint32size.md)
  A structure that represents a 32-bit integer size value.
- [var VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER: Bool](vt_support_colorsync_pixel_transfer.md)
### Errors
- [Error Code Constants](1490398-error-code-constants.md)
  Constants for Video Toolbox operation error codes.
### Reference
- [VideoToolbox Reference](videotoolbox-reference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/VideoToolbox)*