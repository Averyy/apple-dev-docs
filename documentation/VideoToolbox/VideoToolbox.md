# Video Toolbox

**Framework**: Video Toolbox  
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
  An interface for accessing a range of different video-processing features.
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
### Classes
- [class VTLowLatencyFrameInterpolationConfiguration](vtlowlatencyframeinterpolationconfiguration.md)
  Configuration that you use to program Video Toolbox frame processor for low-latency frame interpolation.
- [class VTLowLatencyFrameInterpolationParameters](vtlowlatencyframeinterpolationparameters.md)
  An object that contains both input and output parameters that the low-latency frame interpolation processor needs.
- [class VTLowLatencySuperResolutionScalerConfiguration](vtlowlatencysuperresolutionscalerconfiguration.md)
  An object you use to configure frame processor for low-latency super-resolution scaler processing.
- [class VTLowLatencySuperResolutionScalerParameters](vtlowlatencysuperresolutionscalerparameters.md)
  An object that contains both input and output parameters that the low-latency super-resolution scaler frame processor needs.
- [class VTMotionEstimationSession](vtmotionestimationsession.md)
- [class VTSuperResolutionScalerConfiguration](vtsuperresolutionscalerconfiguration.md)
  Configuration that you use to set up the super-resolution processor.
- [class VTSuperResolutionScalerParameters](vtsuperresolutionscalerparameters.md)
  An object that contains both input and output parameters that the super-resolution processor needs to run on a frame.
- [class VTTemporalNoiseFilterConfiguration](vttemporalnoisefilterconfiguration.md)
  A configuration object to initiate a frame processor and use temporal noise-filter processor.
- [class VTTemporalNoiseFilterParameters](vttemporalnoisefilterparameters.md)
  Encapsulates the frame-level parameters necessary for processing a source frame using temporal noise-filter processor.
### Variables
- [let kVTCameraCalibrationExtrinsicOriginSource_StereoCameraSystemBaseline: CFString](kvtcameracalibrationextrinsicoriginsource_stereocamerasystembaseline.md)
- [let kVTCameraCalibrationLensAlgorithmKind_ParametricLens: CFString](kvtcameracalibrationlensalgorithmkind_parametriclens.md)
- [let kVTCameraCalibrationLensDomain_Color: CFString](kvtcameracalibrationlensdomain_color.md)
- [let kVTCameraCalibrationLensRole_Left: CFString](kvtcameracalibrationlensrole_left.md)
- [let kVTCameraCalibrationLensRole_Mono: CFString](kvtcameracalibrationlensrole_mono.md)
- [let kVTCameraCalibrationLensRole_Right: CFString](kvtcameracalibrationlensrole_right.md)
- [let kVTCompressionPreset_Balanced: CFString](kvtcompressionpreset_balanced.md)
- [let kVTCompressionPreset_HighQuality: CFString](kvtcompressionpreset_highquality.md)
- [let kVTCompressionPreset_HighSpeed: CFString](kvtcompressionpreset_highspeed.md)
- [let kVTCompressionPreset_VideoConferencing: CFString](kvtcompressionpreset_videoconferencing.md)
- [let kVTCompressionPropertyCameraCalibrationKey_ExtrinsicOrientationQuaternion: CFString](kvtcompressionpropertycameracalibrationkey_extrinsicorientationquaternion.md)
- [let kVTCompressionPropertyCameraCalibrationKey_ExtrinsicOriginSource: CFString](kvtcompressionpropertycameracalibrationkey_extrinsicoriginsource.md)
- [let kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrix: CFString](kvtcompressionpropertycameracalibrationkey_intrinsicmatrix.md)
- [let kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixProjectionOffset: CFString](kvtcompressionpropertycameracalibrationkey_intrinsicmatrixprojectionoffset.md)
- [let kVTCompressionPropertyCameraCalibrationKey_IntrinsicMatrixReferenceDimensions: CFString](kvtcompressionpropertycameracalibrationkey_intrinsicmatrixreferencedimensions.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind: CFString](kvtcompressionpropertycameracalibrationkey_lensalgorithmkind.md)
  The following keys are required in each kVTCompressionPropertyKey_CameraCalibrationDataLensCollection dictionary.
