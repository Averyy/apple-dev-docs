# LegacyAppLimitedStatusReasonDetailsResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Response wrapper returning per-country or per-region limited-status reasons for legacy app campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object LegacyAppLimitedStatusReasonDetailsResponse
```

#### Discussion

`LegacyAppLimitedStatusReasonDetailsResponse` extends the standard [`Response`](response.md) envelope with a `result` object containing `countryOrRegionLimitedStatusReasons`. This map associates ISO 3166-1 alpha-2 country or region codes with arrays of reason strings that explain why ad delivery is limited in each market for legacy app campaigns.

An empty array for a given country or region means no limiting reasons are currently active there. Reason strings are human-readable labels corresponding to system conditions such as budget exhaustion, policy holds, or app-eligibility issues.

##### Example

```json
{
  "result": {
    "countryOrRegionLimitedStatusReasons": {
      "US": [
        "APP_NOT_ELIGIBLE_SEARCHADS",
        "AD_GROUPS_LIMITED"
      ],
      "GB": [],
      "CA": [
        "APP_DOC_APPROVAL_PENDING"
      ]
    }
  }
}
```

## Properties

- `result` (LegacyAppLimitedStatusReasonDetails): The response payload object. Read-only.
- `error` (Error)

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
- [object CampaignTargetingUpdate](campaigntargetingupdate.md)
  Targeting configuration for updating an existing campaign’s supply source, placement, and geographic markets.
- [object DailyBudgetUpdate](dailybudgetupdate.md)
  Request wrapper for updating a campaign’s daily budget amount.
- [object LegacyAppLimitedStatusReasonDetails](legacyapplimitedstatusreasondetails.md)
  Per-country or per-region limited-status reasons for legacy app campaigns.
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/legacyapplimitedstatusreasondetailsresponse)*