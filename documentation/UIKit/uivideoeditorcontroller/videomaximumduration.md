# videoMaximumDuration

**Framework**: UIKit  
**Kind**: property

The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var videoMaximumDuration: TimeInterval { get set }
```

#### Discussion

The system-enforced maximum duration for a video recording is 10 minutes; you can set this value to 10 minutes or less. The default value for this property is also 10 minutes.

The video editor user interface forces the user to trim a loaded movie to fit within this property’s value prior to saving.

## See Also

- [var videoPath: String](uivideoeditorcontroller/videopath.md)
  The filesystem path to the movie to be loaded by the video editor.
- [var videoQuality: UIImagePickerController.QualityType](uivideoeditorcontroller/videoquality.md)
  The video quality to use when saving a trimmed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/videomaximumduration)*