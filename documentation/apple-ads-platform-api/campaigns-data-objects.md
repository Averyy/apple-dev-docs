# Campaigns Data Objects

**Framework**: Apple Ads Platform API

Reference the request and response schemas for creating, retrieving, and updating campaigns.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

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
- [object ResponsePagination](responsepagination.md)
  Pagination metadata returned in Campaign list responses, supporting offset-based navigation.
- [object RegulationResponse](regulationresponse.md)
  A regulatory disclosure response pairing a regulation type with the advertiser’s answer.
- [object RegulationResponseCreate](regulationresponsecreate.md)
  Request body for submitting a regulatory disclosure response when creating a resource.
- [object RegulationResponseUpdate](regulationresponseupdate.md)
  Request body for updating a regulatory disclosure response.
- [type RegulationResponseValue](regulationresponsevalue.md)
  The advertiser’s answer to a regulatory disclosure question.
- [type RegulationType](regulationtype.md)
  The category of regulatory disclosure required for a campaign or organization.

## See Also

- [Campaigns Endpoints](campaigns-endpoints.md)
  Create, retrieve, update, and delete campaigns using these endpoints.
- [Campaigns Data Types](campaign-data-types.md)
  Look up the enumerated values and scalar types used across campaign fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigns-data-objects)*