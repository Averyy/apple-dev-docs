# Compression Properties

**Framework**: Videotoolbox

Properties that you use to configure a compression session.

#### Overview

> **Note**:  Video encoders may not support all compression property keys.

 Video encoders may not support all compression property keys.

## Topics

### Buffers
- [let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString](kvtcompressionpropertykey_numberofpendingframes.md)
  The number of pending frames in the compression session.
- [let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString](kvtcompressionpropertykey_pixelbufferpoolisshared.md)
  A Boolean value indicating whether the common pixel buffer pool is shared between the video encoder and the session client.
- [let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString](kvtcompressionpropertykey_videoencoderpixelbufferattributes.md)
  The video encoder’s pixel buffer attributes for the compression session.
### Frame Dependency
- [let kVTCompressionPropertyKey_AllowFrameReordering: CFString](kvtcompressionpropertykey_allowframereordering.md)
  A Boolean value that indicates whether frame reordering is enabled.
- [let kVTCompressionPropertyKey_AllowOpenGOP: CFString](kvtcompressionpropertykey_allowopengop.md)
  Enables Open GOP (Group Of Pictures) encoding.
- [let kVTCompressionPropertyKey_AllowTemporalCompression: CFString](kvtcompressionpropertykey_allowtemporalcompression.md)
  A Boolean value indicating whether temporal compression is enabled.
- [let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString](kvtcompressionpropertykey_maxkeyframeinterval.md)
  The maximum interval between key frames, also known as the key frame rate.
- [let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString](kvtcompressionpropertykey_maxkeyframeintervalduration.md)
  The maximum duration from one key frame to the next in seconds.
### Rate Control
- [let kVTCompressionPropertyKey_AverageBitRate: CFString](kvtcompressionpropertykey_averagebitrate.md)
  The long-term desired average bit rate in bits per second.
- [let kVTCompressionPropertyKey_ConstantBitRate: CFString](kvtcompressionpropertykey_constantbitrate.md)
  Requires that the encoder use a Constant Bit Rate algorithm.
- [let kVTCompressionPropertyKey_DataRateLimits: CFString](kvtcompressionpropertykey_dataratelimits.md)
  Zero, one, or two hard limits on data rate.
- [let kVTCompressionPropertyKey_EstimatedAverageBytesPerFrame: CFString](kvtcompressionpropertykey_estimatedaveragebytesperframe.md)
  An estimate of the expected size in bytes of a single encoded frame based on the current configuration.
- [let kVTCompressionPropertyKey_MoreFramesAfterEnd: CFString](kvtcompressionpropertykey_moreframesafterend.md)
  A Boolean value indicating whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_MoreFramesBeforeStart: CFString](kvtcompressionpropertykey_moreframesbeforestart.md)
  A Boolean value that indicates whether and how a compression session concatenates frames with other compressed frames to form a longer series.
- [let kVTCompressionPropertyKey_Quality: CFString](kvtcompressionpropertykey_quality.md)
  The desired compression quality.
- [let kVTCompressionPropertyKey_TargetQualityForAlpha: CFString](kvtcompressionpropertykey_targetqualityforalpha.md)
  The target quality to use for encoding the alpha channel.
### Bitstream Configuration
- [let kVTCompressionPropertyKey_PreserveAlphaChannel: CFString](kvtcompressionpropertykey_preservealphachannel.md)
  A key that specifies whether to encode the alpha channel of input video frames.
- [let kVTCompressionPropertyKey_Depth: CFString](kvtcompressionpropertykey_depth.md)
  The pixel depth of the encoded video.
- [let kVTCompressionPropertyKey_H264EntropyMode: CFString](kvtcompressionpropertykey_h264entropymode.md)
  The entropy encoding mode for H.264 compression.
- [let kVTCompressionPropertyKey_HDRMetadataInsertionMode: CFString](kvtcompressionpropertykey_hdrmetadatainsertionmode.md)
- [let kVTCompressionPropertyKey_OutputBitDepth: CFString](kvtcompressionpropertykey_outputbitdepth.md)
- [let kVTCompressionPropertyKey_ProfileLevel: CFString](kvtcompressionpropertykey_profilelevel.md)
  The profile and level for the encoded bitstream.
