# AdGroupListResponse

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The response details of ad group requests.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object AdGroupListResponse
```

## Properties

- `data` ([AdGroup]): Response data that the API provides.
- `error` (ErrorResponseBody): Error response data that the API provides.
- `pagination` (PageDetail): Page detail information that the API provides.

## See Also

### Ad Group Request and Response Objects
- [object AdGroup](./adgroup.md)
  The response to ad group requests.
- [object AdGroupUpdate](./adgroupupdate.md)
  The list of ad group fields that are updatable.
- [object AdGroupResponse](./adgroupresponse.md)
  A container for the ad group response body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adgrouplistresponse)*