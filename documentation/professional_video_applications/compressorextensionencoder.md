# CompressorExtensionEncoder

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An interface an extension implements to convert source media to the output format supported in your extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
protocol CompressorExtensionEncoder
```

```objc
@protocol CompressorExtensionEncoder
```

## Overview

Implement the methods in this interface to run an encoding job, support parallel processing, and send output files to a specified destination. To run an encoding job, the Compressor app calls the [`runTranscode(for:start:duration:toFile:startTimeCode:)`](./compressorextensionencoder/runtranscode%28for,start,duration,tofile,starttimecode%29.md) method. During the encoding process, the Compressor app calls the methods in the `CompressorExtensionEncoder` protocol to get updates on the status and progress of an encoding job.

Users sometimes request to pause a running encoder task to free up resources. You can choose to support resuming a job where it left off by saving the extension’s state while pausing in the implementation of the [`cancel(forPause:)`](./compressorextensionencoder/cancel%28forpause%29.md) method.

Increase the encoding speed in your extension by taking advantage of distributed processing, where multiple extension instances process segments of source media concurrently. Determine individual segments of the source media to process in extension instances by implementing the [`splitPoints(forFrameStart:duration:serviceCount:)`](./compressorextensionencoder/splitpoints%28forframestart,duration,servicecount%29.md) method. To combine the individual encoded segments into a single output file, implement the [`mergeSegments(_:andAudio:toFile:)`](./compressorextensionencoder/mergesegments%28_,andaudio,tofile%29.md) method.

## Topics

### Determining the Source Media Segments
- [func splitPoints(forFrameStart: Int64, duration: Int64, serviceCount: Int32) -> [Any]!](./compressorextensionencoder/splitpoints%28forframestart,duration,servicecount%29.md)
  Determines the source media segments based on the number of available encoder services.
### Encoding and Merging Segments
- [func runTranscode(for: CompressorMediaDecoderPtr!, start: Int64, duration: Int64, toFile: URL!, startTimeCode: [AnyHashable : Any]!)](./compressorextensionencoder/runtranscode%28for,start,duration,tofile,starttimecode%29.md)
  Encodes the source media files to an output format based on the encoder settings.
- [func mergeSegments([Any]!, andAudio: URL!, toFile: URL!)](./compressorextensionencoder/mergesegments%28_,andaudio,tofile%29.md)
  Merges multiple encoded video segments with an encoded audio segment.
- [typealias CompressorExtensionEncoderPtr](./compressorextensionencoderptr.md)
  The type alias to use for referencing the `CompressorExtensionEncoder` object.
### Providing Updates of the Encoding Process
- [func statusMessage() -> String!](./compressorextensionencoder/statusmessage%28%29.md)
  Returns the status of an encoding job.
- [func percentDone() -> Double](./compressorextensionencoder/percentdone%28%29.md)
  Returns the completion percentage of an encoding job.
### Canceling or Pausing the Encoding Process
- [func cancel(forPause: Bool) -> [AnyHashable : Any]!](./compressorextensionencoder/cancel%28forpause%29.md)
  Pauses or cancels an encoding job.
- [func setStateFromPause([AnyHashable : Any]!)](./compressorextensionencoder/setstatefrompause%28_%29.md)
  Sets the extension to a previously saved state.
- [func percentLostOnPause() -> Double](./compressorextensionencoder/percentlostonpause%28%29.md)
  Returns the percentage of the encoding job lost on pausing.
### Setting Encoding Values
- [func setSettings(CompressorExtensionSettingsPtr!)](./compressorextensionencoder/setsettings%28_%29.md)
  Sets the current encoding settings based on the given setting values.
- [func setAnnotations([AnyHashable : Any]!)](./compressorextensionencoder/setannotations%28_%29.md)
  Adds annotations to an encoded media file.
- [func setChapters([[AnyHashable : Any]]!)](./compressorextensionencoder/setchapters%28_%29.md)
  Sets chapter markers of an encoded file from the contents of the input dictionary.
### Supporting Pixel Formats
- [var supportedPixelFormats: [NSNumber]!](./compressorextensionencoder/supportedpixelformats.md)
  The supported pixel formats in an encoder extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder)*