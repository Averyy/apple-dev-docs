# Reducing power usage when capturing media

**Framework**: Xcode  
**Role**: Article

Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.

## Overview

Device cameras draw a lot of power when they’re in use. To minimize the amount of time your app uses the device camera, run an [`AVCaptureSession`](../AVFoundation/avcapturesession.md) only while your app is using the captured data, and call [`stopRunning()`](../AVFoundation/avcapturesession/stoprunning%28%29.md) at the earliest opportunity. For example, stop the capture session if your app’s camera view is covered by other content, so that the device stops capturing the camera stream when someone can’t see it.

Because capturing higher-quality images consumes more power, set the capture device’s [`activeFormat`](../AVFoundation/avcapturedevice/activeformat.md) to the format with the lowest image quality that supports your app’s features. Confirm that the [`isVideoBinned`](../AVFoundation/avcapturedevice/format/isvideobinned.md) property is `true` for the format you use, as pixel binning also increases the power efficiency.

## See Also

### Graphics and sound
- [Improving your app’s rendering efficiency](./improving-your-app-s-rendering-efficiency.md)
  Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-power-usage-when-capturing-media)*