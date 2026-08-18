# DailyBudget

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Daily budget cap for a campaign.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object DailyBudget
```

#### Discussion

`DailyBudget` is the campaign-level daily spend cap. Once the daily budget is exhausted, the campaign stops delivering ads for the remainder of that day.

`dailyBudget` is required on all campaigns and caps daily spending. When a campaign also has shared budget assignments, both operate independently: `dailyBudget` enforces a daily cap while each shared budget enforces a flight-period cap defined by its `startTime` and `endTime`.

##### Example

```json
{
  "value": {
    "amount": "100.00",
    "currency": "USD"
  }
}
```

## Properties

- `value` (Money): The daily budget amount as a Money object with amount and ISO 4217 currency code. The currency must match the ad account’s currency. See [`Money`](money.md). Mutable.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/dailybudget)*