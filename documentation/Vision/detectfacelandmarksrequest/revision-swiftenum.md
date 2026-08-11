# DetectFaceLandmarksRequest.Revision

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
- [DetectFaceLandmarksRequest.Revision.revision3](detectfacelandmarksrequest/revision-swift.enum/revision3.md)
  An algorithm or implementation that represents the third revision.
- [DetectFaceLandmarksRequest.Revision.revision4](detectfacelandmarksrequest/revision-swift.enum/revision4.md)
  This revision uses [`DetectFaceRectanglesRequest.Revision.revision4`](detectfacerectanglesrequest/revision-swift.enum/revision4.md) for detecting faces and then detects 98 face landmark points, providing more detailed results than the previous revision. This is the default revision on platforms that support it. Specify `.revision3` at instantiation to preserve the previous behavior. Use [`supportedRevisions`](detectfacelandmarksrequest/supportedrevisions.md) to check if this revision is supported on the platform.

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

- [let revision: DetectFaceLandmarksRequest.Revision](detectfacelandmarksrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [DetectFaceLandmarksRequest.Revision]](detectfacelandmarksrequest/supportedrevisions.md)
  The collection of revisions the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectfacelandmarksrequest/revision-swift.enum)*