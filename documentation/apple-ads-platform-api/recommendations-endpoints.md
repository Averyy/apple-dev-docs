# Recommendations Endpoints

**Framework**: Apple Ads Platform API

Endpoints for querying, applying, and dismissing budget and Target CPA recommendations.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

The Recommendations API returns recommendations for target CPA adjustments and daily budget increases to help you improve your campaigns’ performance. Unlike [`Suggestions Endpoints`](suggestions-endpoints.md), recommendations are stateful; each one has a lifecycle you apply or dismiss, and the system tracks the outcome. For historical performance metrics, see [`Managing Reports`](reports.md). For market-level signals like impression share, see [`Insights Endpoints`](insights-endpoints.md).

#### Explore the Available Endpoints

The API scopes recommendations to a promoted object, either an app or a brand, that you identify by `promotedObjectId` and `promotedObjectType`. For `promotedObjectId`, use the app Adam ID when `promotedObjectType` is `APPSTORE_APP` and the brand ID when it is `BUSINESS_BRAND`. Use `campaignId` as an optional filter to narrow results to a specific campaign.

For Apple Maps (`BUSINESS_BRAND`) campaigns, only daily budget recommendations are available. Target CPA recommendations apply to App Store (`APPSTORE_APP`) campaigns using a Maximize Conversions bid strategy, which relies on Search Match within the Search results placement.

