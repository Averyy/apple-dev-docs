# SearchEntityListResponse

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The response details of geosearch requests.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object SearchEntityListResponse
```

## Properties

- `data` ([SearchEntity]): Response data that the API provides.
- `error` (ErrorResponseBody): Error response data that the API provides.
- `pagination` (PageDetail): Page detail information that the API provides.

## See Also

### Search Geolocation Request and Response Objects
- [object GeoRequest](./georequest.md)
  The geosearch request object.
- [object SearchEntity](./searchentity.md)
  The list of geolocations that includes the geoidentifier and entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/searchentitylistresponse)*