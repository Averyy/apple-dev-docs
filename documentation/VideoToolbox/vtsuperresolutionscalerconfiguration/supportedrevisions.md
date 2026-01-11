# supportedRevisions

**Framework**: Video Toolbox  
**Kind**: property

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

#### Discussion

A property you use to introspect at runtime which revisions are available for each configuration.

## See Also

- [var revision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision you use to perform the request.
- [class var defaultRevision: VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/defaultrevision.md)
  Provides the default revision of a specific algorithm or configuration.
- [VTSuperResolutionScalerConfiguration.Revision](vtsuperresolutionscalerconfiguration/revision-swift.enum.md)
  Available algorithm revisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsuperresolutionscalerconfiguration/supportedrevisions)*