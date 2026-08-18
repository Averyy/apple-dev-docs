# AdGroupTargetingUpdate.PostalCode

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Postal code geographic targeting.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdGroupTargetingUpdate.PostalCode
```

#### Discussion

Postal code IDs are returned by [`Search Geo Locations`](searches-for-a-list-of-geo-locations.md) or [`Query Geo Locations`](gets-a-list-of-geo-locations.md). Applies to Apple Maps campaigns. Uses the [`TargetingDataUpdate`](targetingdataupdate.md) `include`/`exclude` shape.

```json
"postalCode": {
  "include": ["11412181"]
}
```

## Properties

- `include` ([string]): Postal code IDs restricting delivery to those areas. Mutable.
- `exclude` ([string]): Has no effect. `postalCode` is include-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgrouptargetingupdate/postalcode-data.dictionary)*