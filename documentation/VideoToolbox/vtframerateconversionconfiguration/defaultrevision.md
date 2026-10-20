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
class var defaultRevision: VTFrameRateConversionConfiguration.Revision { get }
```

```objc
@property (class, nonatomic, readonly) VTFrameRateConversionConfigurationRevision defaultRevision;
```

## See Also

### Inspecting revision information
- [var revision: VTFrameRateConversionConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision to use to perform the request.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  The collection of currently-supported algorithms or configuration revisions for the class of configurations.
- [VTFrameRateConversionConfiguration.Revision](./revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/defaultrevision)*