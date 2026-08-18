# AppsReportingCreative.CreativeType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The visual format and placement context of the creative at report time.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AppsReportingCreative.CreativeType
```

#### Discussion

`creativeType` in reporting context mirrors the creation-time `creativeType` field on the creative, reflecting the format the creative used during the report’s date range. `creativeType` shares its enum with the Apple Maps (Brands) reporting equivalent, but APPS ad reports only ever return `CUSTOM_PRODUCT_PAGE` or `DEFAULT_PRODUCT_PAGE`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcreative/creativetype-data.typealias)*