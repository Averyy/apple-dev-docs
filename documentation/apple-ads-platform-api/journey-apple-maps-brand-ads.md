# Advertising Your Business on Apple Maps

**Framework**: Apple Ads Platform API

Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

You can promote ads on Apple Maps across two placements: Search results and Search home. Every Maps campaign uses `promotedObjectType: BUSINESS_BRAND`. For the full endpoint reference, see [`Ads on Apple Maps Endpoints`](brands-endpoints.md).

Before you begin:

- Ads on Apple Maps require an Apple Ads profile and a validated brand in Apple Ads.
- Your ad account must have `productFeatures: ["BUSINESS_BRAND_MANUAL"]` and a `BUSINESS_BRAND` delegation to create Maps campaigns.
- All API calls require a `Bearer` token as described in [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md) and [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md).
- All ad-account-scoped calls also require the `X-AP-Context: adAccountId` header.
- When automating campaign, creative, or location group operations at scale, watch the rate-limit headers described in [`Applying Rate Limits`](rate-limits.md) and back off before hitting a `429`.
- For full delegation requirements, see [`ProductFeatures`](productfeatures.md).

#### Identify Your Brand

Retrieve your brand with [`Query Brands`](query-brands.md), as shown below. The response returns the brand `id` you use as the `promotedObjectId` throughout campaign creation.

```json
POST /v1/business-brands/query

{
  "filters": [
    {
      "field": "eligibility.status",
      "operator": "EQUALS",
      "value": "ELIGIBLE"
    }
  ]
}
```

To fetch a single brand’s full details, use [`Get Brand by ID`](get-brand-by-id.md). A brand must have `eligibility.status: ELIGIBLE` before you can use it in an active campaign.

#### Upload Creative Assets

Ads on Apple Maps can use image assets. Use [`Upload Asset`](upload-asset.md) to upload an image file. The response returns an `assetId` you can use in the ad creative, as shown here:

```json
POST /v1/assets/upload

{
  "file": "hero.png",
  "promotedObjectId": "9876543",
  "promotedObjectType": "BUSINESS_BRAND"
}
```

After upload is complete, use [`Query Assets`](query-assets.md) to list and filter your asset library by status, type, or brand, and use [`Get Asset`](get-asset-by-id.md) to inspect a specific asset’s processing state. Assets must reach `ELIGIBLE` (`eligibility.status`) before you can use them in a creative.

#### Build Location Groups

Location groups organize the business locations you want to promote together under an ad group, rather than requiring you to set each location individually. Create a location group with [`Create Location Group`](create-location-group.md) by supplying the required `adAccountId`, `brandId`, `groupType`, and a list of location IDs for `STATIC` groups, as shown here:

```json
POST /v1/location-groups

{
  "name": "AwayFinder - West Coast Stores",
  "adAccountId": "293897290",
  "brandId": "9876543",
  "groupType": "STATIC",
  "locationIds": [
    "1001",
    "1002",
    "1003"
  ]
}
```

Notes when creating location groups:

- A group with a fixed, manually curated list of location IDs reaches `systemStatus: VALID` immediately.
- `DYNAMIC` groups use rule-based criteria to automatically include matching locations and start with `systemStatus: PENDING` while Apple Ads evaluates the rules against the brand’s locations. Wait for `systemStatus: VALID` before referencing a `DYNAMIC` group in ad group targeting.
- To find valid location IDs, query [`Query for Locations`](query-locations.md), which returns Apple Ads locations for a brand and filters by country, name, or status.

For more information, see [`Managing Location Groups`](location-groups-overview.md).

- To list existing groups, use [`Query Location Groups`](query-location-groups.md). To add or remove locations over time, use [`Update Location Group`](update-location-group.md).

#### Choose Placements and Markets

Before creating the campaign, select where you want your ads to run on Apple Maps, and choose one or more markets for the campaign. These choices populate the [`CampaignTargetingCreate`](campaigntargetingcreate.md) object. Here are the fields that control placement and market:

| Field | What it controls |
| --- | --- |
| `supplySource` | The ad channel. For all Apple Maps campaigns, set this to `MAPS`. |
| `supplyPlacement` | The specific Apple Maps placement where the ad appears. |
| `countryOrRegion` | The markets where the campaign is eligible to serve, using ISO 3166-1 alpha-2 codes. |

Apple Maps campaigns support two placements:

| Value | Placement | Notes |
| --- | --- | --- |
| `MAPS_SEARCH_RESULTS` | Search results | Reaches people after they search for something specific and supports radius targeting at the ad group level. See [`AdGroupTargeting`](adgrouptargeting.md). |
| `MAPS_SEARCH_HOME` | Search home | Reaches people at the top of the Suggested Places list, before they search. |

You can include both placement values in a single campaign, or create separate campaigns per placement for independent budget control and reporting. The brand you identified earlier includes a `countryOrRegion` field indicating the markets where the brand is eligible. Set `countryOrRegion.include` to the subset of those markets this campaign should target, like this:

```json
"targeting":
{
  "supplySource": {
    "include": [
      "MAPS"
    ]
  },
  "supplyPlacement": {
    "include": [
      "MAPS_SEARCH_RESULTS"
    ]
  },
  "countryOrRegion": {
    "include": [
      "US"
    ]
  }
}
```

After creation, all three dimensions remain mutable and you can update them via [`CampaignTargeting`](campaigntargeting.md).

#### Create an Apple Maps Campaign

You can create a campaign with [`Create a Campaign`](post-campaigns.md), like this:

