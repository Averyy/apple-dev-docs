# AVFoundation updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to AVFoundation.

#### Overview

Browse notable changes in [AVFoundation](../AVFoundation/AVFoundation.md).

#### June 2024

##### Assets

- Preserve HDR data when generating images with `AVAssetImageGenerator` by setting the value of its [`dynamicRangePolicy`](../AVFoundation/avassetimagegenerator/dynamicrangepolicy-swift.property.md) property to match the source video.
- Export media asynchronously using the [`export(to:as:isolation:)`](../AVFoundation/avassetexportsession/export%28to,as,isolation%29.md) method of [`AVAssetExportSession`](../AVFoundation/avassetexportsession.md). You can monitor the progress of an export by calling the [`states(updateInterval:)`](../AVFoundation/avassetexportsession/states%28updateinterval%29.md) method and awaiting its results.
- Determine whether an [`AVURLAsset`](../AVFoundation/avurlasset.md) decodes its data using a Media Extension by inspecting its [`mediaExtensionProperties`](../AVFoundation/avurlasset/mediaextensionproperties.md) property.

##### Camera

- Show your camera app on the Lock Screen by adopting the  [LockedCameraCapture](../LockedCameraCapture/LockedCameraCapture.md) framework.
- Capture photos in constant color by configuring a photo output’s [`isConstantColorEnabled`](../AVFoundation/avcapturephotooutput/isconstantcolorenabled.md) property.
- Continue background audio playback while performing audio and video capture by enabling a capture session’s [`configuresApplicationAudioSessionToMixWithOthers`](../AVFoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers.md) property.
- Pause and resume video recording in iOS when using [`AVCaptureFileOutput`](../AVFoundation/avcapturefileoutput.md).
- Support enhanced video stabilization using [`AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced`](../AVFoundation/avcapturevideostabilizationmode/cinematicextendedenhanced.md).
- Configure a capture device to automatically adjust its frame rate based on lighting conditions by enabling its [`isAutoVideoFrameRateEnabled`](../AVFoundation/avcapturedevice/isautovideoframerateenabled.md) property.
- Configure a capture device to replace background content in macOS by enabling its [`isBackgroundReplacementEnabled`](../AVFoundation/avcapturedevice/isbackgroundreplacementenabled.md) property.

##### Playback

- Build playback apps using the latest Swift Concurrency features due to enhanced [`Sendable`](../Swift/sendable.md) adoption throughout the playback APIs.
- Capture performance and playback metrics using [`AVMetrics`](../AVFoundation/avmetrics.md).
- Receive rendered captions for the currently playing media using [`AVPlayerItemRenderedLegibleOutput`](../AVFoundation/avplayeritemrenderedlegibleoutput.md).
- Simplify handling of interstitial content by using [`AVPlayerItemIntegratedTimeline`](../AVFoundation/avplayeritemintegratedtimeline.md).
- Send Common Media Client Data (CMCD) as HTTP headers by enabling the new [`sendsCommonMediaClientDataAsHTTPHeaders`](../AVFoundation/avassetresourceloader/sendscommonmediaclientdataashttpheaders.md) property on [`AVAssetResourceLoader`](../AVFoundation/avassetresourceloader.md).

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avfoundation)*