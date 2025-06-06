# Encoding video for low-latency conferencing

**Framework**: Videotoolbox

Configure a compression session to optimize encoding for video-conferencing apps.

**Availability**:
- macOS 13.3+
- Xcode 14.3+

#### Overview

This sample code project demonstrates how to configure and use a `VTCompressionSession` object to encode video for low-latency conferencing.

##### Create a Compression Session

Create a `VTCompressionSession` object and specify the required dimensions and `codecType`. For low latency use, include the `kVTVideoEncoderSpecification_EnableLowLatencyRateControl` option and set it to `true` in the `videoEncoderSpecification`. Optionally, specify `sourceImageBufferAttributes` to provide a description of the source pixel buffers.

```swift
// Specify low-latency video encoding.
let videoEncoderSpecification = [kVTVideoEncoderSpecification_EnableLowLatencyRateControl: true as CFBoolean] as CFDictionary

// Specify the pixel format of the uncompressed video.
let sourceImageBufferAttributes = [kCVPixelBufferPixelFormatTypeKey: options.pixelFormat as CFNumber] as CFDictionary

var compressionSessionOut: VTCompressionSession?
let err = VTCompressionSessionCreate(allocator: kCFAllocatorDefault,
                                     width: Int32(options.destWidth),
                                     height: Int32(options.destHeight),
                                     codecType: options.codec,
                                     encoderSpecification: videoEncoderSpecification,
                                     imageBufferAttributes: sourceImageBufferAttributes,
                                     compressedDataAllocator: nil,
                                     outputCallback: nil,
                                     refcon: nil,
                                     compressionSessionOut: &compressionSessionOut)
guard err == noErr, let compressionSession = compressionSessionOut else {
    throw RuntimeError("VTCompressionSession creation failed (\(err))!")
}
```

##### Configure the Compression Session

Specify the codec profile and level, the expected video source frame rate, and the target average bit rate. Set `kVTCompressionPropertyKey_RealTime` to `kCFBooleanTrue` to indicate that this is a live encoding session. The low-latency rate control that the system enables during the `VTCompressionSession` object creation takes care of the other encoder configuration for low latency.

```swift
/// Configures a compression session for low-latency conferencing.
/// - Parameters:
///   - session: A compression session.
///   - options: The configuration options.
///   - expectedFrameRate: The expected frame rate of the video source.
private func configureVTCompressionSession(session: VTCompressionSession, options: Options, expectedFrameRate: Float) {
    // Different encoder implementations may support different property sets, so
    // the app needs to determine the implications of a failed property setting
    // on a case-by-case basis for the encoder. If the property is essential for
    // the use case and its setting fails, the app terminates. Otherwise, the
    // encoder ignores the failed setting and uses a default value to proceed
    // with encoding.

    var err: OSStatus = noErr

    // Specify the profile and level for the encoded bitstream.
    if options.codec == kCMVideoCodecType_H264 {
        err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_ProfileLevel, value: kVTProfileLevel_H264_Main_AutoLevel)
    } else if options.codec == kCMVideoCodecType_HEVC {
        err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_ProfileLevel, value: kVTProfileLevel_HEVC_Main_AutoLevel)
    }
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_ProfileLevel) failed (\(err))")
    }

    // Indicate that the compression session is real-time, which conferencing
    // requires.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_RealTime, value: kCFBooleanTrue)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_RealTime) failed (\(err))")
    }
```

##### Encode Video Frames

Call `VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:infoFlagsOut:outputHandler:)` and submit each uncompressed frame to the `VTCompressionSession` object for encoding. The object calls the `outputHandler` block for each encoded frame. Check whether a frame drop or error occurs after frame encoding.

Call `VTCompressionSessionCompleteFrames(_:untilPresentationTimeStamp:)` to indicate to the `VTCompressionSession` object that the app submitted all uncompressed video frames for encoding.

##### Perform Compression and Encoding

You can use the movie file `/Assets/video3.m4v` to test this app. Copy the file to your desktop or other working directory, and then open Terminal to that directory and run the following command, where `xxx` is a unique string that Xcode generates. Use autocomplete before the `xxx` component to complete the path for that directory.

`~/Library/Developer/Xcode/DerivedData/VTEncoderForConferencing-xxx/Build/Products/Debug/VTEncoderForConferencing-Swift video3.m4v`

Pass the `--help` option for additional configuration options.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/encoding-video-for-low-latency-conferencing)*