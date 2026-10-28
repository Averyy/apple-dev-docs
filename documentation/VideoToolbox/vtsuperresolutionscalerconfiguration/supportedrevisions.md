# supportedRevisions

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

Provides the collection of currently supported algorithms or configuration revisions for the class of configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class var supportedRevisions: IndexSet { get }
```

```objc
@property (class, nonatomic, readonly) NSIndexSet * supportedRevisions;
```

## Discussion

A property you use to introspect at runtime which revisions are available for each configuration.

## See Also

### Inspecting revision information
- [var revision: VTSuperResolutionScalerConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision you use to perform the request.
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](./defaultrevision.md)
  Provides the default revision of a specific algorithm or configuration.
- [VTSuperResolutionScalerConfiguration.Revision](./revision-swift.enum.md)
  Available algorithm revisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/supportedrevisions)*