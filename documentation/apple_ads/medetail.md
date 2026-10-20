# MeDetail

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The API caller identifiers.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object MeDetail
```

## Properties

- `parentOrgId` (int64): The account parent organization identifier.
- `userId` (int64): The identifier of the API caller.

## See Also

### Access Control List
- [Get User ACL](./get-user-acl.md)
  Fetches roles and organizations that the API has access to.
- [object UserAcl](./useracl.md)
  The response to ACL requests.
- [object UserAclListResponse](./useracllistresponse.md)
  A container for ACL call responses.
- [Get Me Details](./get-me-details.md)
  Fetches details of an API caller.
- [object MeDetailResponse](./medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/medetail)*