### Runtime Restrictions
- [let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString](kvtcompressionpropertykey_maxframedelaycount.md)
  The maximum number of frames that a compressor is allowed to hold before it must output a compressed frame.
- [let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString](kvtcompressionpropertykey_maxh264slicebytes.md)
  The maximum slice size for H.264 encoding.
- [let kVTCompressionPropertyKey_MaximizePowerEfficiency: CFString](kvtcompressionpropertykey_maximizepowerefficiency.md)
- [let kVTCompressionPropertyKey_RealTime: CFString](kvtcompressionpropertykey_realtime.md)
  A Boolean value indicating whether it’s recommended that the video encoder perform compression in real time.
### Hints
- [let kVTCompressionPropertyKey_BaseLayerBitRateFraction: CFString](kvtcompressionpropertykey_baselayerbitratefraction.md)
- [let kVTCompressionPropertyKey_BaseLayerFrameRate: CFString](kvtcompressionpropertykey_baselayerframerate.md)
- [let kVTCompressionPropertyKey_BaseLayerFrameRateFraction: CFString](kvtcompressionpropertykey_baselayerframeratefraction.md)
- [let kVTCompressionPropertyKey_ExpectedDuration: CFString](kvtcompressionpropertykey_expectedduration.md)
  The expected total duration of the compression session, if known.
- [let kVTCompressionPropertyKey_ExpectedFrameRate: CFString](kvtcompressionpropertykey_expectedframerate.md)
  The expected frame rate, if known.
- [let kVTCompressionPropertyKey_MaximumRealTimeFrameRate: CFString](kvtcompressionpropertykey_maximumrealtimeframerate.md)
  A value that specifies the maximum real time rate at which frames can be submitted to a compression session.
- [let kVTCompressionPropertyKey_PrioritizeEncodingSpeedOverQuality: CFString](kvtcompressionpropertykey_prioritizeencodingspeedoverquality.md)
  A hint for the video encoder to maximize its speed during encoding, sacrificing quality if needed.
- [let kVTCompressionPropertyKey_ReferenceBufferCount: CFString](kvtcompressionpropertykey_referencebuffercount.md)
- [let kVTCompressionPropertyKey_SourceFrameCount: CFString](kvtcompressionpropertykey_sourceframecount.md)
  The number of source frames, if known.
- [let kVTCompressionPropertyKey_CalculateMeanSquaredError: CFString](kvtcompressionpropertykey_calculatemeansquarederror.md)
- [let kVTCompressionPropertyKey_HasLeftStereoEyeView: CFString](kvtcompressionpropertykey_hasleftstereoeyeview.md)
- [let kVTCompressionPropertyKey_HasRightStereoEyeView: CFString](kvtcompressionpropertykey_hasrightstereoeyeview.md)
- [let kVTCompressionPropertyKey_HorizontalFieldOfView: CFString](kvtcompressionpropertykey_horizontalfieldofview.md)
- [let kVTSampleAttachmentKey_QualityMetrics: CFString](kvtsampleattachmentkey_qualitymetrics.md)
- [let kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError: CFString](kvtsampleattachmentqualitymetricskey_chromabluemeansquarederror.md)
- [let kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError: CFString](kvtsampleattachmentqualitymetricskey_chromaredmeansquarederror.md)
- [let kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError: CFString](kvtsampleattachmentqualitymetricskey_lumameansquarederror.md)
### Hardware Acceleration
- [let kVTCompressionPropertyKey_SupportsBaseFrameQP: CFString](kvtcompressionpropertykey_supportsbaseframeqp.md)
  A value that indicates whether the encoder supports base frame QP requests.
