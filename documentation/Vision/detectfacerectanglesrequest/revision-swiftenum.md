# DetectFaceRectanglesRequest.Revision

**Framework**: Vision  
**Kind**: enum

A type that describes the algorithm or implementation that the request performs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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
- [DetectFaceRectanglesRequest.Revision.revision3](detectfacerectanglesrequest/revision-swift.enum/revision3.md)
  An algorithm or implementation that represents the third revision.
- [DetectFaceRectanglesRequest.Revision.revision4](detectfacerectanglesrequest/revision-swift.enum/revision4.md)
  Compared to `.revision3`, this revision generally provides better precision and recall, and bounding boxes tend to be tighter. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detectfacerectanglesrequest/supportedrevisions.md) to check if this revision is supported on the platform.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let revision: DetectFaceRectanglesRequest.Revision](detectfacerectanglesrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectFaceRectanglesRequest.Revision]](detectfacerectanglesrequest/supportedrevisions.md)
  The collection of revisions the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacerectanglesrequest/revision-swift.enum)*