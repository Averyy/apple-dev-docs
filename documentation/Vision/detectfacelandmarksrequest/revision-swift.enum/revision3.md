# DetectFaceLandmarksRequest.Revision.revision3

**Framework**: Vision  
**Kind**: case

An algorithm or implementation that represents the third revision.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
case revision3
```

## See Also

- [DetectFaceLandmarksRequest.Revision.revision4](detectfacelandmarksrequest/revision-swift.enum/revision4.md)
  This revision uses [`DetectFaceRectanglesRequest.Revision.revision4`](detectfacerectanglesrequest/revision-swift.enum/revision4.md) for detecting faces and then detects 98 face landmark points, providing more detailed results than the previous revision. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detectfacelandmarksrequest/supportedrevisions.md) to check if this revision is supported on the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacelandmarksrequest/revision-swift.enum/revision3)*