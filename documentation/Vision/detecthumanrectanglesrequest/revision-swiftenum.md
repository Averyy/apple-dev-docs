# DetectHumanRectanglesRequest.Revision

**Framework**: Vision  
**Kind**: enum

A type that describes the algorithm or implementation that the request performs.

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
enum Revision
```

## Topics

### Getting the revision
- [DetectHumanRectanglesRequest.Revision.revision2](detecthumanrectanglesrequest/revision-swift.enum/revision2.md)
  An algorithm or implementation that represents the second revision.
- [DetectHumanRectanglesRequest.Revision.revision3](detecthumanrectanglesrequest/revision-swift.enum/revision3.md)
  Compared to `.revision2`, this revision generally provides better precision and recall. This is the default revision on platforms that support it. Specify `.revision2` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detecthumanrectanglesrequest/supportedrevisions.md) to check if this revision is supported on the platform.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let revision: DetectHumanRectanglesRequest.Revision](detecthumanrectanglesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectHumanRectanglesRequest.Revision]](detecthumanrectanglesrequest/supportedrevisions.md)
  The collection of revisions the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanrectanglesrequest/revision-swift.enum)*