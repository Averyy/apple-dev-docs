# DetectHumanRectanglesRequest.Revision.revision3

**Framework**: Vision  
**Kind**: case

Compared to `.revision2`, this revision generally provides better precision and recall. This is the default revision on platforms that support it. Specify `.revision2` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detecthumanrectanglesrequest/supportedrevisions.md) to check if this revision is supported on the platform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case revision3
```

## See Also

- [DetectHumanRectanglesRequest.Revision.revision2](detecthumanrectanglesrequest/revision-swift.enum/revision2.md)
  An algorithm or implementation that represents the second revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanrectanglesrequest/revision-swift.enum/revision3)*