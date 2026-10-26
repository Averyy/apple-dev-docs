# kCEMarkerImageFileURLKey

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

Specifies the marker’s file URL when the marker image comes from a local file.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
var kCEMarkerImageFileURLKey: String { get }
```

```c
#define kCEMarkerImageFileURLKey
```

#### Discussion

When [`kCEMarkerKindKey`](./kcemarkerkindkey.md) is available, and both [`kCEMarkerURLKey`](./kcemarkerurlkey.md) and [`kCEMarkerImageFileURLKey`](./kcemarkerimagefileurlkey.md) are set to `nil`, the extension sets the chapter marker image to the specified frame of the source file.

If there is no image associated with a chapter marker, [`kCEMarkerImageSourceTimeKey`](./kcemarkerimagesourcetimekey.md), [`kCEMarkerImageSourceFrameNumberKey`](./kcemarkerimagesourceframenumberkey.md), [`kCEMarkerURLKey`](./kcemarkerurlkey.md), and [`kCEMarkerImageFileURLKey`](./kcemarkerimagefileurlkey.md) should be set to `nil`.

## See Also

### Encoder Attribute Keys
- [var kCEAllowsSegmentationKey: String](./kceallowssegmentationkey.md)
  Specifies whether the extension supports segmentation of the source media.
- [var kCEFileExtensionKey: String](./kcefileextensionkey.md)
  Specifies the extension of the output file.
- [var kCEFieldOrderKey: String](./kcefieldorderkey.md)
  Specifies the output scanning method.
- [var kCEColorSpaceKey: String](./kcecolorspacekey.md)
  Specifies the color space supported in the output file.
- [var kCEAudioChannelLayoutKey: String](./kceaudiochannellayoutkey.md)
  Specifies the audio channel layout for the output file.
- [var kCEVideoEnabledKey: String](./kcevideoenabledkey.md)
  Specifies whether video is enabled in the output file.
- [var kCEAudioEnabledKey: String](./kceaudioenabledkey.md)
  Specifies whether audio is enabled in the output file.
- [var kCEAudioSampleFloatKey: String](./kceaudiosamplefloatkey.md)
  Specifies whether audio samples are in floating-point value.
- [var kCEAudioSampleRateKey: String](./kceaudiosampleratekey.md)
  Specifies the sample rate of audio in the output file.
- [var kCEAudioSampleSizeKey: String](./kceaudiosamplesizekey.md)
  Specifies the number of bits per audio sample in the output file.
- [var kCEWidthKey: String](./kcewidthkey.md)
  Specifies the width of the encoded video.
- [var kCEHeightKey: String](./kceheightkey.md)
  Specifies the height of the encoded video.
- [var kCEAutoRateKey: String](./kceautoratekey.md)
  Specifies whether the frame rate is set to automatic in the encoder settings.
- [var kCEAutoWidthKey: String](./kceautowidthkey.md)
  Specifies whether the output file width is set to automatic in the encoder settings.
- [var kCEAutoHeightKey: String](./kceautoheightkey.md)
  Specifies whether the output file height is set to automatic in the encoder settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kcemarkerimagefileurlkey)*