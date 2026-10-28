# BrandsReportingCreative.CreativeType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The visual format and placement context of the creative at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingCreative.CreativeType
```

## Possible Values

- `LOCAL_ADS_SEARCH_CREATIVE`: An Ads on Apple Maps creative.

## Discussion

This identifies the creative format captured in the report row, which for Brands campaigns always describes the same Ads on Apple Maps unit type.

The `creativeType` field shares its enum with the App Store reporting equivalent, but Brands (Apple Maps) creative reports only ever return `LOCAL_ADS_SEARCH_CREATIVE`.

### Example

```json
{
  "creativeType": "LOCAL_ADS_SEARCH_CREATIVE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcreative/creativetype-data.typealias)*