The following endpoints let you query, apply, and dismiss recommendations:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/recommendations/daily-budgets/query` | Returns daily budget recommendations using [`Query Daily Budget Recommendations`](query-daily-budget-recommendations.md). Recommends an increased daily budget for campaigns that may have more opportunities, and includes historical and expected performance metrics. |
| `POST` | `/v1/recommendations/daily-budgets/apply` | Applies a daily budget recommendation using [`Apply Daily Budget Recommendations`](apply-daily-budget-recommendations.md) and updates the campaign’s daily budget. |
| `POST` | `/v1/recommendations/daily-budgets/dismiss` | Dismisses a daily budget recommendation using [`Dismiss Daily Budget Recommendations`](dismiss-daily-budget-recommendations.md). |
| `POST` | `/v1/recommendations/target-cpas/query` | Returns target CPA recommendations using [`Query Target CPA Recommendations`](query-target-cpa-recommendations.md). Recommends an adjusted target cost-per-acquisition for campaigns using a Maximize Conversions bid strategy. The system sets bids automatically to try to meet the target; the target itself isn’t a bid. |
| `POST` | `/v1/recommendations/target-cpas/apply` | Applies a target CPA recommendation using [`Apply Target CPA Recommendations`](apply-target-cpa-recommendations.md). |
| `POST` | `/v1/recommendations/target-cpas/dismiss` | Dismisses a target CPA recommendation using [`Dismiss Target CPA Recommendations`](dismiss-target-cpa-recommendations.md). |

##### Track the Recommendation Lifecycle

Every recommendation has a `state` field. Recommendations start in `AVAILABLE` state and move to either `APPLIED` or `DISMISSED` via the API. State is terminal. After the system applies or dismisses a recommendation, it doesn’t return to available.

The `state` field tracks the advertiser’s response. New recommendations start `AVAILABLE`, then move to `APPLIED` or `DISMISSED`. The `status` field reflects whether the system marks the recommendation record itself `ENABLED`, `DISABLED`, or `DELETED`. In most workflows, only `state` matters.

The following table lists the possible `state` values:

| State | Meaning |
| --- | --- |
| `AVAILABLE` | The recommendation is active and awaiting action. This is the default state for new recommendations. |
| `APPLIED` | The advertiser accepted the recommendation, and the system made the change to the campaign or ad group. |
| `DISMISSED` | The advertiser explicitly rejected the recommendation. The system made no change to the campaign. |
| `DELETE` | The system archives the recommendation and no longer returns it in queries. |

> **Note**: The `DELETE` value of `state` and the `DELETED` value of `status` are similarly named but distinct. Don’t confuse them when filtering or reading a recommendation record.

##### Filter By Recommendation Category

The `recommendationType` field uses the [`RecommendationCategory`](recommendationcategory.md) enum. Each optimization area has a merged category and a system category (algorithm-generated, prefixed `S`). Use the merged category when filtering to retrieve all recommendations for that area.

The following table lists each optimization area’s merged and system categories:

| Merged | System (S) | Applies To |
| --- | --- | --- |
| `KEYWORD` | `SKEYWORD` | Keyword recommendations |
| `DAILYCAP` | `SDAILYCAP` | Daily budget recommendations |
| `TCPA` | `STCPA` | Target CPA recommendations |
| `BID` | `SBID` | Bid recommendations |

##### Query Recommendations

All recommendation types use a `POST /query` pattern with the [`RecommendationQueryRequest`](recommendationqueryrequest.md) body. Two filters are mandatory on every request:

- The `promotedObjectId` field is the ID of the promoted object being queried. Use the app Adam ID when `promotedObjectType` is `APPSTORE_APP`, or the brand ID when it is `BUSINESS_BRAND`.
- The `promotedObjectType` field is the type of the promoted object (for example, `APPSTORE_APP`).

Optional filters such as `state` and `campaignId` narrow results further. The following example shows a query request body with these filters applied:

```json
{
  "pagination": {
    "offset": 0,
    "pageSize": 20
  },
  "filters": [
    {
      "field": "promotedObjectId",
      "operator": "EQUALS",
      "value": [
        "123456"
      ]
    },
    {
      "field": "promotedObjectType",
      "operator": "EQUALS",
      "value": [
        "APPSTORE_APP"
      ]
    },
    {
      "field": "state",
      "operator": "EQUALS",
      "value": [
        "AVAILABLE"
      ]
    }
  ],
  "sorting": [
    {
      "field": "creationTime",
      "order": "DESC"
    }
  ]
}
```

##### Apply Recommendations

Applying a recommendation signals that the API user accepts the recommendation and wants the API to make the corresponding change automatically. Each type has a dedicated apply endpoint. All items in a single request must share the same `promotedObjectId`.

The following table shows what each apply endpoint changes:

| Endpoint | Action Taken |
| --- | --- |
| `/v1/recommendations/daily-budgets/apply` | Updates the campaign’s daily budget. See [`Campaign.DailyBudget`](campaign/dailybudget-data.dictionary.md). |
| `/v1/recommendations/target-cpas/apply` | Updates the target CPA the campaign’s Maximize Conversions auto-bidding uses. This isn’t a field on Campaign or AdGroup. The applied value is only visible in this endpoint’s history response. |

Required fields on every apply item are `id`, `promotedObjectId`, and `promotedObjectType`.

##### Dismiss Recommendations

Dismiss requests use the same structure as apply, but the API ignores value override fields. You only need `id`, `promotedObjectId`, and `promotedObjectType`. The request doesn’t modify any campaign or ad group entity.

##### Review Recommendation History

Apply and dismiss operations return a history object rather than the original recommendation object. History records preserve the full state of the recommendation at the time of the action, including the value the system actually applied, and serve as the audit trail for optimization changes.

## Topics

- [Query Target CPA Recommendations](query-target-cpa-recommendations.md)
  Retrieve target cost-per-acquisition recommendations for campaigns using a Maximize Conversions bid strategy.
- [Apply Target CPA Recommendations](apply-target-cpa-recommendations.md)
  Apply one or more target CPA recommendations.
- [Dismiss Target CPA Recommendations](dismiss-target-cpa-recommendations.md)
  Dismiss one or more target CPA recommendations without changing the campaign’s bid strategy.
- [Query Daily Budget Recommendations](query-daily-budget-recommendations.md)
  Retrieve daily budget recommendations for campaigns that may have more opportunities.
- [Apply Daily Budget Recommendations](apply-daily-budget-recommendations.md)
  Apply one or more daily budget recommendations, updating the campaign’s daily budget to the suggested amount.
- [Dismiss Daily Budget Recommendations](dismiss-daily-budget-recommendations.md)
  Dismiss one or more daily budget recommendations without changing the campaign’s budget.

## See Also

- [Suggestions Endpoints](suggestions-endpoints.md)
  Endpoints for querying keyword, phrase, category, and Target CPA suggestions.
- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [Insights Endpoints](insights-endpoints.md)
  Query impression share and search term popularity data for your apps.
- [Recommendations Data Objects](recommendations-data-objects.md)
  Request and response objects for recommendation endpoints.
- [Recommendations Query and Filter Objects](recommendations-query-filter-objects.md)
  Query, filter, pagination, and sorting objects for recommendation requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendations-endpoints)*