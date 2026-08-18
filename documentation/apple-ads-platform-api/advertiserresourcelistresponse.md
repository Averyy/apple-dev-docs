# AdvertiserResourceListResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response envelope for advertiser resource list requests.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdvertiserResourceListResponse
```

#### Discussion

`AdvertiserResourceListResponse` is the response envelope the API returns when you fetch advertiser resources associated with an organization.

Advertiser resources include entities such as content providers and brands. These resources appear in `Delegation` objects and control whether App Store or Apple Maps campaigns are accessible to an ad account.

##### Example

```json
{
  "result": [
    {
      "resourceId": "555666777",
      "resourceType": "CONTENT_PROVIDER",
      "resourceName": "AwayFinder"
    }
  ]
}
```

## Properties

- `error` (Error): Error detail if the request failed. See [`Error`](error.md).
- `result` ([Delegation]): Array of matching advertiser resources. See [`Delegation`](delegation.md).

## See Also

- [type ProductFeatures](productfeatures.md)
  Product features are the advertising capabilities for an ad account.
- [type OrgSystemStatus](orgsystemstatus.md)
  System-derived operational status of an organization.
- [type OrgSystemStatusReason](orgsystemstatusreason.md)
  Reasons that can cause an organization’s system status to be `INACTIVE`.
- [type AdAccountSystemStatus](adaccountsystemstatus.md)
  System-derived operational status of an ad account.
- [type AdAccountSystemStatusReason](adaccountsystemstatusreason.md)
  Enumeration of reasons that can cause an ad account’s system status to be `INACTIVE`.
- [type AdvertiserResourceType](advertiserresourcetype.md)
  The type of advertiser resource you delegate to an ad account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/advertiserresourcelistresponse)*