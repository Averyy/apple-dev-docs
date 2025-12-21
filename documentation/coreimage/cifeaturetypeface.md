# CIFeatureTypeFace

**Framework**: Core Image  
**Kind**: var

A Core Image feature type for person’s face.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
let CIFeatureTypeFace: String
```

#### Discussion

To detect faces in an image or video, pass this to `/CIDetector/detectorOfType:context:options:`

Use the [`CIFaceFeature`](cifacefeature.md) class to find more information about the detected face.

## See Also

- [let CIFeatureTypeRectangle: String](cifeaturetyperectangle.md)
  A Core Image feature type for rectangular object.
- [let CIFeatureTypeQRCode: String](cifeaturetypeqrcode.md)
  A Core Image feature type for QR code object.
- [let CIFeatureTypeText: String](cifeaturetypetext.md)
  A Core Image feature type for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)*