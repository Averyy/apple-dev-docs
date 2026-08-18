# RegulationResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A regulatory disclosure response pairing a regulation type with the advertiser’s answer.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RegulationResponse
```

## Topics

### Type Aliases
- [type RegulationResponse.RegulationType](regulationresponse/regulationtype-data.typealias.md)
  The category of regulatory disclosure this response answers.
- [type RegulationResponse.ResponseValue](regulationresponse/responsevalue-data.typealias.md)
  The advertiser’s answer to the regulatory disclosure question.

## Properties

- `regulationType` (RegulationResponse.RegulationType): The category of regulatory disclosure this response answers. See [`RegulationResponse.RegulationType`](regulationresponse/regulationtype-data.typealias.md). Read-only.
- `responseValue` (RegulationResponse.ResponseValue): The advertiser’s answer to the regulatory disclosure question. See [`RegulationResponse.ResponseValue`](regulationresponse/responsevalue-data.typealias.md). Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponse)*