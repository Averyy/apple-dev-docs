# Encoding video for live streaming

**Framework**: Videotoolbox

Configure a compression session to encode video for live streaming.

**Availability**:
- macOS 13.3+
- Xcode 14.3+

#### Overview

This sample code project demonstrates how to configure and use a `VTCompressionSession` object to encode video for live streaming.

##### Create a Compression Session

Create a `VTCompressionSession` object and specify the required dimensions and `codecType`. Optionally, specify `sourceImageBufferAttributes` to provide a description of the source pixel buffers.

```swift
// Specify the pixel format of the uncompressed video.
let sourceImageBufferAttributes = [kCVPixelBufferPixelFormatTypeKey: options.pixelFormat as CFNumber] as CFDictionary

var compressionSessionOut: VTCompressionSession?
let err = VTCompressionSessionCreate(allocator: kCFAllocatorDefault,
                                     width: Int32(options.destWidth),
                                     height: Int32(options.destHeight),
                                     codecType: options.codec,
                                     encoderSpecification: nil,
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

Specify the codec profile and level, the expected video source frame rate, and the maximum interval between key frames. Specify the target average bit rate and the data rate limits or the target constant bit rate. Enable temporal compression and frame reordering. Set `kVTCompressionPropertyKey_RealTime` to `kCFBooleanTrue` to indicate this is a live encoding session.

```swift
/// Configures a compression session for live streaming.
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

    // Indicate that the compression session is in real time, which streaming
    // requires.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_RealTime, value: kCFBooleanTrue)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_RealTime) failed (\(err))")
    }

    // Indicate the expected frame rate, if known. This is just a hint for rate
    // control purposes; the actual encoding frame rate matches the incoming
    // frame rate even if it doesn't match this setting. When
    // `kVTCompressionPropertyKey_RealTime` is `kCFBooleanTrue`, the video
    // encoder may optimize energy usage.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_ExpectedFrameRate, value: expectedFrameRate as CFNumber)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_ExpectedFrameRate) failed (\(err))")
    }

    if  options.cbr {
        // This is intended for legacy content distribution networks that
        // require constant bitrate, not for general streaming scenarios. The
        // encoder pads the frames if they are smaller than necessary based on
        // the constant bit rate.
        err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_ConstantBitRate, value: options.destBitRate as CFNumber)
        if noErr != err {
            print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_ConstantBitRate) failed (\(err))")
        }
    } else {
        // Specify the long-term desired average bit rate in bits per second. It's a
        // soft limit, so the encoder may overshoot or undershoot and the average
        // bit rate of the output video may be over or under the target.
        err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_AverageBitRate, value: options.destBitRate as CFNumber)
        if noErr != err {
            print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_AverageBitRate) failed (\(err))")
        }

        // Specify a hard data-rate cap for a given time window, which the
        // encoder won't overshoot. Use `kVTCompressionPropertyKey_AverageBitRate`
        // and `kVTCompressionPropertyKey_DataRateLimits` together to specify an
        // overall target bit rate and hard limits over a smaller window.
        let byteLimit = (Double(options.destBitRate) / 8 * 1.5) as CFNumber
        let secLimit = Double(1.0) as CFNumber
        let limitsArray = [ byteLimit, secLimit ] as CFArray
        err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_DataRateLimits, value: limitsArray)
        if noErr != err {
            print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_DataRateLimits) failed (\(err))")
        }
    }

    // Enables temporal compression.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_AllowTemporalCompression, value: kCFBooleanTrue)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_AllowTemporalCompression) failed (\(err))")
    }

    // Enables frame reordering.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_AllowFrameReordering, value: kCFBooleanTrue)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_AllowFrameReordering) failed (\(err))")
    }

    // Specify the maximum interval between key frames, also known as the key
    // frame rate. Set this in conjunction with
    // `kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration` to enforce both
    // limits, which requires a keyframe every X frames or every Y seconds,
    // whichever comes first.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_MaxKeyFrameInterval, value: options.maxKeyFrameInterval as CFNumber)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_MaxKeyFrameInterval) failed (\(err))")
    }

    // Specify the maximum duration from one key frame to the next in seconds.
    err = VTSessionSetProperty(session, key: kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration,
                               value: options.maxKeyFrameIntervalDuration as CFNumber)
    if noErr != err {
        print("Warning: VTSessionSetProperty(kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration) failed (\(err))")
    }
}
```

##### Encode Video Frames

Call `VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:infoFlagsOut:outputHandler:)` and submit each uncompressed frame to the `VTCompressionSession` object for encoding. The object calls the `outputHandler` block for each encoded frame. Check whether a frame drop or error occurs after frame encoding.

Call `VTCompressionSessionCompleteFrames(_:untilPresentationTimeStamp:)` to indicate to the `VTCompressionSession` object that the app submitted all uncompressed video frames for encoding.

##### Perform Compression and Encoding

You can use the movie file `/Assets/video3.m4v` to test this app. Copy the file to your desktop or other working directory, and then open Terminal to that directory and run the following command, where `xxx` is a unique string that Xcode generates. Use autocomplete before the `xxx` component to complete the path for that directory.

`~/Library/Developer/Xcode/DerivedData/VTEncoderForStreaming-xxx/Build/Products/Debug/VTEncoderForStreaming-Swift video3.m4v`

Pass the `--help` option for additional configuration options.

## See Also

- [Encoding video for low-latency conferencing](encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/encoding-video-for-live-streaming)*