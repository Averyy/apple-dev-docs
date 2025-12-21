# supportedRevisions

**Framework**: Video Toolbox  
**Kind**: property

The collection of currently-supported algorithms or configuration revisions for the class of configurations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+

## Declaration

```swift
class var supportedRevisions: IndexSet { get }
```

#### Discussion

Use this property to determine the supported revisions for each configuration at runtime.

## See Also

- [var revision: VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/revision-swift.property.md)
  The specific algorithm or configuration revision to use to perform the request.
- [class var defaultRevision: VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [VTFrameRateConversionConfiguration.Revision](vtframerateconversionconfiguration/revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/supportedrevisions)*