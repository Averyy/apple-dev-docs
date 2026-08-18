# Advertising Your App on the App Store

**Framework**: Apple Ads Platform API

Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

You can promote your app on the App Store in four placements, as detailed in the table below: search results, the Search tab, the Today tab, and Product Pages. Every App Store campaign uses `promotedObjectType: APPSTORE_APP`.

| Placement | Where it appears |
| --- | --- |
| **Search results** | Search results ads can appear at the top of the results or further down the page. |
| **Search tab** | Appears prominently at the top of the suggested apps list on the Search tab. |
| **Today tab** | Where users start their journey on the App Store. |
| **Product Pages** | Product Pages ads appear across the App Store, reaching people while they’re viewing other apps, whether their journey started on the App Store or from an outside link. |

Before you begin:

- Every API call requires a valid Bearer token. Complete the OAuth setup in [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md) before proceeding.
- Your ad account must have `productFeatures: ["APPSTORE_APP_MANUAL"]` and a `CONTENT_PROVIDER` delegation with the CPID as `resourceId` to create App Store campaigns. Both must be in place before campaigns can go live. For full delegation requirements, see [`ProductFeatures`](productfeatures.md).
- For `ad-account-scoped` operations, also include the `X-AP-Context` header. For the full header reference and a request example, see [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md).
- When automating campaign, creative, or keyword operations at scale, watch the rate-limit headers described in [`Applying Rate Limits`](rate-limits.md) and back off before hitting a `429`.
- See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on the request structure and common query patterns.

#### Confirm Your Organization and Ad Account

Start by confirming which organization and ad account you’re working under. [`Get User ACL`](get-user-acls.md) returns the ad accounts and roles available to your token, as shown here:

```console
GET https://api.ads.apple.com/v1/acls
```

For each ad account, [`Get Ad Account by ID`](get-ad-accounts-_id_.md), shown below, returns full ad account details including currency, time zone, and payment model, all of which you need when creating campaigns and interpreting reports.

```console
GET https://api.ads.apple.com/v1/ad-accounts/{adAccountId}
```

Confirm the `productFeatures` and `CONTENT_PROVIDER` delegation mentioned above are present on this ad account. To update an ad account’s delegations, use [`Update Ad Accounts`](put-ad-accounts-_id_.md). The `delegations` field uses full-replacement semantics: a partial array removes unlisted entries, so always send the complete desired state.

#### Choose Your App

To search the App Store catalog for your app and retrieve its Adam ID, use [`Search for Apps`](searches-for-a-list-of-apps.md). The Adam ID is the `promotedObjectId` you set on every App Store campaign.

```console
GET https://api.ads.apple.com/v1/search/apps
```

To retrieve full metadata (display name, category, supported device classes, and `availableStorefronts`), use [`Get App Details by Adam ID`](get-app-details-by-adam-id.md), like this:

```console
GET https://api.ads.apple.com/v1/apps/{adamId}
```

Check `availableStorefronts` to confirm which App Store countries or regions you can target before setting campaign targets. See [`Search Apps Endpoints`](search-apps-endpoints.md) for more information.

#### Verify Your App Is Eligible to Advertise

To confirm your app’s advertising eligibility status before you build a campaign, use [`Check App Eligibility`](find-apps-eligibilities.md). Pass your app’s Adam ID to check which placements and App Store countries or regions are available, as shown here:

```json
POST /v1/eligibilities/apps/query

{
  "filters": [
    {
      "field": "adamId",
      "operator": "EQUALS",
      "value": 123456789
    }
  ]
}
```

For eligibility states and per-placement details, see [`App Eligibility Endpoints`](app-eligibility-endpoints.md).

#### Choose Placements and App Store Countries or Regions

Before creating the campaign, select where you want your ads to run on the App Store (Today tab, Search tab, search results, or product pages) and choose one or more App Store countries or regions for the campaign to run.

There are three campaign-level targeting dimensions, described in the table below:

| Field | What it controls |
| --- | --- |
| `supplySource` | The ad channel. For all App Store campaigns, set this to `APPSTORE`. |
| `supplyPlacement` | The specific App Store placement where the ad appears. |
| `countryOrRegion` | The App Store countries or regions where the campaign is eligible to serve, using ISO 3166-1 alpha-2 codes. |

App Store campaigns support the four placements described below:

| Value | Placement | When to use |
| --- | --- | --- |
| `APPSTORE_SEARCH_RESULTS` | Search results | Reach users who search for something specific. Can appear in one of two places in App Store search results: at the top of search results or further down in search results. Supports keyword targeting at the ad group level. |
| `APPSTORE_SEARCH_TAB` | Search tab | Reach users before they search for something specific, with an ad that appears prominently at the top of the suggested apps list on the Search tab. |
| `APPSTORE_TODAY_TAB` | Today tab | Where users start their journey on the App Store. |
| `APPSTORE_PRODUCT_PAGES` | Product pages | Reach users while they’re viewing other apps on pages across the App Store. |

Set `countryOrRegion.include` using the `availableStorefronts` list you retrieved earlier when choosing your app, as shown below. Only include App Store countries or regions where your app is available for download or purchase.

```json
"targeting":
{
  "supplySource": {
    "include": [
      "APPSTORE"
    ]
  },
  "supplyPlacement": {
    "include": [
      "APPSTORE_SEARCH_RESULTS"
    ]
  },
  "countryOrRegion": {
    "include": [
      "US"
    ]
  }
}
```

#### Create a Campaign

This example creates an `APPSTORE_SEARCH_RESULTS` placement campaign:

```json
POST /v1/campaigns

{
  "name": "AwayFinder - Brand Keywords - US",
  "adAccountId": 123456789,
  "billingEvent": "TAPS",
  "promotedObjectType": "APPSTORE_APP",
  "promotedObjectId": "123456789",
  "dailyBudget": {
    "value": { "amount": "100.00", "currency": "USD" }
  },
  "targeting": {
    "countryOrRegion": { "include": ["US"] },
    "supplyPlacement": { "include": ["APPSTORE_SEARCH_RESULTS"] }
  },
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP"
  },
  "status": "ENABLED"
}
```

#### Create an Ad Group

Ad groups sit under a campaign and control targeting, scheduling, and bidding. Create one with [`Create an Ad Group`](post-adgroups.md), supplying the `campaignId` from the previous step. App Store ad groups support audience targeting (device class, age, gender, app category, and app downloader), geo targeting (country, admin area, and locality), daypart, and keyword targeting. For a full description, see [`Ad Groups Endpoints`](adgroups-endpoints.md).

```json
POST /v1/adgroups

{
  "campaignId": 542317095,
  "name": "AwayFinder - Brand Keywords - US",
  "pricingModel": "CPT",
  "bidStrategy": {
    "bidStrategyType": "MANUAL_CPT",
    "bidStrategyGoal": "TAP",
    "bid": { "amount": "1.00", "currency": "USD" }
  },
  "status": "ENABLED",
  "startTime": "2026-01-01T00:00:00.000",
  "endTime": "2026-03-31T23:59:59.999"
}
```

#### Add Keywords

To add keywords to an ad group for Search results placement, use [`Create a Keyword`](post-keywords.md) or [`Bulk Create Keywords`](post-keywords-bulk-create.md). `matchType` is `BROAD` or `EXACT`, as shown in the example below. An optional per-keyword bid overrides the ad group default. For the full match type reference, see [`KeywordMatchType`](keywordmatchtype.md).

```json
POST /v1/keywords/bulk-create

{
  "items": [
    {
      "correlationId": 1,
      "data": {
        "adGroupId": 542370539,
        "text": "travel app",
        "matchType": "BROAD",
        "bid": {
          "amount": "1.25",
          "currency": "USD"
        },
        "status": "ENABLED"
      }
    },
    {
      "correlationId": 2,
      "data": {
        "adGroupId": 542370539,
        "text": "flight tracker",
        "matchType": "EXACT",
        "bid": {
          "amount": "1.50",
          "currency": "USD"
        },
        "status": "ENABLED"
      }
    }
  ]
}
```

If you’re not sure which keywords to add, use [`Query Keyword Suggestions`](query-keyword-suggestions.md) to discover terms related to your app’s category and [`Query Phrase Suggestions`](query-phrase-suggestions.md) to explore broader phrase ideas.

#### Exclude Irrelevant Traffic with Negative Keywords

Negative keywords prevent your ads from showing for unrelated searches. Apply them at two levels:

- Campaign-level negatives apply across all ad groups. Set `campaignId`, omit `adGroupId`.
- Ad group-level negatives apply to a single ad group. Set `adGroupId`, omit `campaignId`.

