# defaultRevision

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

The default revision of a particular algorithm or configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
class var defaultRevision: VTOpticalFlowConfiguration.Revision { get }
```

```objc
@property (class, nonatomic, readonly) VTOpticalFlowConfigurationRevision defaultRevision;
```

## See Also

### Inspecting revision information
- [var revision: VTOpticalFlowConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision that is to be used to perform the request.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  A boolean value that indicates whether the processor supported on the current configuration.
- [VTOpticalFlowConfiguration.Revision](./revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/defaultrevision)*