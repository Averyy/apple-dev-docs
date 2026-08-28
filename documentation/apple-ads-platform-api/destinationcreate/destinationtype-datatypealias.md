# DestinationCreate.DestinationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The type of post-tap destination to create.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string DestinationCreate.DestinationType
```

#### Discussion

Apple Maps ad creatives only support `LOCAL_ADS_PLACECARD`, while App Store ad creatives use `APP_STORE_PRODUCT_PAGE`.

##### Example

```json
{
  "destinationType": "APP_STORE_PRODUCT_PAGE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationcreate/destinationtype-data.typealias)*