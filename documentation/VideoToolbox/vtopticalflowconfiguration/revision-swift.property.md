# revision

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Instance Property

The specific algorithm or configuration revision that is to be used to perform the request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
var revision: VTOpticalFlowConfiguration.Revision { get }
```

```objc
@property (nonatomic, readonly) VTOpticalFlowConfigurationRevision revision;
```

## See Also

### Inspecting revision information
- [class var defaultRevision: VTOpticalFlowConfiguration.Revision](./defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  A boolean value that indicates whether the processor supported on the current configuration.
- [VTOpticalFlowConfiguration.Revision](./revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtopticalflowconfiguration/revision-swift.property)*