# DetectFaceRectanglesRequest.Revision.revision3

**Framework**: Vision  
**Kind**: case

An algorithm or implementation that represents the third revision.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
case revision3
```

## See Also

- [DetectFaceRectanglesRequest.Revision.revision4](detectfacerectanglesrequest/revision-swift.enum/revision4.md)
  Compared to `.revision3`, this revision generally provides better precision and recall, and bounding boxes tend to be tighter. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detectfacerectanglesrequest/supportedrevisions.md) to check if this revision is supported on the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacerectanglesrequest/revision-swift.enum/revision3)*