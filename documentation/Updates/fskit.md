# FSKit updates

**Framework**: Updates

Learn about important changes to FSKit.

#### Overview

Browse notable changes in [`FSKit`](https://developer.apple.com/documentation/fskit).

#### June 2026

- Update your [`FSVolume`](https://developer.apple.com/documentation/fskit/fsvolume) implementations to adopt [`FSVolume.Handler`](https://developer.apple.com/documentation/fskit/fsvolume/handler) and the related “handler” protocols, which replace the now-deprecated [`FSVolume.Operations`](https://developer.apple.com/documentation/fskit/fsvolume/operations) and other “operations” protocols. The “Handler” protocols provide richer [`FSVolumeHandlerResult`](https://developer.apple.com/documentation/fskit/fsvolumehandlerresult) subtypes to pass back to the framework after each call completes. Some calls also provide an [`FSContext`](https://developer.apple.com/documentation/fskit/fscontext) parameter which contains user and group identifiers. You can use these to restrict access to your filesystem to known callers.
- Improve performance with kernel data caching, by conforming to the [`FSVolume.DataCacheHandler`](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler) protocol.

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
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/fskit)*