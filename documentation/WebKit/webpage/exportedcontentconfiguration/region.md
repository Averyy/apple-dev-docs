# WebPage.ExportedContentConfiguration.Region

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Represents a specific semantic region of a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Region
```

## Topics

### Type Properties
- [static var contents: WebPage.ExportedContentConfiguration.Region](./region/contents.md)
  The entire region of the webpage.
### Type Methods
- [static func rect(CGRect) -> WebPage.ExportedContentConfiguration.Region](./region/rect%28_%29.md)
  A region that corresponds to a rectangle in the page’s coordinate system.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configurable types
- [static func image(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool, snapshotWidth: CGFloat?, afterScreenUpdates: Bool) -> WebPage.ExportedContentConfiguration](./image%28region,allowtransparentbackground,snapshotwidth,afterscreenupdates%29.md)
  A configuration of a webpage for a representation as image data.
- [static func pdf(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool) -> WebPage.ExportedContentConfiguration](./pdf%28region,allowtransparentbackground%29.md)
  A configuration of a webpage for a representation as PDF data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration/region)*