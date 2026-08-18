# InvoiceDetailCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Invoice billing contact details supplied when creating a campaign or budget order.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object InvoiceDetailCreate
```

#### Discussion

`InvoiceDetailCreate` is the create-time counterpart to [`InvoiceDetail`](invoicedetail.md). It is required for Line of Credit (`LOC`) accounts when creating a campaign or budget order.

##### Example

```json
{
  "name": "AwayFinder Q3 Campaign Invoice",
  "primaryBuyerName": "Jordan Blake",
  "primaryBuyerEmail": "jordan.blake@awayfinder.com",
  "billingEmail": "billing@awayfinder.com",
  "clientName": "AwayFinder",
  "orderNumber": "PO-555666777"
}
```

## Properties

- `primaryBuyerName` (string) *(required)*: Name of the primary buyer.
- `primaryBuyerEmail` (string) *(required)*: Email address of the primary buyer. Must be a valid email address.
- `billingEmail` (string) *(required)*: Billing email address. Must be a valid email address.
- `clientName` (string): Identifies the advertiser or product.
- `orderNumber` (string): Purchase order number.

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
- [object LegacyAppLimitedStatusReasonDetailsResponse](legacyapplimitedstatusreasondetailsresponse.md)
  Response wrapper returning per-country or per-region limited-status reasons for legacy app campaigns.
- [object CampaignTargetingUpdate](campaigntargetingupdate.md)
  Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.
- [object DailyBudgetUpdate](dailybudgetupdate.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object LegacyAppLimitedStatusReasonDetails](legacyapplimitedstatusreasondetails.md)
  Per-country or per-region limited-status reasons for legacy app campaigns.
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/invoicedetailcreate)*