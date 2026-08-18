# CampaignUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing Campaign object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignUpdate
```

#### Discussion

`CampaignUpdate` is the request payload for modifying an existing campaign. Only the fields listed here can be changed after creation. Immutable fields such as `billingEvent`, `promotedObjectType`, and `promotedObjectId` are not present. Include only the fields you want to modify.

Both `dailyBudget` and `sharedBudgets` can be present on a campaign and function independently: `dailyBudget` caps daily spending, while each shared budget enforces a flight-period cap defined by its `startTime` and `endTime`.

To pause (`PAUSED`) or resume (`ENABLED`) delivery without deleting the campaign, use `status`.

##### Example

```json
{
  "name": "AwayFinder Apple Maps Campaign",
  "startTime": "2025-09-01T00:00:00.000",
  "endTime": "2025-12-31T23:59:59.000",
  "status": "ENABLED",
  "dailyBudget": {
    "value": {
      "amount": "1200.00",
      "currency": "USD"
    }
  },
  "sharedBudgets": [
    {
      "budgetId": 555666777
    }
  ],
  "targeting": {
    "supplySource": {
      "include": [
        "MAPS"
      ]
    },
    "supplyPlacement": {
      "include": [
        "MAPS_SEARCH_RESULTS"
      ]
    },
    "countryOrRegion": {
      "include": [
        "US"
      ]
    }
  },
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP",
    "bid": {
      "amount": "2.50",
      "currency": "USD"
    }
  },
  "invoiceDetail": {
    "name": "AwayFinder Q3 Invoice",
    "orderNumber": "PO-555666777",
    "clientName": "AwayFinder",
    "primaryBuyerName": "Jordan Lee",
    "primaryBuyerEmail": "jordan.lee@awayfinder.com",
    "billingEmail": "billing@awayfinder.com"
  },
  "regulationResponses": [
    {
      "regulationType": "CAMPAIGN_SAPIN_LAW",
      "responseValue": "NOT_ANSWERED"
    }
  ]
}
```

## Topics

### Dictionaries
- [object CampaignUpdate.BidStrategy](campaignupdate/bidstrategy-data.dictionary.md)
  The request body for updating a bid strategy on an ad group or campaign.
- [object CampaignUpdate.DailyBudget](campaignupdate/dailybudget-data.dictionary.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object CampaignUpdate.InvoiceDetail](campaignupdate/invoicedetail-data.dictionary.md)
  The request body for updating the invoice details of a budget order.
- [object CampaignUpdate.Targeting](campaignupdate/targeting-data.dictionary.md)
  Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.
### Type Aliases
- [type CampaignUpdate.Status](campaignupdate/status-data.typealias.md)
  Advertiser-configurable run state for a campaign.

## Properties

- `name` (string): The advertiser-given name of this campaign. Maximum 200 characters. Must be non-empty. Mutable.
- `startTime` (date-time): The scheduled start date and time of the campaign. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-06-07T00:00:00.000`). Mutable.
- `endTime` (date-time): The scheduled end date and time. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-12-31T00:00:00.000`). Omit to keep the campaign running indefinitely. Mutable.
- `status` (CampaignUpdate.Status): Advertiser-configurable serving status. Use to pause or resume the campaign. See [`CampaignStatus`](campaignstatus.md). Mutable.
- `dailyBudget` (CampaignUpdate.DailyBudget): The daily spend cap for this campaign. See [`DailyBudgetUpdate`](dailybudgetupdate.md). Mutable.
- `sharedBudgets` ([SharedBudgetAssignmentUpdate]): One or more budget order assignments for this campaign. See [`SharedBudgetAssignmentUpdate`](sharedbudgetassignmentupdate.md). Mutable.
- `targeting` (CampaignUpdate.Targeting): Country/region, supply source, and placement targeting for this campaign. Mutable.
- `bidStrategy` (CampaignUpdate.BidStrategy): The bid strategy governing how this campaign competes in auctions. `bidStrategyType` and `bidStrategyGoal` must be sent together and matched per the pairings in [`CampaignUpdate.BidStrategy`](campaignupdate/bidstrategy-data.dictionary.md). See [`BidStrategyUpdate`](bidstrategyupdate.md). Mutable.
- `invoiceDetail` (CampaignUpdate.InvoiceDetail): Invoice and billing contact details for Line of Credit accounts. Mutable.
- `regulationResponses` ([RegulationResponseUpdate]): Regulatory consent acknowledgments required in certain markets. See [`RegulationResponseUpdate`](regulationresponseupdate.md). Mutable.

## See Also

- [object Campaign](campaign.md)
  The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.
- [object CampaignCreate](campaigncreate.md)
  The request body for creating a new campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignupdate)*