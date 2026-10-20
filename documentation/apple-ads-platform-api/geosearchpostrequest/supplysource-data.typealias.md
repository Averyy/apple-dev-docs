# GeoSearchPostRequest.SupplySource

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The supply source context that scopes a geo location search to App Store or Apple Maps eligibility rules.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string GeoSearchPostRequest.SupplySource
```

## Possible Values

- `APPSTORE`: Scopes the geo search to the App Store supply source. Returns results for App Store campaigns. `PostalCode` entities are excluded.
- `MAPS`: Scopes the geo search to the Apple Maps supply source. Returns results for Apple Maps campaigns. Restricted to US and CA. `Country` entity type excluded. `PostalCode` entities are available.

#### Discussion

Case-insensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geosearchpostrequest/supplysource-data.typealias)*