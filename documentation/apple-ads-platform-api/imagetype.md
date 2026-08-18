# ImageType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Image format type for an uploaded asset.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string ImageType
```

#### Discussion

`ImageType` identifies the image file format of an [`Asset`](asset.md). The system infers the value from the uploaded file and returns it in the asset record. The API caller does not set it directly.

Uploading through [`Upload Asset`](upload-asset.md) only accepts PNG, JPG, and HEIC files. The remaining values (JPEG, HEIF, SVG, WEBP) can appear on assets that were sourced or created outside this upload path.

## See Also

- [type AssetType](assettype.md)
  The media type of an asset.
- [type Orientation](orientation.md)
  Asset orientation and aspect ratio classification.
- [type AssetEligibilityStatus](asseteligibilitystatus.md)
  Overall eligibility status for an asset’s policy evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/imagetype)*