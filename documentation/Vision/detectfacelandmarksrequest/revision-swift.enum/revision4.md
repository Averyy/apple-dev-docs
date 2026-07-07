# DetectFaceLandmarksRequest.Revision.revision4

**Framework**: Vision  
**Kind**: case

This revision uses [`DetectFaceRectanglesRequest.Revision.revision4`](detectfacerectanglesrequest/revision-swift.enum/revision4.md) for detecting faces and then detects 98 face landmark points, providing more detailed results than the previous revision. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detectfacelandmarksrequest/supportedrevisions.md) to check if this revision is supported on the platform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case revision4
```

## See Also

- [DetectFaceLandmarksRequest.Revision.revision3](detectfacelandmarksrequest/revision-swift.enum/revision3.md)
  An algorithm or implementation that represents the third revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacelandmarksrequest/revision-swift.enum/revision4)*