```json
POST /v1/campaigns

{
  "name": "AwayFinder - West Coast Brand - Q1",
  "adAccountId": 293897290,
  "billingEvent": "TAPS",
  "promotedObjectType": "BUSINESS_BRAND",
  "promotedObjectId": "9876543",
  "dailyBudget": {
    "value": { "amount": "200.00", "currency": "USD" }
  },
  "targeting": {
    "supplySource": { "include": ["MAPS"] },
    "supplyPlacement": { "include": ["MAPS_SEARCH_RESULTS"] }
  },
  "bidStrategy": {
    "bidStrategyType": "MAX_ENGAGEMENTS",
    "bidStrategyGoal": "TAP"
  },
  "status": "ENABLED"
}
```

#### Create an Ad Group with Location Targeting

Create an ad group under your Apple Maps campaign with [`Create an Ad Group`](post-adgroups.md). Apple Maps ad groups support admin area, locality, postal code, location group, radius, and daypart targeting. You can add keyword phrases and keyword categories for the Search results placement, as shown below, though keyword bids don’t apply to ad groups that use location groups.

For a full description of targeting dimensions, see [`Ad Groups Endpoints`](adgroups-endpoints.md). Reference the location group IDs from the previous step in the `targeting.locationGroup` field to restrict delivery to your chosen locations. This ad group’s `bidStrategy` matches the `MAX_ENGAGEMENTS` / `TAP` pairing you set on the campaign.

```json
POST /v1/adgroups

{
  "campaignId": 542317099,
  "name": "AwayFinder - West Coast Locations",
  "pricingModel": "CPT",
  "bidStrategy": {
    "bidStrategyType": "MAX_ENGAGEMENTS",
    "bidStrategyGoal": "TAP"
  },
  "targeting": {
    "locationGroup": {
      "include": ["LG-77001"]
    }
  },
  "status": "ENABLED"
}
```

#### Create a Creative

A creative ties together an asset, promotional text, and the destination (always the Apple Maps place card) into the ad unit shown in Apple Maps. You can create one with [`Create an Ad Creative`](post-creatives.md), referencing the brand and the asset IDs from the previous steps, like this:

```json
POST /v1/creatives

{
  "name": "AwayFinder - Summer Promo - Logo Banner",
  "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
  "creativeSpec": {
    "brandId": "9876543",
    "creativeSubtype": "BUSINESS_ASSET",
    "creativeAssets": [
      { "assetId": "770e8400-e29b-41d4-a716-446655440002" }
    ],
    "localizedText": {
      "en-US": { "promoText": "Visit us today for special offers!" }
    },
    "defaultLocale": "en-US"
  },
  "destination": {
    "destinationType": "LOCAL_ADS_PLACECARD"
  }
}
```

To audit your creative library, use [`Query Ad Creatives`](post-creatives-query.md) and [`Get an Ad Creative`](get-creatives-_id_.md). Creatives go through a review process. If Apple Ads doesn’t approve a creative, [`Query Rejection Reasons for Brands`](query-policy-assignments-(rejection-reasons)-for-external-consumers.md) returns rejection reason details.

#### Create an Ad Linking a Creative and an Ad Group

With the creative and ad group ready, create the ad with [`Create an Ad`](post-ads.md) to connect them, as in the code below. Ads for Apple Maps campaigns reference the creative ID you got from the Create a Creative section above.

```json
POST /v1/ads

{
  "adGroupId": 542317200,
  "creativeId": 666777888,
  "name": "Summer Promo Ad",
  "status": "ENABLED"
}
```

#### Pull Apple Maps Campaign Reports

Apple Maps campaigns use the `business-brands` promoted object type in all report endpoints. You can retrieve campaign-level performance with [`Campaigns Report (Brands)`](get-brand-campaign-reports.md) and drill into ad group or creative performance as needed, like this:

```json
POST /v1/reports/business-brands/campaigns/query

{
  "timeRange": {
    "start": "2026-01-01",
    "end": "2026-01-31",
    "timeZone": "ORTZ",
    "granularity": "DAILY"
  },
  "filters": [
    { "field": "campaignId", "operator": "EQUALS", "value": 542317099 }
  ]
}
```

Apple Maps campaigns don’t have a dedicated location-level report endpoint. Instead, you can group or filter any of the five `business-brands` report endpoints (`campaigns`, `adgroups`, `ads`, `keywords`, `searchterms`) by `locationId` to see performance broken down by individual map location. For deeper funnel analysis, use [`Ad Groups Report (Brands)`](get-brand-ad-group-reports.md), [`Ads Report (Brands)`](get-brand-ad-reports.md), [`Keywords Report (Brands)`](get-brand-keyword-reports.md), and [`Search Terms Report (Brands)`](get-brand-search-term-reports.md).

#### Optimize Campaigns

With Apple Maps campaigns running, you can:

- Audit your asset library over time with [`Query Assets`](query-assets.md) and replace underperforming creatives.
- Add keywords to ad groups with [`Create a Keyword`](post-keywords.md) for the Search results placement within Maps.
- Audit any changes made to campaigns or creatives using [`Query Change History`](query-audit-summary-_-grouped-by-transaction.md).

## See Also

- [Implementing OAuth for the Apple Ads Platform API](implementing-oauth-for-the-apple-ads-platform-api.md)
  Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.
- [Calling the Apple Ads Platform API](calling-apple-ads-platform-api.md)
  Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.
- [Using Client Libraries](client-libraries.md)
  Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.
- [Applying Rate Limits](rate-limits.md)
  Track your remaining quota and pace requests.
- [Advertising Your App on the App Store](journey-app-store-ads.md)
  Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/journey-apple-maps-brand-ads)*