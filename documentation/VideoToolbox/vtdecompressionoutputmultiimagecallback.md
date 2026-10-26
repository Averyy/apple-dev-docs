# VTDecompressionOutputMultiImageCallback

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A callback that the system invokes when multi-image frame decompression completes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias VTDecompressionOutputMultiImageCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, OSStatus, VTDecodeInfoFlags, __CMTaggedBufferGroup?, CMTime, CMTime) -> Void
```

```c
typedef void (*)(void *, void *, int, enum VTDecodeInfoFlags, struct OpaqueCMTaggedBufferGroup *, CMTime, CMTime) VTDecompressionOutputMultiImageCallback;
```

#### Discussion

The system doesn’t guarantee that it calls this function in display order.

> ❗ **Important**:  The video decompressor may still reference the pixel buffers returned in this callback if the [`imageBufferModifiable`](./vtdecodeinfoflags/imagebuffermodifiable.md) flag isn’t set. It’s not safe to modify the image buffer in this state.

## Parameters

- `decompressionOutputMultiImageRefCon`: The callback’s reference value, copied from the `outputMultiImageRefcon` argument passed to [`VTDecompressionSessionSetMultiImageCallback`](./vtdecompressionsessionsetmultiimagecallback.md).
- `sourceFrameRefCon`: The frame’s reference value, copied from the `sourceFrameRefCon` argument passed to [`VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:frameRefcon:infoFlagsOut:)`](./vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,framerefcon,infoflagsout%29.md).
- `status`: A value of `noErr` if decompression succeeds or an error code if decompression fails.
- `infoFlags`: Contains information about the decode operation:

  - An [`asynchronous`](./vtdecodeinfoflags/asynchronous.md) flag indicates the decode ran asynchronously.
  - A [`frameDropped`](./vtdecodeinfoflags/framedropped.md) flag indicates the session dropped a frame.
  - An [`imageBufferModifiable`](./vtdecodeinfoflags/imagebuffermodifiable.md) flag indicates that you can safely modify the image buffer.
- `taggedBufferGroup`: Contains the decompressed frame’s multiple images, if decompression was successful; otherwise, `NULL`.
- `presentationTimeStamp`: The frame’s presentation timestamp, which the system determines by calling [`CMSampleBufferGetOutputPresentationTimeStamp(_:)`](../CoreMedia/cmsamplebuffergetoutputpresentationtimestamp%28_%29.md); otherwise, [`invalid`](../CoreMedia/cmtime/invalid.md) if the timestamp isn’t available.
- `presentationDuration`: The frame’s presentation duration, which the system determines by calling [`CMSampleBufferGetOutputDuration(_:)`](../CoreMedia/cmsamplebuffergetoutputduration%28_%29.md); otherwise, [`invalid`](../CoreMedia/cmtime/invalid.md) if the duration isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputmultiimagecallback)*