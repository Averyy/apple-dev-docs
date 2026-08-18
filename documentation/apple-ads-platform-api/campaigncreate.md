# CampaignCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignCreate
```

#### Discussion

Creating a campaign ties together what’s being promoted, a budget, targeting, and a bid strategy in a single request.

##### Example

```json
{
  "name": "AwayFinder App Campaign",
  "startTime": "2025-09-01T00:00:00.000",
  "endTime": "2025-12-31T23:59:59.000",
  "dailyBudget": {
    "value": {
      "amount": "100.00",
      "currency": "USD"
    }
  },
  "sharedBudgets": [
    {
      "budgetId": 555666777
    }
  ],
  "targeting": {
    "countryOrRegion": {
      "include": [
        "US"
      ]
    },
    "supplyPlacement": {
      "include": [
        "APPSTORE_SEARCH_RESULTS"
      ]
    }
  },
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP"
  },
  "invoiceDetail": {
    "name": "AwayFinder Inc.",
    "orderNumber": "PO-100234",
    "clientName": "AwayFinder Inc.",
    "primaryBuyerName": "Jordan Lee",
    "primaryBuyerEmail": "jordan.lee@awayfinder.com",
    "billingEmail": "billing@awayfinder.com"
  },
  "regulationResponses": [
    {
      "regulationType": "CAMPAIGN_SAPIN_LAW",
      "responseValue": "NOT_AGENT"
    }
  ],
  "adAccountId": 123456789,
  "billingEvent": "TAPS",
  "promotedObjectId": "987654321",
  "promotedObjectType": "APPSTORE_APP",
  "status": "ENABLED"
}
```

## Topics

### Dictionaries
- [object CampaignCreate.BidStrategy](campaigncreate/bidstrategy-data.dictionary.md)
  The creation payload for configuring a bid strategy on an ad group or campaign.
- [object CampaignCreate.DailyBudget](campaigncreate/dailybudget-data.dictionary.md)
  Request wrapper for setting a campaign’s daily budget at creation time.
- [object CampaignCreate.InvoiceDetail](campaigncreate/invoicedetail-data.dictionary.md)
  Invoice billing contact details supplied when creating a campaign or budget order.
- [object CampaignCreate.Targeting](campaigncreate/targeting-data.dictionary.md)
  Targeting configuration supplied when creating a campaign.
### Type Aliases
- [type CampaignCreate.BillingEvent](campaigncreate/billingevent-data.typealias.md)
  The user interaction that triggers a charge for a campaign.
- [type CampaignCreate.PromotedObjectType](campaigncreate/promotedobjecttype-data.typealias.md)
  The category of entity being promoted by a campaign, determining which ad placements and creative workflows apply.
- [type CampaignCreate.Status](campaigncreate/status-data.typealias.md)
  Advertiser-configurable run state for a campaign.

## Properties

- `name` (string) *(required)*: The advertiser-given name of this campaign. Maximum 200 characters. Must be non-empty. Mutable.
- `startTime` (date-time): The scheduled start date and time of this campaign. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2025-09-01T00:00:00.000`). If omitted, the campaign starts immediately upon activation. Mutable.
- `endTime` (date-time): The scheduled end date and time. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2025-12-31T23:59:59.000`). Omit to keep the campaign running indefinitely. Mutable.
- `dailyBudget` (CampaignCreate.DailyBudget) *(required)*: The daily spend cap for this campaign. See [`DailyBudgetCreate`](dailybudgetcreate.md). Mutable.
- `sharedBudgets` ([SharedBudgetAssignmentCreate]): One or more budget order assignments for this campaign. Can be provided alongside `dailyBudget`. See [`SharedBudgetAssignmentCreate`](sharedbudgetassignmentcreate.md).
- `targeting` (CampaignCreate.Targeting) *(required)*: Country or region, supply source, and placement targeting for this campaign. See [`CampaignTargetingCreate`](campaigntargetingcreate.md). Mutable.
- `bidStrategy` (CampaignCreate.BidStrategy): Bid strategy governing how this campaign competes in auctions. `bidStrategyType` and `bidStrategyGoal` must both be supplied and must match one of the pairings in [`CampaignCreate.BidStrategy`](campaigncreate/bidstrategy-data.dictionary.md). Omitting either field, or pairing a mismatched goal, returns an error. See [`BidStrategyCreate`](bidstrategycreate.md). Mutable.
- `invoiceDetail` (CampaignCreate.InvoiceDetail): Invoice and billing contact details. Required for Line of Credit accounts. See [`InvoiceDetailCreate`](invoicedetailcreate.md).
- `regulationResponses` ([RegulationResponseCreate]): Regulatory consent acknowledgments required in certain markets. See [`RegulationResponseCreate`](regulationresponsecreate.md).
- `adAccountId` (int64) *(required)*: The ad account this campaign belongs to. Immutable after creation.
- `billingEvent` (CampaignCreate.BillingEvent) *(required)*: The billing event for this campaign. See [`CampaignCreate.BillingEvent`](campaigncreate/billingevent-data.typealias.md). Immutable after creation.
- `promotedObjectId` (string) *(required)*: The identifier for the promoted object (for example, an app Adam ID). Immutable after creation.
- `promotedObjectType` (CampaignCreate.PromotedObjectType) *(required)*: The type of the promoted object. See [`CampaignCreate.PromotedObjectType`](campaigncreate/promotedobjecttype-data.typealias.md). Immutable after creation.
- `status` (CampaignCreate.Status): Advertiser-configurable serving status, `ENABLED` or `PAUSED`. Specify it explicitly if a specific initial status is required. See [`CampaignStatus`](campaignstatus.md).

## See Also

- [object Campaign](campaign.md)
  The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.
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
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigncreate)*