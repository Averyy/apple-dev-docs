# CIFeatureTypeQRCode

**Framework**: Core Image  
**Kind**: var

A Core Image feature type for QR code object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
let CIFeatureTypeQRCode: String
```

#### Discussion

To detect QR codes in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [`CIQRCodeFeature`](ciqrcodefeature.md) class to find more information about the detected QR code.

## See Also

- [let CIFeatureTypeFace: String](cifeaturetypeface.md)
  A Core Image feature type for person’s face.
- [let CIFeatureTypeRectangle: String](cifeaturetyperectangle.md)
  A Core Image feature type for rectangular object.
- [let CIFeatureTypeText: String](cifeaturetypetext.md)
  A Core Image feature type for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeaturetypeqrcode)*