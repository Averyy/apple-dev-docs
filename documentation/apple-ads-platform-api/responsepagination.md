# ResponsePagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination metadata returned in Campaign list responses, supporting offset-based navigation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ResponsePagination
```

#### Discussion

`ResponsePagination` reports offset-based pagination metadata: `offset`/`pageSize`/`totalCount` allow jumping to any page directly.

##### Example

```json
{
  "offset": 0,
  "pageSize": 20,
  "totalCount": 143
}
```

## Properties

- `offset` (integer): The starting position of the current page. Read-only.
- `pageSize` (integer): The number of items returned in this page. Read-only.
- `totalCount` (integer): The total number of items matching the query across all pages. Read-only.

## See Also

- [object Campaign](campaign.md)
  The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.
- [object CampaignCreate](campaigncreate.md)
  The request body for creating a new campaign.
- [object CampaignUpdate](campaignupdate.md)
  The request body for updating an existing Campaign object.
- [object CampaignResponse](campaignresponse.md)
  The response object for a Campaign operation.
- [object CampaignQueryResponse](campaignqueryresponse.md)
  The response object for a Campaign query, containing matched results and pagination metadata.
- [object CampaignTargeting](campaigntargeting.md)
  Defines where a campaign is eligible to serve ads, including supply source, placement, and geographic markets.
- [object CampaignTargetingCreate](campaigntargetingcreate.md)
  Targeting configuration supplied when creating a campaign.
- [object DailyBudget](dailybudget.md)
  Daily budget cap for a campaign.
- [object DailyBudgetCreate](dailybudgetcreate.md)
  Request wrapper for setting a campaign’s daily budget at creation time.
- [object Money](money.md)
  Monetary representation with currency.
- [object InvoiceDetailCreate](invoicedetailcreate.md)
  Invoice billing contact details supplied when creating a campaign or budget order.
- [object LegacyAppLimitedStatusReasonDetailsResponse](legacyapplimitedstatusreasondetailsresponse.md)
  Response wrapper returning per-country or per-region limited-status reasons for legacy app campaigns.
- [object CampaignTargetingUpdate](campaigntargetingupdate.md)
  Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.
- [object DailyBudgetUpdate](dailybudgetupdate.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object LegacyAppLimitedStatusReasonDetails](legacyapplimitedstatusreasondetails.md)
  Per-country or per-region limited-status reasons for legacy app campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/responsepagination)*