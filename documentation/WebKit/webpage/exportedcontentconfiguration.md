# WebPage.ExportedContentConfiguration

**Framework**: WebKit  
**Kind**: struct

A specialized configuration of a specific exportable type that can have specific properties unique to the content type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
struct ExportedContentConfiguration
```

## Topics

### Configurable types
- [WebPage.ExportedContentConfiguration.Region](webpage/exportedcontentconfiguration/region.md)
  Represents a specific semantic region of a webpage.
- [static func image(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool, snapshotWidth: CGFloat?, afterScreenUpdates: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/image(region:allowtransparentbackground:snapshotwidth:afterscreenupdates:).md)
  A configuration of a webpage for a representation as image data.
- [static func pdf(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/pdf(region:allowtransparentbackground:).md)
  A configuration of a webpage for a representation as PDF data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func exported(as: WebPage.ExportedContentConfiguration) async throws -> Data](webpage/exported(as:).md)
  Using the type’s `Transferable` conformance implementation, exports a value as binary data, optionally with a specified configuration for that type of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration)*