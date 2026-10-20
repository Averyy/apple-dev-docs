# ImageType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Image format type for an uploaded asset.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string ImageType
```

## Possible Values

- `JPEG`: JPEG image format.
- `JPG`: JPG image format.
- `PNG`: PNG image format.
- `HEIC`: HEIC (High Efficiency Image Container) format.
- `HEIF`: HEIF (High Efficiency Image Format).
- `SVG`: Scalable Vector Graphics format.
- `WEBP`: WebP image format.

#### Discussion

The `ImageType` identifies the image file format of an [`Asset`](./asset.md). The system infers the value from the uploaded file and returns it in the asset record. The API caller doesn’t set it directly.

Uploading through [`Upload Asset`](./upload-asset.md) only accepts PNG, JPG, and HEIC files. The remaining values (JPEG, HEIF, SVG, WEBP) can appear on assets that were sourced or created outside this upload path.

## See Also

- [type AssetType](./assettype.md)
  The media type of an asset.
- [type Orientation](./orientation.md)
  Asset orientation and aspect ratio classification.
- [type AssetEligibilityStatus](./asseteligibilitystatus.md)
  Overall eligibility status for an asset’s policy evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/imagetype)*