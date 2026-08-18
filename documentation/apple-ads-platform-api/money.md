# Money

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Monetary representation with currency.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Money
```

#### Discussion

`Money` is the standard monetary value type used throughout the API for budgets, bids, and spend amounts. An account doesn’t support mixing currencies.

To avoid validation errors when setting bid amounts or budgets, always use the currency code returned by the ad account’s `currency` field.

##### Example

```json
{
  "currency": "USD",
  "amount": "10.00"
}
```

> **Note**: Don’t set amount fields with leading zeros. Use `"5.00"` rather than `"05.00"`.

## Properties

- `currency` (string): The ISO 4217 currency code (for example, `"USD"`, `"EUR"`). Must match the ad account’s currency.
- `amount` (string) *(required)*: The monetary amount as a decimal string (for example, `"10.00"`), represented as a string to preserve decimal precision.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/money)*