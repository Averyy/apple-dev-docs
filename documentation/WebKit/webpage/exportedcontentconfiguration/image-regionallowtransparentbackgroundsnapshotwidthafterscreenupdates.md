# image(region:allowTransparentBackground:snapshotWidth:afterScreenUpdates:)

**Framework**: WebKit  
**Kind**: method

A configuration of a webpage for a representation as image data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func image(region: WebPage.ExportedContentConfiguration.Region = .contents, allowTransparentBackground: Bool = false, snapshotWidth: CGFloat? = nil, afterScreenUpdates: Bool = true) -> WebPage.ExportedContentConfiguration
```

#### Return Value

The image configuration of this page that will be used when producing its representation.

## Parameters

- `region`: The region of the page used to generate the image.
- `allowTransparentBackground`: Indicates whether the image may have a transparent background.
- `snapshotWidth`: The default value of this parameter is  , which returns an image whose size matches the original size of the captured region.
- `afterScreenUpdates`: Indicates whether to take the snapshot after incorporating any pending screen updates.

## See Also

- [WebPage.ExportedContentConfiguration.Region](webpage/exportedcontentconfiguration/region.md)
  Represents a specific semantic region of a webpage.
- [static func pdf(region: WebPage.ExportedContentConfiguration.Region, allowTransparentBackground: Bool) -> WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration/pdf(region:allowtransparentbackground:).md)
  A configuration of a webpage for a representation as PDF data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exportedcontentconfiguration/image(region:allowtransparentbackground:snapshotwidth:afterscreenupdates:))*