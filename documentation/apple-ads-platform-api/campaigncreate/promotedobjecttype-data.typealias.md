# CampaignCreate.PromotedObjectType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The category of entity being promoted by a campaign, determining which ad placements and creative workflows apply.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignCreate.PromotedObjectType
```

## Possible Values

- `APPSTORE_APP`: Promotes an iOS application. Ads serve on App Store placements including Search results, the Search tab, the Today tab, and Product pages. The `promotedObjectId` must be the app’s `adamId` from the App Store. Retrieve it from [`Search for Apps`](../searches-for-a-list-of-apps.md) or [`Get App Details by Adam ID`](../get-app-details-by-adam-id.md). See [Search Apps Endpoints](../search-apps-endpoints.md) for details.
- `BUSINESS_BRAND`: Promotes a brand on Apple Maps. Ads serve on the Maps Search results and Search home placements. The `promotedObjectId` must be the brand identifier. Retrieve it from `GET /v1/advertiser-resources?resourceType=BUSINESS_BRAND`, which returns the `resourceId` for each delegated brand.

#### Discussion

Set at campaign creation and immutable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate/promotedobjecttype-data.typealias)*