- [let kVTCompressionPropertyKey_UsingGPURegistryID: CFString](kvtcompressionpropertykey_usinggpuregistryid.md)
- [let kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder: CFString](kvtcompressionpropertykey_usinghardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether a hardware-accelerated video encoder is used.
- [let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated video encoding is allowed, if available.
- [let kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_preferredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated encoding is required.
- [let kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_requiredencodergpuregistryid.md)
### Per-Frame Configuration
- [let kVTEncodeFrameOptionKey_BaseFrameQP: CFString](kvtencodeframeoptionkey_baseframeqp.md)
- [let kVTEncodeFrameOptionKey_ForceKeyFrame: CFString](kvtencodeframeoptionkey_forcekeyframe.md)
  Boolean value indicating whether the current frame is forced to be a key frame.
### Clean Aperture and Pixel Aspect Ratio
- [let kVTCompressionPropertyKey_AspectRatio16x9: CFString](kvtcompressionpropertykey_aspectratio16x9.md)
  A Boolean value indicating whether the DV video stream should have the 16x9 flag set.
- [let kVTCompressionPropertyKey_CleanAperture: CFString](kvtcompressionpropertykey_cleanaperture.md)
  The clean aperture for encoded frames.
- [let kVTCompressionPropertyKey_FieldCount: CFString](kvtcompressionpropertykey_fieldcount.md)
  The field count indicating whether the frames should be encoded progressive (1) or interlaced (2).
- [let kVTCompressionPropertyKey_FieldDetail: CFString](kvtcompressionpropertykey_fielddetail.md)
  Field ordering for encoded interlaced frames.
- [let kVTCompressionPropertyKey_PixelAspectRatio: CFString](kvtcompressionpropertykey_pixelaspectratio.md)
  The pixel aspect ratio for encoded frames.
- [let kVTCompressionPropertyKey_ProgressiveScan: CFString](kvtcompressionpropertykey_progressivescan.md)
  A Boolean value indicating whether the DV video stream should have the progressive flag set.
### Color
- [let kVTCompressionPropertyKey_AlphaChannelMode: CFString](kvtcompressionpropertykey_alphachannelmode.md)
- [let kVTCompressionPropertyKey_ColorPrimaries: CFString](kvtcompressionpropertykey_colorprimaries.md)
  The color primaries for compressed content.
- [let kVTCompressionPropertyKey_ContentLightLevelInfo: CFString](kvtcompressionpropertykey_contentlightlevelinfo.md)
- [let kVTCompressionPropertyKey_GammaLevel: CFString](kvtcompressionpropertykey_gammalevel.md)
- [let kVTCompressionPropertyKey_ICCProfile: CFString](kvtcompressionpropertykey_iccprofile.md)
  The ICC profile for compressed content.
- [let kVTCompressionPropertyKey_MasteringDisplayColorVolume: CFString](kvtcompressionpropertykey_masteringdisplaycolorvolume.md)
- [let kVTCompressionPropertyKey_TransferFunction: CFString](kvtcompressionpropertykey_transferfunction.md)
  The transfer function for compressed content.
- [let kVTCompressionPropertyKey_YCbCrMatrix: CFString](kvtcompressionpropertykey_ycbcrmatrix.md)
  The YCbCr matrix for compressed content.
### Precompression Processing
- [let kVTCompressionPropertyKey_PixelTransferProperties: CFString](kvtcompressionpropertykey_pixeltransferproperties.md)
  Properties for configuring a pixel transfer session.
### Multipass Storage
- [let kVTCompressionPropertyKey_MultiPassStorage: CFString](kvtcompressionpropertykey_multipassstorage.md)
  A property key that enables multipass compression and provides storage for encoder private data.
### Encoder Information
- [let kVTVideoEncoderSpecification_EncoderID: CFString](kvtvideoencoderspecification_encoderid.md)
  A key that indicates a particular video encoder to use.
- [let kVTCompressionPropertyKey_RecommendedParallelizationLimit: CFString](kvtcompressionpropertykey_recommendedparallelizationlimit.md)
  The recommended number of compression sessions to instantiate in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration: CFString](kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumduration.md)
  The recommended minimum duration for a given subdivision in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumFrameCount: CFString](kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumframecount.md)
  The recommended minimum number of video frames for a given subdivision in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_EnableLTR: CFString](kvtcompressionpropertykey_enableltr.md)
  Enables Long Term Reference (LTR) frames during encoding.
