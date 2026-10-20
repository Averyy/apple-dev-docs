# AdvertiserResourceType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The type of advertiser resource you delegate to an ad account.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdvertiserResourceType
```

## Possible Values

- `CONTENT_PROVIDER`: A content provider resource associated with the ad account. Its `resourceId` is the Content Provider ID (CPID).
- `BUSINESS_BRAND`: A Brand resource delegated from an organization. Its `resourceId` is the Brand ID.

## See Also

- [type ProductFeatures](./productfeatures.md)
  Product features are the advertising capabilities for an ad account.
- [type OrgSystemStatus](./orgsystemstatus.md)
  System-derived operational status of an organization.
- [type OrgSystemStatusReason](./orgsystemstatusreason.md)
  Reasons that can cause an organization’s system status to not be active.
- [type AdAccountSystemStatus](./adaccountsystemstatus.md)
  System-derived operational status of an ad account.
- [type AdAccountSystemStatusReason](./adaccountsystemstatusreason.md)
  Enumeration of reasons that can cause an ad account’s system status to be `INACTIVE`.
- [object AdvertiserResourceListResponse](./advertiserresourcelistresponse.md)
  Response envelope for advertiser resource list requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/advertiserresourcetype)*