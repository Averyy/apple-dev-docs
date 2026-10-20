# DetectFaceRectanglesRequest.Revision

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

A type that describes the algorithm or implementation that the request performs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
enum Revision
```

## Topics

### Getting the revision
- [DetectFaceRectanglesRequest.Revision.revision3](./revision-swift.enum/revision3.md)
  An algorithm or implementation that represents the third revision.
- [DetectFaceRectanglesRequest.Revision.revision4](./revision-swift.enum/revision4.md)
  Compared to `.revision3`, this revision generally provides better precision and recall, and bounding boxes tend to be tighter. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](./supportedrevisions.md) to check if this revision is supported on the platform.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the revision
- [let revision: DetectFaceRectanglesRequest.Revision](./revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectFaceRectanglesRequest.Revision]](./supportedrevisions.md)
  The collection of revisions the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacerectanglesrequest/revision-swift.enum)*