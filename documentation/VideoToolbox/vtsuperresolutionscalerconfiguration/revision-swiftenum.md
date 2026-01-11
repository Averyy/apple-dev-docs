# VTSuperResolutionScalerConfiguration.Revision

**Framework**: Video Toolbox  
**Kind**: enum

Available algorithm revisions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Revision
```

#### Overview

A new enum case with a higher revision number is added when the processing algorithm is updated. The [`defaultRevision`](vtsuperresolutionscalerconfiguration/defaultrevision.md) property provides the default algorithm revision.

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerConfiguration.Revision.revision1](vtsuperresolutionscalerconfiguration/revision-swift.enum/revision1.md)
### Initializers
- [init?(rawValue: Int)](vtsuperresolutionscalerconfiguration/revision-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var revision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision you use to perform the request.
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/defaultrevision.md)
  Provides the default revision of a specific algorithm or configuration.
- [class var supportedRevisions: IndexSet](vtsuperresolutionscalerconfiguration/supportedrevisions.md)
  Provides the collection of currently supported algorithms or configuration revisions for the class of configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/revision-swift.enum)*