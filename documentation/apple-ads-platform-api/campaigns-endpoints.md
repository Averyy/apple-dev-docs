# Campaigns Endpoints

**Framework**: Apple Ads Platform API

Create, retrieve, update, and delete campaigns using these endpoints.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

To promote iOS apps in the App Store or brands and locations on Apple Maps, use campaigns.

#### Use These Campaign Endpoints

The following endpoints create, retrieve, update, and delete campaigns, and return per-country limited-status details for legacy app campaigns:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/campaigns` | [`Create a Campaign`](post-campaigns.md) creates a new campaign. |
| `POST` | `/v1/campaigns/query` | [`Query Campaigns`](post-campaigns-query.md) retrieves campaigns matching the specified filters. |
| `GET` | `/v1/campaigns/{id}` | [`Get a Campaign`](get-campaigns-_id_.md) retrieves a single campaign by its ID. |
| `PUT` | `/v1/campaigns/{id}` | [`Update a Campaign`](put-campaigns-_id_.md) updates an existing campaign. |
| `DELETE` | `/v1/campaigns/{id}` | [`Delete a Campaign`](delete-campaigns-_id_.md) soft-deletes a campaign by its ID. |
| `GET` | `/v1/campaigns/{id}/legacy-app-limited-status-reason-details` | [`Get Legacy App Limited Status Reason Details`](get-campaigns-_id_-legacy-app-limited-status-reason-details.md) returns per-country limited-status reason details for a legacy app campaign. |

Both App Store ads and Apple Maps ads share the same campaign, ad group, and reporting infrastructure. They differ in `promotedObjectType`, creative requirements, and bid strategy options.

Every campaign is scoped to a single ad account and identifies its promoted object through two immutable fields set at creation: `promotedObjectType` and `promotedObjectId`. For App Store campaigns, `promotedObjectId` is the app’s `adamId`. For Apple Maps campaigns, it’s the brand’s unique identifier. Retrieve the brand identifier from [`Query Brands`](query-brands.md) or from `GET /v1/advertiser-resources?resourceType=BUSINESS_BRAND`. See [`Create a Campaign`](post-campaigns.md) for the required fields and payload examples for each campaign type.

The following table compares how App Store and Apple Maps campaigns differ:

|  | App Store | Apple Maps |
| --- | --- | --- |
| `promotedObjectType` | `APPSTORE_APP` | `BUSINESS_BRAND` |
| What is promoted | An iOS app | A brand and its business locations |
| `supplyPlacement` values | `APPSTORE_SEARCH_RESULTS`, `APPSTORE_TODAY_TAB`, `APPSTORE_SEARCH_TAB`, `APPSTORE_PRODUCT_PAGES` | `MAPS_SEARCH_RESULTS`, `MAPS_SEARCH_HOME` |
| `supplySource` values | `APPSTORE` | `MAPS` |
| Creative source | App Store product page (no upload required) | Brand assets uploaded via the Assets API |
| Bid strategy options | `MANUAL_CPT`, `MAX_CONVERSIONS` | `MAX_ENGAGEMENTS`, `MANUAL_CPT`, `MANUAL_CPM` |

An ad account’s `productFeatures` gate which campaign type it can create. An account authorized with `APPSTORE_APP_MANUAL` can only create App Store campaigns, and an account authorized with `BUSINESS_BRAND_MANUAL` can only create Apple Maps campaigns. See [`ProductFeatures`](productfeatures.md) for details.

##### Promote Apps

App Store campaigns (`promotedObjectType: APPSTORE_APP`) promote iOS apps across App Store placements. See [`CampaignTargeting`](campaigntargeting.md) for the full list of accepted App Store country or region and placement targeting values.

The app must be available for purchase, download, or preorder in the App Store and Apple Ads must be available in the targeted countries. To check eligibility before creating a campaign, use [`Check App Eligibility`](find-apps-eligibilities.md). After you confirm eligibility, see [`Create a Campaign`](post-campaigns.md) to create the campaign.

##### Promote Brands and Locations

Apple Maps campaigns (`promotedObjectType: BUSINESS_BRAND`) promote brands on Apple Maps. The brand must have `eligibility.status: ELIGIBLE` before a campaign can serve. The ad account must also have a `BUSINESS_BRAND` delegation linking it to the brand before campaigns can go live. See [`ProductFeatures`](productfeatures.md) for delegation requirements. The `billingEvent` can be `TAPS` (for `MANUAL_CPT` or `MAX_ENGAGEMENTS`) or `IMPRESSIONS` (for `MANUAL_CPM`).

See [`Ads on Apple Maps Endpoints`](brands-endpoints.md) for the full setup workflow, then see [`Create a Campaign`](post-campaigns.md) to create the campaign.

##### Choose a Bid Strategy

The `bidStrategy` object is always present on a campaign and controls how the campaign competes in auctions. It’s required at creation: you must send both `bidStrategyType` and `bidStrategyGoal`, and the goal must match the type. See [`BidStrategy`](bidstrategy.md) for the type/goal pairings.

Use the following table to match your goal to a `bidStrategyType` and `bidStrategyGoal` pair:

| If you want to… | Use `bidStrategyType` | With `bidStrategyGoal` | Campaign type |
| --- | --- | --- | --- |
| Set a fixed price per tap | `MANUAL_CPT` | `TAP` | App Store or Apple Maps |
| Set a fixed price per 1,000 impressions | `MANUAL_CPM` | `IMPRESSION` | Apple Maps only |
| Automatically optimize for installs | `MAX_CONVERSIONS` | `INSTALL` | App Store only |
| Automatically optimize for taps on your place card | `MAX_ENGAGEMENTS` | `TAP` | Apple Maps only |

A Maximize Conversions bid strategy (`MAX_CONVERSIONS`) maximizes the number of tap-through conversions at or near your target CPA. It uses a cost-per-tap pricing model and requires an automated ad group.

To switch a campaign’s bid strategy after creation, send an updated `bidStrategy` object with a matching `bidStrategyType`/`bidStrategyGoal` pair via [`Update a Campaign`](put-campaigns-_id_.md). See [`BidStrategyUpdate`](bidstrategyupdate.md) for the field-level mechanics. For reports with a Maximize Conversions bid strategy, see [`Campaigns Report`](get-app-campaign-reports.md) and [`Ad Groups Report`](get-app-ad-group-reports.md).

##### Manage Budget Orders

A budget order enforces a spending cap for a group of campaigns within an ad account. Campaigns assigned to the same budget order share a common spend limit via the `sharedBudgets` field. Budget orders are available to Apple Ads customers on monthly invoicing. A campaign with shared budget assignments also requires a `dailyBudget`. Both controls function independently: `dailyBudget` caps daily spending while each shared budget caps spending over its flight period.

See [`Budget Orders Endpoints`](budget-orders-endpoints.md) for details on creating and managing budget orders.

##### Monitor Campaign and System Status

Campaigns have three status fields and a bid strategy that together reflect their delivery state.

The `status` field captures the advertiser’s intent for the campaign to serve. Set it to `ENABLED` to allow the campaign to serve or `PAUSED` to stop delivery without deleting the campaign.

The `systemStatus` field is system-computed. A value of `RUNNING` means the campaign is active and eligible to serve, and `NOT_RUNNING` means a condition is preventing delivery.

The `displayStatus` field is system-computed and represents a rolled-up label that combines `status` and `systemStatus` into a single delivery state. It’s the same value that campaign reporting returns.

The `bidStrategy` object is always present on a campaign and is required at creation. See the Choose a Bid Strategy section above for details.

The following table lists what each `displayStatus` value means:

| `displayStatus` | Meaning |
| --- | --- |
| `RUNNING` | The campaign is actively delivering ads. |
| `PAUSED` | The advertiser paused the campaign. |
| `ON_HOLD` | A system or account condition stops delivery. |
| `LIMITED` | The campaign is serving at reduced capacity. |
| `PROCESSING` | The system recently created or modified the campaign and is still processing it. |
| `DELETED` | The advertiser soft-deleted the campaign. |

When `systemStatus` is `NOT_RUNNING`, the system populates the `systemStatusReasons` array with one or more [`CampaignSystemStatusReason`](campaignsystemstatusreason.md) values explaining why. Reasons include scheduling, app or brand eligibility, budget exhaustion, payment issues, and ad group state, among others.

When a campaign is running but delivering at reduced capacity, the system populates the `systemStatusLimitingReasons` array with one or more [`CampaignSystemLimitedStatusReason`](campaignsystemlimitedstatusreason.md) values. These don’t stop delivery. They indicate conditions that constrain reach or impression volume.

To filter campaigns by status, see [`Query Campaigns`](post-campaigns-query.md).

> **Note**: The `cpaCap` field on ad groups is deprecated. Configure conversion targeting via the `bidStrategy` object using `bidStrategyType: MAX_CONVERSIONS`.

##### Continue Building Campaign Delivery

Once a campaign exists, continue building out its delivery: create [`Ad Groups Endpoints`](adgroups-endpoints.md) to configure targeting and bid strategy, add [`Managing Keywords and Negative Keywords`](keywords-and-negative-keywords.md) for App Store search campaigns, and create [`Ads Endpoints`](ads-endpoints.md) to serve within each ad group.

## Topics

- [Create a Campaign](post-campaigns.md)
  Create a new advertising campaign with a promoted object, budget, targeting, and bid strategy configuration.
- [Query Campaigns](post-campaigns-query.md)
  Query campaigns using filters, sorting, and pagination.
- [Get a Campaign](get-campaigns-_id_.md)
  Retrieve a single campaign by its unique identifier.
- [Update a Campaign](put-campaigns-_id_.md)
  Update a campaign’s name, status, budget, targeting, or bid strategy.
- [Delete a Campaign](delete-campaigns-_id_.md)
  Soft-delete a campaign by its unique identifier, cascading to its ad groups, keywords, and ads.
- [Get Legacy App Limited Status Reason Details](get-campaigns-_id_-legacy-app-limited-status-reason-details.md)
  Return a map of country or region codes to their associated limited-status reason for legacy app campaigns.

## See Also

- [Campaigns Data Objects](campaigns-data-objects.md)
  Reference the request and response schemas for creating, retrieving, and updating campaigns.
- [Campaigns Data Types](campaign-data-types.md)
  Look up the enumerated values and scalar types used across campaign fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaigns-endpoints)*