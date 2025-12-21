# WebPage.ExportedContentConfiguration.Region

**Framework**: WebKit  
**Kind**: struct

Represents a specific semantic region of a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Region
```

## Topics

### Type Properties
- [static var contents: WebPage.ExportedContentConfiguration.Region](webpage/exportedcontentconfiguration/region/contents.md)
  The entire region of the webpage.
### Type Methods
- [static func rect(CGRect) -> WebPage.ExportedContentConfiguration.Region](webpage/exportedcontentconfiguration/region/rect(_:).md)
  A region that corresponds to a rectangle in the page’s coordinate system.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func image(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool, snapshotWidth: CGFloat?, afterScreenUpdates: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/image(region:allowtransparentbackground:snapshotwidth:afterscreenupdates:).md)
  A configuration of a webpage for a representation as image data.
- [static func pdf(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/pdf(region:allowtransparentbackground:).md)
  A configuration of a webpage for a representation as PDF data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration/region)*