# UserAclListResponse

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

A container for ACL call responses.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object UserAclListResponse
```

## Properties

- `data` ([UserAcl]): Response data that the API provides.
- `error` (ErrorResponseBody): Error response data that the API provides.
- `pagination` (PageDetail): Page detail information that the API provides.

## See Also

### Access Control List
- [Get User ACL](./get-user-acl.md)
  Fetches roles and organizations that the API has access to.
- [object UserAcl](./useracl.md)
  The response to ACL requests.
- [Get Me Details](./get-me-details.md)
  Fetches details of an API caller.
- [object MeDetail](./medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](./medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/useracllistresponse)*