You can add negative keywords with [`Create a Negative Keyword`](post-negative-keywords.md), as shown below. For large exclusion lists, you can use bulk creation via [`Bulk Create Negative Keywords`](post-negative-keywords-bulk-create.md). See [`Managing Keywords and Negative Keywords`](keywords-and-negative-keywords.md) for scoping rules and match type behavior.

```json
POST /v1/negative-keywords

{
  "adGroupId": 542370539,
  "text": "free",
  "matchType": "BROAD",
  "status": "ENABLED"
}
```

#### Create a Creative and an Ad

First, create the creative with [`Create an Ad Creative`](post-creatives.md) using `creativeType: DEFAULT_PRODUCT_PAGE`, as the example below demonstrates. You also need `destination.parameters.adamId`, which should match the `promotedObjectId` you set when creating the campaign.

```json
POST /v1/creatives

{
  "name": "AwayFinder - Default Product Page",
  "creativeType": "DEFAULT_PRODUCT_PAGE",
  "creativeSpec": {},
  "destination": {
    "destinationType": "APP_STORE_PRODUCT_PAGE",
    "parameters": {
      "adamId": "123456789"
    }
  }
}
```

The response’s `result.id` is the `creativeId` you reference below. Create the ad with [`Create an Ad`](post-ads.md), and link it to the ad group and creative.

```json
POST /v1/ads

{
  "adGroupId": 542370539,
  "creativeId": 666777888,
  "name": "Default Search Ad",
  "status": "ENABLED"
}
```

To use a custom product page instead of the default, first retrieve available pages with [`Query Product Pages`](query-product-pages.md), then set `creativeType: CUSTOM_PRODUCT_PAGE` and pass the chosen `productPageId` alongside `adamId` in the creative’s `destination.parameters`. For more information on fetching page IDs and locale details, see [`Product Pages Endpoints`](product-pages-endpoints.md). For the full creative workflow, see [`Creatives Endpoints`](creatives-endpoints.md).

#### Pull Campaign Performance Reports

After your campaign is live, you can retrieve performance data with [`Campaigns Report`](get-app-campaign-reports.md). All report calls follow the same `POST /query` structure with a required `timeRange` as shown below:

```json
POST /v1/reports/apps/campaigns/query

{
  "timeRange": {
    "start": "2026-01-01",
    "end": "2026-01-31",
    "timeZone": "UTC",
    "granularity": "DAILY"
  },
  "filters": [
    { "field": "campaignId", "operator": "EQUALS", "value": 542317095 }
  ]
}
```

Search term reports show the actual queries that triggered your ads, so you can use them to discover new keyword opportunities and build out your [`Managing Keywords and Negative Keywords`](keywords-and-negative-keywords.md) list. To understand which keywords and creatives are driving results, drill deeper with [`Ad Groups Report`](get-app-ad-group-reports.md), [`Keywords Report`](get-app-keyword-reports.md), and [`Search Terms Report`](get-app-search-term-reports.md).

#### Optimize Your Campaigns

With a campaign running and data flowing, you’re ready to optimize in the following ways:

- To act on automated suggestions, use [`Query Daily Budget Recommendations`](query-daily-budget-recommendations.md).
- To understand how often your ads win auctions versus competitors, use [`Impression Share Query`](query-app-impression-share-data.md).
- To identify trending search terms in your category, use [`Search Term Popularity Query`](query-app-search-term-popularity-data.md).
- Scale keyword changes with [`Bulk Update Keywords`](post-keywords-bulk-update.md). To remove a keyword, use the single-item [`Delete a Keyword`](delete-keywords-_id_.md) endpoint. When looping over many campaigns or ad groups, watch the rate-limit headers described in [`Applying Rate Limits`](rate-limits.md) and back off before hitting a `429`.

## See Also

- [Implementing OAuth for the Apple Ads Platform API](implementing-oauth-for-the-apple-ads-platform-api.md)
  Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.
- [Calling the Apple Ads Platform API](calling-apple-ads-platform-api.md)
  Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.
- [Using Client Libraries](client-libraries.md)
  Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.
- [Applying Rate Limits](rate-limits.md)
  Track your remaining quota and pace requests.
- [Advertising Your Business on Apple Maps](journey-apple-maps-brand-ads.md)
  Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/journey-app-store-ads)*