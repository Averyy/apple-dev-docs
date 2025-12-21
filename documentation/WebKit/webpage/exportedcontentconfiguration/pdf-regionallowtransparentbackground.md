# pdf(region:allowTransparentBackground:)

**Framework**: WebKit  
**Kind**: method

A configuration of a webpage for a representation as PDF data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func pdf(region: WebPage.ExportedContentConfiguration.Region = .contents, allowTransparentBackground: Bool = false) -> WebPage.ExportedContentConfiguration
```

#### Return Value

The PDF configuration of this page that will be used when producing its representation.

## Parameters

- `region`: The region of the page used to generate the PDF.
- `allowTransparentBackground`: Indicates whether the PDF may have a transparent background.

## See Also

- [WebPage.ExportedContentConfiguration.Region](webpage/exportedcontentconfiguration/region.md)
  Represents a specific semantic region of a webpage.
- [static func image(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool, snapshotWidth: CGFloat?, afterScreenUpdates: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/image(region:allowtransparentbackground:snapshotwidth:afterscreenupdates:).md)
  A configuration of a webpage for a representation as image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration/pdf(region:allowtransparentbackground:))*