# AVFoundation updates

**Framework**: Updates

Learn about important changes to AVFoundation.

#### Overview

Browse notable changes in [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation).

#### June 2024

##### Assets

- Preserve HDR data when generating images with `AVAssetImageGenerator` by setting the value of its [`dynamicRangePolicy`](https://developer.apple.com/documentation/AVFoundation/AVAssetImageGenerator/dynamicRangePolicy-swift.property) property to match the source video.
- Export media asynchronously using the [`export(to:as:isolation:)`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession/export(to:as:isolation:)) method of [`AVAssetExportSession`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession). You can monitor the progress of an export by calling the [`states(updateInterval:)`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession/states(updateInterval:)) method and awaiting its results.
- Determine whether an [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset) decodes its data using a Media Extension by inspecting its [`mediaExtensionProperties`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset/mediaExtensionProperties) property.

##### Camera

- Show your camera app on the Lock Screen by adopting the  [`LockedCameraCapture`](https://developer.apple.com/documentation/LockedCameraCapture) framework.
- Capture photos in constant color by configuring a photo output’s [`isConstantColorEnabled`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhotoOutput/isConstantColorEnabled) property.
- Continue background audio playback while performing audio and video capture by enabling a capture session’s [`configuresApplicationAudioSessionToMixWithOthers`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/configuresApplicationAudioSessionToMixWithOthers) property.
- Pause and resume video recording in iOS when using [`AVCaptureFileOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureFileOutput).
- Support enhanced video stabilization using [`AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoStabilizationMode/cinematicExtendedEnhanced).
- Configure a capture device to automatically adjust its frame rate based on lighting conditions by enabling its [`isAutoVideoFrameRateEnabled`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/isAutoVideoFrameRateEnabled) property.
- Configure a capture device to replace background content in macOS by enabling its [`isBackgroundReplacementEnabled`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/isBackgroundReplacementEnabled) property.

##### Playback

- Build playback apps using the latest Swift Concurrency features due to enhanced [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable) adoption throughout the playback APIs.
- Capture performance and playback metrics using [`AVMetrics`](https://developer.apple.com/documentation/AVFoundation/AVMetrics).
- Receive rendered captions for the currently playing media using [`AVPlayerItemRenderedLegibleOutput`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItemRenderedLegibleOutput).
- Simplify handling of interstitial content by using [`AVPlayerItemIntegratedTimeline`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItemIntegratedTimeline).
- Send Common Media Client Data (CMCD) as HTTP headers by enabling the new [`sendsCommonMediaClientDataAsHTTPHeaders`](https://developer.apple.com/documentation/AVFoundation/AVAssetResourceLoader/sendsCommonMediaClientDataAsHTTPHeaders) property on [`AVAssetResourceLoader`](https://developer.apple.com/documentation/AVFoundation/AVAssetResourceLoader).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [Background Tasks updates](backgroundtasks.md)
  Learn about important changes in Background Tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avfoundation)*