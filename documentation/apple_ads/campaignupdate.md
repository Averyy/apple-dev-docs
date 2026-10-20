# CampaignUpdate

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The list of campaign fields that are updatable.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object CampaignUpdate
```

## Properties

- `biddingStrategy` (string): The bidding strategy for the campaign.

  **Default**: `MANUAL_CPT`; **Allowed Values**: `MANUAL_CPT`, `MAX_CONVERSIONS`
- `budgetOrders` ([int64]): The budget orders that you assign to the campaign. This applies only to campaigns with monthly invoicing. Refer to the [Apple Ads Advanced help](https://ads.apple.com/help/billing/0031-monthly-invoicing) for billing details.
- `countriesOrRegions` ([string]): The App Store geoterritories where you’re promoting your app. The default value is `US`.

  This field requires an ISO country code value for the locations where you’re promoting.
- `dailyBudgetAmount` (Money): Your daily budget.

  - Campaigns require a `dailyBudgetAmount`.
  - Your `dailyBudgetAmount` must be greater than or equal to the `defaultBidAmount` in your [`AdGroup`](./adgroup.md).

  You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.
- `locInvoiceDetails` (LOCInvoiceDetails): The standard invoice details you can set and edit using the [`LOCInvoiceDetails`](./locinvoicedetails.md) object.
- `name` (string): The name of the campaign, which is unique within an organization.
- `status` (string): The user-controlled status to enable or pause the campaign.

  **Allowed Values**: `ENABLED`, `PAUSED`
- `targetCpa` (Money): The target cost-per-acquisition for `MAX_CONVERSIONS` campaigns. This field is required if the `biddingStrategy` is `MAX_CONVERSIONS`. Returned as `null` for `MANUAL_CPT campaigns`.

  Mutable after campaign creation.

## See Also

### Campaign Request and Response Objects
- [object Campaign](./campaign.md)
  The response to a request to create and fetch campaigns.
- [object CampaignResponse](./campaignresponse.md)
  A container for the campaign response body.
- [object Campaign.CountryOrRegionServingStateReasons](./campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.
- [object CampaignListResponse](./campaignlistresponse.md)
  The response details of campaign requests.
- [object UpdateCampaignRequest](./updatecampaignrequest.md)
  The payload properties to clear geotargeting from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/campaignupdate)*