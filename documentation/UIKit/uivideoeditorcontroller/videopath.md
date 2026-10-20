# videoPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The filesystem path to the movie to be loaded by the video editor.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var videoPath: String { get set }
```

```objc
@property (nonatomic, copy) NSString * videoPath;
```

## See Also

### Configuring the editor
- [var videoMaximumDuration: TimeInterval](./videomaximumduration.md)
  The maximum duration, in seconds, permitted for trimmed movies saved by the video editor.
- [var videoQuality: UIImagePickerController.QualityType](./videoquality.md)
  The video quality to use when saving a trimmed movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/videopath)*