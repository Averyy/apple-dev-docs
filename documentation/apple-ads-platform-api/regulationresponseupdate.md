# RegulationResponseUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for updating a regulatory disclosure response.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RegulationResponseUpdate
```

## Topics

### Type Aliases
- [type RegulationResponseUpdate.RegulationType](regulationresponseupdate/regulationtype-data.typealias.md)
  The category of regulatory disclosure being answered.
- [type RegulationResponseUpdate.ResponseValue](regulationresponseupdate/responsevalue-data.typealias.md)
  The advertiser’s answer to the regulatory disclosure question.

## Properties

- `regulationType` (RegulationResponseUpdate.RegulationType): The category of regulatory disclosure being answered. See [`RegulationResponseUpdate.RegulationType`](regulationresponseupdate/regulationtype-data.typealias.md). Not nullable.
- `responseValue` (RegulationResponseUpdate.ResponseValue): The advertiser’s answer to the regulatory disclosure question. See [`RegulationResponseUpdate.ResponseValue`](regulationresponseupdate/responsevalue-data.typealias.md). Not nullable.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/regulationresponseupdate)*