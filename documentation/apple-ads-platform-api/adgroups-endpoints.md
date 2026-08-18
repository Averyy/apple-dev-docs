# Ad Groups Endpoints

**Framework**: Apple Ads Platform API

Create, retrieve, update, and delete ad groups.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

An ad group is the organizational unit within a campaign that groups a set of ads sharing the same targeting, bid strategy, and schedule. Ad groups let you run multiple targeting configurations or bid strategies side by side under the same campaign, without duplicating the campaign itself.

A [`Campaign`](campaign.md) must already exist before you can create an ad group. You create every ad group with a `campaignId` referencing its parent campaign, and it defines targeting, bid strategy, and scheduling for a set of ads within that campaign. You configure bid strategy via [`BidStrategy`](bidstrategy.md), using a matched [`BidStrategyType`](bidstrategytype.md) and [`BidStrategyGoal`](bidstrategygoal.md) pair. Ad group behavior varies by the campaign’s `promotedObjectType`.

##### Target App Store Ad Groups

App Store (`APPSTORE_APP`) ad groups support the following targeting dimensions, including audience targeting (device class, age, gender, app category, and app downloader), [`Geo Targeting Endpoints`](geo-targeting-endpoints.md) (country, admin area, and locality), daypart, and keyword targeting. Manage your own keyword list with explicit bid amounts, or use the Search Match feature (`automatedKeywordsOptIn: true`) to automatically match search queries. When you don’t provide a keyword-level bid, the ad group’s `bidStrategy` bid applies.

##### Target Apple Maps Ad Groups

Apple Maps (`BUSINESS_BRAND`) ad groups support the following targeting dimensions, including geo targeting (admin area, locality, and postal code), [`Managing Location Groups`](location-groups-overview.md) (location groups, or radius, used with `MAPS_SEARCH_RESULTS`), and daypart. You can add keyword phrases and keyword categories for Search Results placement. Keyword bids don’t apply to ad groups that use location groups.

For full targeting mode details and payload examples, see [`Create an Ad Group`](post-adgroups.md).

#### Use These Endpoints

