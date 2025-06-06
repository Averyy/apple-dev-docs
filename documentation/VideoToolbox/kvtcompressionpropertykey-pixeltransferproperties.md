# kVTCompressionPropertyKey_PixelTransferProperties

**Framework**: Videotoolbox  
**Kind**: var

Properties for configuring a pixel transfer session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_PixelTransferProperties: CFString
```

#### Discussion

The properties for configuring a [`VTPixelTransferSession`](vtpixeltransfersession-api-collection.md) to transfer source frames from the client’s image buffers to the video encoder’s image buffers, if necessary.

#### Discussion

The value is a doc://com.apple.documentation/documentation/corefoundation/cfdictionary-rum of properties to configure a [`VTPixelTransferSession`](vtpixeltransfersession-api-collection.md). Setting this property alone does not necessarily guarantee that a [`VTPixelTransferSession`](vtpixeltransfersession-api-collection.md) will be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_pixeltransferproperties)*