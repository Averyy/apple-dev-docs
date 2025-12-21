# Reducing power usage when capturing media

**Framework**: Xcode

Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.

#### Overview

Device cameras draw a lot of power when they’re in use. To minimize the amount of time your app uses the device camera, run an [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) only while your app is using the captured data, and call [`stopRunning()`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/stopRunning()) at the earliest opportunity. For example, stop the capture session if your app’s camera view is covered by other content, so that the device stops capturing the camera stream when someone can’t see it.

Because capturing higher-quality images consumes more power, set the capture device’s [`activeFormat`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/activeFormat) to the format with the lowest image quality that supports your app’s features. Confirm that the [`isVideoBinned`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/Format/isVideoBinned) property is `true` for the format you use, as pixel binning also increases the power efficiency.

## See Also

- [Improving your app’s rendering efficiency](improving-your-app-s-rendering-efficiency.md)
  Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-power-usage-when-capturing-media)*