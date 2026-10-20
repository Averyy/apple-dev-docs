# supportedRevisions

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, readonly) NSIndexSet * supportedRevisions;
```

#### Discussion

Use this property to determine the supported revisions for each configuration at runtime.

## See Also

### Inspecting revision information
- [var revision: VTFrameRateConversionConfiguration.Revision](./revision-swift.property.md)
  The specific algorithm or configuration revision to use to perform the request.
- [class var defaultRevision: VTFrameRateConversionConfiguration.Revision](./defaultrevision.md)
  The default revision of a particular algorithm or configuration.
- [VTFrameRateConversionConfiguration.Revision](./revision-swift.enum.md)
  The specific algorithm or configuration revision that is to be used to perform the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframerateconversionconfiguration/supportedrevisions)*