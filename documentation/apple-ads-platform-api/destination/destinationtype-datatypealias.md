# Destination.DestinationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The type of post-tap destination.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Destination.DestinationType
```

#### Discussion

This mirrors the destination type set when the ad creative was created, tying App Store ad creatives to `APP_STORE_PRODUCT_PAGE` and Apple Maps ad creatives to `LOCAL_ADS_PLACECARD`.

##### Example

```json
{
  "destinationType": "APP_STORE_PRODUCT_PAGE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destination/destinationtype-data.typealias)*