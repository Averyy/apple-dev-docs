# DetectHumanRectanglesRequest.Revision.revision2

**Framework**: Vision  
**Kind**: case

An algorithm or implementation that represents the second revision.

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
case revision2
```

## See Also

- [DetectHumanRectanglesRequest.Revision.revision3](detecthumanrectanglesrequest/revision-swift.enum/revision3.md)
  Compared to `.revision2`, this revision generally provides better precision and recall. This is the default revision on platforms that support it. Specify `.revision2` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detecthumanrectanglesrequest/supportedrevisions.md) to check if this revision is supported on the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanrectanglesrequest/revision-swift.enum/revision2)*