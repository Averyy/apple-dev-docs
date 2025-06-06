# videoQuality

**Framework**: UIKit  
**Kind**: property

The video quality to use when saving a trimmed movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var videoQuality: UIImagePickerController.QualityType { get set }
```

#### Discussion

The available video qualities are described in the [`UIImagePickerController.QualityType`](uiimagepickercontroller/qualitytype.md) enumeration. The default value for this property is [`UIImagePickerController.QualityType.typeLow`](uiimagepickercontroller/qualitytype/typelow.md).

If a user attempts to reencode a movie to a higher quality, the movie is saved at its existing quality. Reencoding never increases movie dimensions, frame rate, or bit rate.

## See Also

- [var videoMaximumDuration: TimeInterval](uivideoeditorcontroller/videomaximumduration.md)
  The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.
- [var videoPath: String](uivideoeditorcontroller/videopath.md)
  The filesystem path to the movie to be loaded by the video editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/videoquality)*