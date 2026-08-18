# Campaign

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Campaign
```

#### Discussion

A `Campaign` is the top-level advertising container that defines the promoted object, billing model, scheduling, and geographic targeting for a set of ad groups. Each campaign belongs to a single ad account and promotes either an App Store app (`APPSTORE_APP`) or a brand (`BUSINESS_BRAND`). The `billingEvent`, `promotedObjectType`, and `promotedObjectId` fields stay fixed after creation. To change any of them, create a new campaign.

The `status` field captures the advertiser’s intent for the campaign to serve, while the `systemStatus` field reflects Apple’s system assessment of whether the campaign can deliver. When `systemStatus` isn’t `RUNNING`, inspect `systemStatusReasons` to identify blocking conditions and `systemStatusLimitingReasons` for delivery-reducing (but non-blocking) factors.

A required `dailyBudget` cap controls the campaign’s budget and limits daily spending. You can also assign a campaign to one or more shared budgets via `sharedBudgets`. The two budget controls function independently: `dailyBudget` enforces a daily cap, while each shared budget enforces a flight-period cap defined by its `startTime` and `endTime`.

For filterable fields and query operators, see [`Query Campaigns`](post-campaigns-query.md). For the complete list of required and optional fields at creation, see [`CampaignCreate`](campaigncreate.md). For the fields that can be changed after creation, see [`CampaignUpdate`](campaignupdate.md).

##### Example

```json
{
  "id": 123456789,
  "adAccountId": 555666777,
  "name": "AwayFinder Fall Launch",
  "billingEvent": "TAPS",
  "paymentModel": "LOC",
  "startTime": "2025-01-10T08:00:00.000",
  "endTime": "2025-12-31T00:00:00.000",
  "promotedObjectType": "APPSTORE_APP",
  "promotedObjectId": "987654321",
  "status": "ENABLED",
  "systemStatus": "RUNNING",
  "systemStatusReasons": [],
  "systemStatusLimitingReasons": [],
  "displayStatus": "RUNNING",
  "dailyBudget": {
    "value": {
      "amount": "100.00",
      "currency": "USD"
    }
  },
  "sharedBudgets": [
    {
      "budgetId": 246813579
    }
  ],
  "targeting": {
    "supplySource": {
      "include": [
        "APPSTORE"
      ]
    },
    "supplyPlacement": {
      "include": [
        "APPSTORE_SEARCH_RESULTS"
      ]
    },
    "countryOrRegion": {
      "include": [
        "US",
        "CA"
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
    "orderNumber": "PO-2025-0456",
    "clientName": "AwayFinder Inc.",
    "primaryBuyerName": "Jordan Lee",
    "primaryBuyerEmail": "jordan.lee@awayfinder.com",
    "billingEmail": "billing@awayfinder.com"
  },
  "regulationResponses": [
    {
      "regulationType": "CAMPAIGN_SAPIN_LAW",
      "responseValue": "NOT_ANSWERED"
    }
  ],
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000",
  "deleted": false
}
```

## Topics

### Dictionaries
- [object Campaign.BidStrategy](campaign/bidstrategy-data.dictionary.md)
  Defines how this campaign competes in auctions, including bid type, optimization goal, and bid amount.
- [object Campaign.DailyBudget](campaign/dailybudget-data.dictionary.md)
  Daily budget cap for a campaign.
- [object Campaign.InvoiceDetail](campaign/invoicedetail-data.dictionary.md)
  Invoice details for the LOC payment model.
- [object Campaign.Targeting](campaign/targeting-data.dictionary.md)
  Defines where a campaign is eligible to serve ads, including supply source, placement, and geographic markets.
### Type Aliases
- [type Campaign.BillingEvent](campaign/billingevent-data.typealias.md)
  The user interaction that triggers a charge for a campaign.
- [type Campaign.DisplayStatus](campaign/displaystatus-data.typealias.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type Campaign.PaymentModel](campaign/paymentmodel-data.typealias.md)
  The payment model that determines payment method and budget availability for the ad account running this campaign.
- [type Campaign.PromotedObjectType](campaign/promotedobjecttype-data.typealias.md)
  The category of entity being promoted by a campaign, determining which ad placements and creative workflows apply.
- [type Campaign.Status](campaign/status-data.typealias.md)
  Advertiser-configurable run state for a campaign.
- [type Campaign.SystemStatus](campaign/systemstatus-data.typealias.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type Campaign.SystemStatusLimitingReasons](campaign/systemstatuslimitingreasons-data.typealias.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type Campaign.SystemStatusReasons](campaign/systemstatusreasons-data.typealias.md)
  A reason code explaining why a campaign is not currently running.

## Properties

- `adAccountId` (int64): The ad account this campaign belongs to. Read-only.
- `name` (string): Campaign name. Maximum 200 characters. Must be non-empty. Mutable.
- `billingEvent` (Campaign.BillingEvent): The event type that triggers a charge (for example, `TAPS` or `IMPRESSIONS`). See [`Campaign.BillingEvent`](campaign/billingevent-data.typealias.md). Read-only.
- `paymentModel` (Campaign.PaymentModel): The payment model for this campaign (for example, `LOC` for Line of Credit or `PAYG` for Pay As You Go). See [`Campaign.PaymentModel`](campaign/paymentmodel-data.typealias.md). System-set, Read-only.
- `startTime` (date-time): The scheduled start date and time of the campaign. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-06-07T00:00:00.000`). Mutable.
- `endTime` (date-time): The scheduled end date and time. Format: `yyyy-MM-dd'T'HH:mm:ss.SSS` in UTC (e.g., `2026-12-31T00:00:00.000`). Omit to keep the campaign running indefinitely. Mutable.
- `promotedObjectType` (Campaign.PromotedObjectType): Whether this campaign promotes an App Store app (`APPSTORE_APP`) or a brand (`BUSINESS_BRAND`). See [`Campaign.PromotedObjectType`](campaign/promotedobjecttype-data.typealias.md). Read-only.
- `promotedObjectId` (string): The identifier of the promoted entity: the `adamId` for App Store apps or the brand ID for Brands. Read-only.
- `status` (Campaign.Status): Captures the advertiser’s intent for the campaign to serve. See [`CampaignStatus`](campaignstatus.md). Mutable.
- `systemStatus` (Campaign.SystemStatus): System-computed operational status reflecting the campaign’s current serving state. See [`CampaignSystemStatus`](campaignsystemstatus.md). System-set, Read-only.
- `systemStatusReasons` ([Campaign.SystemStatusReasons]): System-applied reasons that contribute to the current `systemStatus`. See [`CampaignSystemStatusReason`](campaignsystemstatusreason.md) for possible values. System-set, Read-only.
- `systemStatusLimitingReasons` ([Campaign.SystemStatusLimitingReasons]): System-applied reasons that limit delivery below maximum potential. See [`CampaignSystemLimitedStatusReason`](campaignsystemlimitedstatusreason.md) for possible values. System-set, Read-only.
- `displayStatus` (Campaign.DisplayStatus): System-computed, rolled-up delivery state combining `status` and `systemStatus` into a single user-facing label. See [`CampaignDisplayStatus`](campaigndisplaystatus.md). System-set, Read-only.
- `dailyBudget` (Campaign.DailyBudget): The required daily spend cap for this campaign. Limits spending each calendar day, independent of any shared budget assignments. See [`Campaign.DailyBudget`](campaign/dailybudget-data.dictionary.md). Mutable.
- `sharedBudgets` ([SharedBudgetAssignment]): One or more budget orders assigned to this campaign. Each assignment enforces a flight-period spending cap defined by the budget order’s `startTime` and `endTime`. A campaign must have a `dailyBudget` and may also have one or more shared budget assignments. See [`SharedBudgetAssignment`](sharedbudgetassignment.md). Mutable.
- `targeting` (Campaign.Targeting): Country or region, supply source, and placement targeting configuration for this campaign. See [`CampaignTargeting`](campaigntargeting.md). Mutable.
- `bidStrategy` (Campaign.BidStrategy): The bid strategy governing how this campaign competes in auctions. See [`Campaign.BidStrategy`](campaign/bidstrategy-data.dictionary.md). Mutable.
- `invoiceDetail` (Campaign.InvoiceDetail): Invoice and billing contact details. Required for Line of Credit accounts. See [`Campaign.InvoiceDetail`](campaign/invoicedetail-data.dictionary.md). Mutable.
- `regulationResponses` ([RegulationResponse]): Regulatory consent acknowledgments required in certain markets. See [`RegulationResponse`](regulationresponse.md). Mutable.
- `id` (int64): System-assigned unique identifier for this campaign. System-set, Read-only.
- `creationTime` (date-time): Timestamp when this campaign was created (ISO 8601). System-set, Read-only.
- `modificationTime` (date-time): Timestamp of the last modification to this campaign (ISO 8601). System-set, Read-only.
- `deleted` (boolean): Whether this campaign has been soft-deleted. System-set, Read-only.

## See Also

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
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign)*