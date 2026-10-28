# VTSuperResolutionScalerConfiguration.Revision

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum VTSuperResolutionScalerConfigurationRevision : NSInteger;
```

## Overview

A new enum case with a higher revision number is added when the processing algorithm is updated. The [`defaultRevision`](./defaultrevision.md) property provides the default algorithm revision.

## Topics

### Enumeration Cases
- [VTSuperResolutionScalerConfiguration.Revision.revision1](./revision-swift.enum/revision1.md)
### Initializers
- [init?(rawValue: Int)](./revision-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting revision information
- [var revision: VTSuperResolutionScalerConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision you use to perform the request.
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](./defaultrevision.md)
  Provides the default revision of a specific algorithm or configuration.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  Provides the collection of currently supported algorithms or configuration revisions for the class of configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/revision-swift.enum)*