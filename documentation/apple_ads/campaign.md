# Campaign

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The response to a request to create and fetch campaigns.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object Campaign
```

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 2](./apple-search-ads-campaign-management-api-2.md)
- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

## Topics

### Objects
- [object Campaign.CountryOrRegionServingStateReasons](./campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.

## Properties

- `adamId` (int64) *(required)*: Your unique App Store app identifier. You can obtain your app `adamId` through [`Search for iOS apps`](./search-for-ios-apps.md), [`Get a Campaign`](./get-a-campaign.md), or [`Get all Campaigns`](./get-all-campaigns.md).

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).
- `adChannelType` (string) *(required)*: The channel type of an ad in a campaign.

  See [`AdChannelType`](./adchanneltype.md) for value descriptions.

  You can use the `EQUALS` selector [`Condition`](./condition.md) operator with [`Find Campaigns`](./find-campaigns.md) and [`Get Campaign-Level Reports`](./get-campaign-level-reports.md).

  **Allowed Values**: `SEARCH, DISPLAY`
- `billingEvent` (string) *(required)*: The type of billing event for a campaign.

  See [`BillingEventType`](./billingeventtype.md) for value descriptions.

  **Allowed Values**: `IMPRESSIONS`, `TAPS`
- `biddingStrategy` (string): The bidding strategy for the campaign. Possible values include:

  `MANUAL_CPT` (default): The manual cost-per-tap bidding. This is existing behavior in the API.

  `MAX_CONVERSIONS`: Maximize Conversions bidding strategy with automated bid optimization.

  Mutable after campaign creation. This field is updatable. To switch bidding stategies, see [`Update a Campaign`](./update-a-campaign.md).

  **Default**: `MANUAL_CPT`; **Allowed Values**: `MANUAL_CPT`, `MAX_CONVERSIONS`
- `budgetOrders` ([int64]): The budget orders that you assign to the campaign. This applies only to campaigns with a line-of-credit payment model.

  This field is updatable.
- `countriesOrRegions` ([string]) *(required)*: The App Store geoterritories where you’re promoting your app. The default value is `US`.

  Use an alpha-2 country code value , such as `US`, for the locations where you’re promoting.

  The `EQUALS`, `CONTAINS_ANY`, and `CONTAINS_ALL` selector [`Condition`](./condition.md) operators are available to use with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.
- `countryOrRegionServingStateReasons` (Campaign.CountryOrRegionServingStateReasons): The map of reasons that returns when a campaign isn’t running.

  See [`CampaignCountryOrRegionsServingStateReasons`](./campaigncountryorregionsservingstatereasons.md) for value descriptions.
- `creationTime` (date-time): The date and time of the creation of the `campaign` object.
- `dailyBudgetAmount` (Money) *(required)*: Your daily budget.

  A `dailyBudgetAmount` is a required field for all new campaigns.

  - A `dailyBudgetAmount` can be changed but not removed from the payload when updating an existing campaign.
  - Your `dailyBudgetAmount` must be greater than or equal to the `defaultBidAmount` in your [`AdGroup`](./adgroup.md).

  You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.
- `deleted` (boolean): The indicator of whether the campaign is soft-deleted.

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  **Default**: `false`
- `displayStatus` (string): The status of the campaign. The status resolves according to `servingStatus` and additional criteria.

  **Allowed Values**: `DELETED`, `ON_HOLD`, `PAUSED`, `RUNNING`
- `endTime` (date-time): The scheduled end time and date for the campaign.

  - The `endTime` must be after the `startTime`.
  - The `endTime` is updatable until you reach the designated time.
  - The `endTime` must be in UTC.

  You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).
- `id` (int64): A unique identifier for the campaign that you can use as a `campaignid` in endpoint resources.

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).
- `locInvoiceDetails` (LOCInvoiceDetails): The standard invoice details that you can set and edit using the [`LOCInvoiceDetails`](./locinvoicedetails.md) object.

  This field is updatable.
- `modificationTime` (date-time): The date and time of the most recent modification of the object.

  You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).
- `name` (string) *(required)*: The name of the campaign, which is unique within an organization.

  You can use the `EQUALS`, `IN`, and `STARTSWITH` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.

  **Maximum Length**: `200`
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [Apple Ads](https://ads.apple.com/).
- `paymentModel` (string): The payment model that you set through [Apple Ads](https://ads.apple.com/). If you don’t set a payment model, campaigns can’t run.

  See [`PaymentModel`](./paymentmodel.md) for value descriptions.

  If you don’t select a payment model, you can still create campaigns. You must select a payment model before a campaign is eligible to run.

  See [`BudgetOrder`](./budgetorder.md) for details about setting a payment model.

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  **Allowed Values**: `LOC`, `PAYG`
- `servingStateReasons` ([string]): A list of reasons that displays when a campaign can’t run.

  See [`CampaignServingStateReasons`](./campaignservingstatereasons.md) for value descriptions.

  **Allowed Values**: `AD_GROUP_MISSING`, `APP_NOT_CATEGORIZED`, `APP_NOT_ELIGIBLE`, `APP_NOT_ELIGIBLE_SEARCHADS`, `APP_NOT_ELIGIBLE_SUPPLY_SOURCE`, `APP_NOT_LINKED_TO_CAMPAIGN_GROUP`, `APP_NOT_PUBLISHED_YET`, `APP_SENSITIVE_CONTENT`, `BO_END_DATE_REACHED`, `BO_EXHAUSTED`, `BO_START_DATE_IN_FUTURE`, `CAMPAIGN_END_DATE_REACHED`, `CAMPAIGN_START_DATE_IN_FUTURE`, `CONTENT_PROVIDER_UNLINKED`, `CREDIT_CARD_DECLINED`, `DAILY_CAP_EXHAUSTED`, `DELETED_BY_USER`, `FEATURE_NOT_YET_AVAILABLE`, `FEATURE_NO_LONGER_AVAILABLE`, `INELIGIBLE_BUSINESS_LOCATION`, `LOC_EXHAUSTED`, `MISSING_BO_OR_INVOICING_FIELDS`, `NO_AVAILABLE_AD_GROUPS`, `NO_ELIGIBLE_COUNTRIES`, `NO_PAYMENT_METHOD_ON_FILE`, `ORG_CHARGE_BACK_DISPUTED`, `ORG_PAYMENT_TYPE_CHANGED`, `ORG_SUSPENDED_FRAUD`, `ORG_SUSPENDED_POLICY_VIOLATION`, `PAUSED_BY_SYSTEM`, `PAUSED_BY_USER`, `SAPIN_LAW_AGENT_UNKNOWN`, `SAPIN_LAW_FRENCH_BIZ`, `SAPIN_LAW_FRENCH_BIZ_UNKNOWN`, `TAX_VERIFICATION_PENDING`, `TOTAL_BUDGET_EXHAUSTED`, `USER_REQUESTED_ACCOUNT_SUSPENSION`
- `servingStatus` (string): The status of the campaign.

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  **Allowed Values**: `RUNNING`, `NOT_RUNNING`
- `startTime` (date-time): The scheduled start time and date for the campaign.

  - The `startTime` must be greater than the current time, and before the campaign `endTime`, if you set it.
  - If you don’t set a `startTime`, the campaign defaults to the campaign request timestamp and the `startTime` is updatable until you reach the designated time.
  - The `startTime` must be in UTC.

  You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.
- `status` (string): The user-controlled status to enable or pause the campaign.

  You can use the `EQUALS` and `IN` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  This field is updatable.

  **Default**: `ENABLED`; **Allowed Values**: `ENABLED`, `PAUSED`
- `supplySources` ([string]) *(required)*: The ad placements for a campaign.

  See [`SupplySource`](./supplysource.md) for full descriptions of values.

  You can use the  `EQUALS` , `CONTAINS_ANY`, `CONTAINS_ALL` selector [`Condition`](./condition.md) operators with [`Find Campaigns`](./find-campaigns.md).

  **Allowed Values**: `APPSTORE_PRODUCT_PAGES_BROWSE`, `APPSTORE_SEARCH_RESULTS`, `APPSTORE_SEARCH_TAB`, `APPSTORE_TODAY_TAB`
- `targetCpa` (Money): The target cost-per-acquisition for `MAX_CONVERSIONS` campaigns. This field is required if the biddingStrategy is `MAX_CONVERSIONS`. The Target CPA is the average amount you want to spend per tap-through install. This amount is used to calculate optimal bids for each search query, with the goal of maximizing the number of installs near your target CPA.

  Returned as `null` for `MANUAL_CPT campaigns`.

  Mutable after campaign creation.

## See Also

### Campaign Request and Response Objects
- [object CampaignResponse](./campaignresponse.md)
  A container for the campaign response body.
- [object Campaign.CountryOrRegionServingStateReasons](./campaign/countryorregionservingstatereasons-data.dictionary.md)
  Reasons why a campaign can’t run.
- [object CampaignListResponse](./campaignlistresponse.md)
  The response details of campaign requests.
- [object CampaignUpdate](./campaignupdate.md)
  The list of campaign fields that are updatable.
- [object UpdateCampaignRequest](./updatecampaignrequest.md)
  The payload properties to clear geotargeting from a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/campaign)*