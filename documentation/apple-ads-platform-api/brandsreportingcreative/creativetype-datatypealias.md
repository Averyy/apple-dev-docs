# BrandsReportingCreative.CreativeType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The visual format and placement context of the creative at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string BrandsReportingCreative.CreativeType
```

#### Discussion

`creativeType` shares its enum with the App Store reporting equivalent, but Brands (Apple Maps) creative reports only ever return `LOCAL_ADS_SEARCH_CREATIVE`.

##### Example

```json
{
  "creativeType": "LOCAL_ADS_SEARCH_CREATIVE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcreative/creativetype-data.typealias)*