- [let kVTCompressionPropertyKey_EncoderID: CFString](kvtcompressionpropertykey_encoderid.md)
  Specifies a particular video encoder by its ID string.
- [let kVTCompressionPropertyKey_MinAllowedFrameQP: CFString](kvtcompressionpropertykey_minallowedframeqp.md)
  The minimum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_MaxAllowedFrameQP: CFString](kvtcompressionpropertykey_maxallowedframeqp.md)
  The maximum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_PreserveDynamicHDRMetadata: CFString](kvtcompressionpropertykey_preservedynamichdrmetadata.md)
  Specifies whether to preserve dynamic HDR metadata on the input pixel buffer.
- [let kVTEncodeFrameOptionKey_AcknowledgedLTRTokens: CFString](kvtencodeframeoptionkey_acknowledgedltrtokens.md)
  Enable Long Term Reference (LTR) frames during encoding.
- [let kVTEncodeFrameOptionKey_ForceLTRRefresh: CFString](kvtencodeframeoptionkey_forceltrrefresh.md)
  A Boolean value that indicates whether to force Long Term Reference (LTR).
- [let kVTSampleAttachmentKey_RequireLTRAcknowledgementToken: CFString](kvtsampleattachmentkey_requireltracknowledgementtoken.md)
  A number value that contains a unique token for this Long Term Reference (LTR).
- [let kVTVideoEncoderSpecification_EnableLowLatencyRateControl: CFString](kvtvideoencoderspecification_enablelowlatencyratecontrol.md)
  Specifies to select an encoder that supports low-latency operation and enables low-latency mode.
- [let kVTCompressionPropertyKey_SpatialAdaptiveQPLevel: CFString](kvtcompressionpropertykey_spatialadaptiveqplevel.md)
  A value that controls spatial adaptation of the quantization parameter (QP) based on per-frame statistics.
- [let kVTCompressionPropertyKey_SuggestedLookAheadFrameCount: CFString](kvtcompressionpropertykey_suggestedlookaheadframecount.md)
  A value that requests that the encoder retain the specified number of frames during encoding.
### Video Extended Usage (VEXU) Signaling
- [let kVTCompressionPropertyKey_HeroEye: CFString](kvtcompressionpropertykey_heroeye.md)
  A value that indicates which eye is the primary eye when rendering in 2D.
- [let kVTCompressionPropertyKey_StereoCameraBaseline: CFString](kvtcompressionpropertykey_stereocamerabaseline.md)
  A value that specifies the distance between centers of the lenses of the camera system.
- [let kVTCompressionPropertyKey_HorizontalDisparityAdjustment: CFString](kvtcompressionpropertykey_horizontaldisparityadjustment.md)
  A value that indicates a relative shift of the left and right images, which changes the zero parallax plane.
- [let kVTCompressionPropertyKey_ProjectionKind: CFString](kvtcompressionpropertykey_projectionkind.md)
  A value that indicates the projection kind.
- [let kVTCompressionPropertyKey_ViewPackingKind: CFString](kvtcompressionpropertykey_viewpackingkind.md)
  A value that indicates the view packing kind.
### Multiview compression
- [let kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: CFString](kvtcompressionpropertykey_mvhevcvideolayerids.md)
  The identifiers of the video layers to encode in a multiview encoding operation.
- [let kVTCompressionPropertyKey_MVHEVCViewIDs: CFString](kvtcompressionpropertykey_mvhevcviewids.md)
  The identifiers of the views corresponding to the video layers in a multiview encoding operation.
- [let kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: CFString](kvtcompressionpropertykey_mvhevcleftandrightviewids.md)
  Specifies which view identifier corresponds to the left eye and right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/compression-properties)*