Use these endpoints to create, retrieve, update, and delete ad groups:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/adgroups` | [`Create an Ad Group`](post-adgroups.md) creates a new ad group within a campaign. |
| `POST` | `/v1/adgroups/query` | [`Query Ad Groups`](post-adgroups-query.md) retrieves ad groups matching the specified filters. |
| `GET` | `/v1/adgroups/{id}` | [`Get an Ad Group`](get-adgroups-_id_.md) retrieves a single ad group by its ID. |
| `PUT` | `/v1/adgroups/{id}` | [`Update an Ad Group`](put-adgroups-_id_.md) updates an existing ad group. |
| `DELETE` | `/v1/adgroups/{id}` | [`Delete an Ad Group`](delete-adgroups-_id_.md) soft-deletes an ad group by its ID. |

##### Build a Campaign Keywords Strategy

When building a campaign promotion strategy, you define keywords relevant to your app and bid on them. Relevant keywords increase the viability of your app to rank high in user searches. You can either automate your keyword and bid strategy by using the Search Match feature, or use your own keywords and bid strategy.

The Search Match feature is an algorithm that uses multiple resources to match your ad to relevant searches in the App Store. The resources include metadata from your App Store product page, information about similar apps in the same genre, and other available search data. Search Match is a good option if you don’t want to figure out all keyword possibilities and actively bid on them.

##### Enable and Disable Search Match

To enable Search Match, use [`Create an Ad Group`](post-adgroups.md) or [`Update an Ad Group`](put-adgroups-_id_.md) endpoints to perform the following steps:

1. Set `automatedKeywordsOptIn: true`.
2. Set `bidStrategy` with the desired strategy type and goal.
3. Leave keyword fields empty. Search Match automatically identifies and targets relevant search queries.
4. Submit the request to apply the configuration.

Use `automatedKeywordsOptIn` or your own keywords, not both, on the same ad group. Enabling Search Match on an ad group that already has keywords doesn’t delete them, but avoid combining Search Match with manually targeted keywords. Choose one strategy per ad group.

If you’re using your own keywords and bid strategy, disable Search Match with the [`Create an Ad Group`](post-adgroups.md) or [`Update an Ad Group`](put-adgroups-_id_.md) endpoints by following these steps:

1. Set `automatedKeywordsOptIn: false`.
2. Set `bidStrategy` with the desired strategy type and goal.
3. Add your own keywords using the [`Create a Keyword`](post-keywords.md) or [`Update a Keyword`](put-keywords-_id_.md) endpoints.
4. Set `Keyword.bid` on each keyword to specify the per-keyword bid amount.

> ❗ **Important**: Keywords without an explicit `Keyword.bid` value use the campaign-level bid strategy settings.

##### Automate Ad Groups with Maximize Conversions

The Maximize Conversions bid strategy uses an automated ad group with Search Match to automatically optimize bids for each search query. This eliminates the need to manually set and monitor individual keyword bids, while prioritizing keywords most likely to drive conversions.

To create a campaign with a Maximize Conversions bid strategy, see the payload example in [`Create a Campaign`](post-campaigns.md).

To set `bidStrategy` on ad group creation, see [`Create an Ad Group`](post-adgroups.md) and [`BidStrategyCreate`](bidstrategycreate.md). To echo an existing auto-bidding campaign’s strategy on an update, see the “Echo Auto-Bidding Strategy” example in [`Update an Ad Group`](put-adgroups-_id_.md).

For details on switching between [`Campaigns Endpoints`](campaigns-endpoints.md) and manual campaigns, see the payload examples in [`Update a Campaign`](put-campaigns-_id_.md).

For reports with a Maximize Conversions bidding strategy, see campaign and ad group [`Campaigns Report`](get-app-campaign-reports.md) and [`Ad Groups Report`](get-app-ad-group-reports.md).

##### Configure Daypart Targeting

Daypart targeting restricts ad delivery to specific hour slots within a 7-day week. The API represents the week as a flat grid of 168 integer slots (0 through 167), starting at Sunday midnight. Slot 0 is Sunday 12:00 a.m., slot 1 is Sunday 1:00 a.m., and so on through slot 167 (Saturday 11:00 p.m.).

Configure daypart targeting via the `targeting.daypart` field on an ad group. Pass a `TargetingData` object with an `include` array of slot integers to restrict delivery to those hours. Daypart targeting is include-only.

Daypart targeting applies across ad group creation and updates. Use [`Create an Ad Group`](post-adgroups.md) to set the initial window, and [`Update an Ad Group`](put-adgroups-_id_.md) to adjust the schedule without recreating the ad group. Changes take effect at the start of the next eligible hour slot.

The system evaluates all slot values in the ad account’s configured time zone. Daypart targeting supports only the `APPSTORE_SEARCH_RESULTS` placement for App Store ad groups, and only the `MAPS_SEARCH_RESULTS` placement for Apple Maps ad groups.

For the include structure, see [`AdGroupTargeting`](adgrouptargeting.md).

##### Follow Apple Maps Ad Group Constraints

Ad groups for Maps campaigns (`BUSINESS_BRAND`) attach a location group via `targeting.locationGroup` to control which of the advertiser’s business locations the ad group promotes. For how to create and manage location groups, see [`Managing Location Groups`](location-groups-overview.md). Key constraints:

- The `pricingModel` must match the campaign `billingEvent`: `CPT` for `TAPS`, `CPM` for `IMPRESSIONS`.
- You can’t combine radius and geo location targeting modes within a single ad group.
- In practice, you use radius targeting with `MAPS_SEARCH_RESULTS` campaigns. The `radius` field is a generic string array in the schema, with no enumerated values or campaign-type restriction.
- Daypart targeting supports only the `MAPS_SEARCH_RESULTS` placement on Maps ad groups.

See [`Create an Ad Group`](post-adgroups.md) for full targeting mode details and payload examples.

##### Track Ad Group Status and System Status

Ad groups have three status fields that together determine whether the ad group is delivering:

- The `status` field captures the advertiser’s intent for the ad group to serve: `ENABLED` or `PAUSED`.
- The `systemStatus` field is system-computed. A value of `RUNNING` means the ad group is active and eligible to serve, and `NOT_RUNNING` means a condition is blocking delivery.
- The `displayStatus` field is system-computed and represents a rolled-up label combining `status` and `systemStatus` into a single delivery state. See [`AdGroupDisplayStatus`](adgroupdisplaystatus.md) for all values.

When `systemStatus` is `NOT_RUNNING`, the system populates `systemStatusReasons` with one or more [`AdGroupSystemStatusReason`](adgroupsystemstatusreason.md) values; see [`AdGroupSystemStatusReason`](adgroupsystemstatusreason.md) for the full list. When an ad group is running but delivering at reduced capacity, the system populates `systemStatusLimitingReasons` with one or more [`AdGroupSystemLimitedStatusReason`](adgroupsystemlimitedstatusreason.md) values. These reasons don’t stop delivery; see [`AdGroupSystemLimitedStatusReason`](adgroupsystemlimitedstatusreason.md) for the full list.

## Topics

- [Create an Ad Group](post-adgroups.md)
  Create a new ad group within a campaign, defining targeting, bid strategy, and scheduling for a set of ads.
- [Query Ad Groups](post-adgroups-query.md)
  Query ad groups using filters, sorting, and pagination.
- [Get an Ad Group](get-adgroups-_id_.md)
  Retrieve a single ad group by its unique identifier.
- [Update an Ad Group](put-adgroups-_id_.md)
  Update an existing ad group’s name, status, bid strategy, targeting, or scheduling.
- [Delete an Ad Group](delete-adgroups-_id_.md)
  Soft-delete an ad group by its unique identifier, along with all ads and keywords associated with it.

## See Also

- [Ad Groups Data Objects](adgroups-data-objects.md)
  Reference the request and response objects for ad group endpoints.
- [Ad Groups Data Types](adgroups-data-types.md)
  Reference the enumerations and scalar types for ad groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroups-endpoints)*