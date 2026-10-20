# VTOpticalFlowConfiguration.Revision

**Framework**: Video Toolbox  
**Kind**: enum  
**Role**: Enumeration

The specific algorithm or configuration revision that is to be used to perform the request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
enum Revision
```

```c
enum VTOpticalFlowConfigurationRevision : NSInteger;
```

## Topics

### Enumeration Cases
- [VTOpticalFlowConfiguration.Revision.revision1](./revision-swift.enum/revision1.md)
  An algorithm or implementation that represents the first revision.
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
- [var revision: VTOpticalFlowConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
- [class var defaultRevision: VTOpticalFlowConfiguration.Revision](./defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  A boolean value that indicates whether the processor supported on the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/revision-swift.enum)*