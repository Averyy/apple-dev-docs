# kCEColorSpaceKey

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

Specifies the color space supported in the output file.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
var kCEColorSpaceKey: String { get }
```

```c
#define kCEColorSpaceKey
```

#### Discussion

The value can be one of the integers representing a color space from [`eCEColorSpace`](./ececolorspace.md). If you don’t provide this key, the output file uses the same color space as the source file.

## See Also

### Encoder Attribute Keys
- [var kCEAllowsSegmentationKey: String](./kceallowssegmentationkey.md)
  Specifies whether the extension supports segmentation of the source media.
- [var kCEFileExtensionKey: String](./kcefileextensionkey.md)
  Specifies the extension of the output file.
- [var kCEFieldOrderKey: String](./kcefieldorderkey.md)
  Specifies the output scanning method.
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
- [var kCEPixelAspectKey: String](./kcepixelaspectkey.md)
  Specifies the aspect ratio of the output frame pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kcecolorspacekey)*