- [let kVTCompressionPropertyCameraCalibrationKey_LensDistortions: CFString](kvtcompressionpropertycameracalibrationkey_lensdistortions.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensDomain: CFString](kvtcompressionpropertycameracalibrationkey_lensdomain.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensFrameAdjustmentsPolynomialX: CFString](kvtcompressionpropertycameracalibrationkey_lensframeadjustmentspolynomialx.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensFrameAdjustmentsPolynomialY: CFString](kvtcompressionpropertycameracalibrationkey_lensframeadjustmentspolynomialy.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensIdentifier: CFString](kvtcompressionpropertycameracalibrationkey_lensidentifier.md)
- [let kVTCompressionPropertyCameraCalibrationKey_LensRole: CFString](kvtcompressionpropertycameracalibrationkey_lensrole.md)
- [let kVTCompressionPropertyCameraCalibrationKey_RadialAngleLimit: CFString](kvtcompressionpropertycameracalibrationkey_radialanglelimit.md)
- [let kVTCompressionPropertyKey_CameraCalibrationDataLensCollection: CFString](kvtcompressionpropertykey_cameracalibrationdatalenscollection.md)
- [let kVTCompressionPropertyKey_SupportedPresetDictionaries: CFString](kvtcompressionpropertykey_supportedpresetdictionaries.md)
- [let kVTCompressionPropertyKey_VBVBufferDuration: CFString](kvtcompressionpropertykey_vbvbufferduration.md)
- [let kVTCompressionPropertyKey_VBVInitialDelayPercentage: CFString](kvtcompressionpropertykey_vbvinitialdelaypercentage.md)
- [let kVTCompressionPropertyKey_VBVMaxBitRate: CFString](kvtcompressionpropertykey_vbvmaxbitrate.md)
- [let kVTCompressionPropertyKey_VariableBitRate: CFString](kvtcompressionpropertykey_variablebitrate.md)
- [let kVTDecodeFrameOptionKey_ContentAnalyzerCropRectangle: CFString](kvtdecodeframeoptionkey_contentanalyzercroprectangle.md)
- [let kVTDecodeFrameOptionKey_ContentAnalyzerRotation: CFString](kvtdecodeframeoptionkey_contentanalyzerrotation.md)
- [let kVTHDRMetadataInsertionMode_RequestSDRRangePreservation: CFString](kvthdrmetadatainsertionmode_requestsdrrangepreservation.md)
- [let kVTHeroEye_Left: CFString](kvtheroeye_left.md)
- [let kVTHeroEye_Right: CFString](kvtheroeye_right.md)
- [let kVTMotionEstimationSessionCreationOption_Label: CFString!](kvtmotionestimationsessioncreationoption_label.md)
  A label you use to log and track resources.
- [let kVTMotionEstimationSessionCreationOption_MotionVectorSize: CFString!](kvtmotionestimationsessioncreationoption_motionvectorsize.md)
  The size of the search blocks that motion estimation session uses.
- [let kVTMotionEstimationSessionCreationOption_UseMultiPassSearch: CFString!](kvtmotionestimationsessioncreationoption_usemultipasssearch.md)
  An option to use for higher quality motion estimation.
- [let kVTProjectionKind_Equirectangular: CFString](kvtprojectionkind_equirectangular.md)
- [let kVTProjectionKind_HalfEquirectangular: CFString](kvtprojectionkind_halfequirectangular.md)
- [let kVTProjectionKind_ParametricImmersive: CFString](kvtprojectionkind_parametricimmersive.md)
- [let kVTProjectionKind_Rectilinear: CFString](kvtprojectionkind_rectilinear.md)
- [let kVTRAWProcessingPropertyKey_MetadataForSidecarFile: CFString!](kvtrawprocessingpropertykey_metadataforsidecarfile.md)
- [var kVTVideoEncoderAutoWhiteBalanceNotLockedErr: OSStatus](kvtvideoencoderautowhitebalancenotlockederr.md)
- [let kVTViewPackingKind_OverUnder: CFString](kvtviewpackingkind_overunder.md)
- [let kVTViewPackingKind_SideBySide: CFString](kvtviewpackingkind_sidebyside.md)
### Functions
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, frameRefcon: UnsafeMutableRawPointer?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:frameoptions:framerefcon:infoflagsout:).md)
- [func VTDecompressionSessionDecodeFrame(VTDecompressionSession, sampleBuffer: CMSampleBuffer, flags: VTDecodeFrameFlags, frameOptions: CFDictionary?, infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>?, outputHandler: VTDecompressionOutputHandler) -> OSStatus](vtdecompressionsessiondecodeframe(_:samplebuffer:flags:frameoptions:infoflagsout:outputhandler:).md)
### Type Aliases
- [typealias VTMotionEstimationOutputHandler](vtmotionestimationoutputhandler.md)
  A block invoked by motion-estimation session when frame processing is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/VideoToolbox)*