# WebPage.ExportedContentConfiguration

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A specialized configuration of a specific exportable type that can have specific properties unique to the content type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
struct ExportedContentConfiguration
```

## Topics

### Configurable types
- [WebPage.ExportedContentConfiguration.Region](./exportedcontentconfiguration/region.md)
  Represents a specific semantic region of a webpage.
- [static func image(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool, snapshotWidth: CGFloat?, afterScreenUpdates: Bool) -> WebPage.ExportedContentConfiguration](./exportedcontentconfiguration/image%28region,allowtransparentbackground,snapshotwidth,afterscreenupdates%29.md)
  A configuration of a webpage for a representation as image data.
- [static func pdf(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool) -> WebPage.ExportedContentConfiguration](./exportedcontentconfiguration/pdf%28region,allowtransparentbackground%29.md)
  A configuration of a webpage for a representation as PDF data.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Exporting webpage content
- [func exported(as: WebPage.ExportedContentConfiguration) async throws -> Data](./exported%28as%29.md)
  Using the type’s `Transferable` conformance implementation, exports a value as binary data, optionally with a specified configuration for that type of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration)*