# CampaignQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a Campaign query, containing matched results and pagination metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CampaignQueryResponse
```

#### Discussion

The campaign query endpoint returns `CampaignQueryResponse`, which contains the filtered, sorted, and paginated set of `Campaign` objects matching the request. Pagination metadata in the envelope supports offset-based navigation through large result sets.

##### Example

```json
{
  "result": [
    {
      "id": 111222333,
      "name": "AwayFinder Apple Maps Campaign",
      "adAccountId": 123456789,
      "promotedObjectType": "BUSINESS_BRAND",
      "promotedObjectId": "987654321",
      "status": "ENABLED",
      "billingEvent": "TAPS",
      "startTime": "2025-09-01T00:00:00.000",
      "endTime": "2025-12-31T23:59:59.000",
      "dailyBudget": {
        "value": {
          "amount": "900.00",
          "currency": "USD"
        }
      },
      "targeting": {
        "supplySource": {
          "include": [
            "MAPS"
          ]
        },
        "supplyPlacement": {
          "include": [
            "MAPS_SEARCH_RESULTS"
          ]
        }
      },
      "bidStrategy": {
        "bidStrategyType": "MAX_ENGAGEMENTS",
        "bidStrategyGoal": "TAP"
      },
      "creationTime": "2025-01-15T10:30:00.000",
      "modificationTime": "2025-01-20T14:45:00.000",
      "paymentModel": "PAYG",
      "systemStatus": "RUNNING",
      "systemStatusReasons": [],
      "systemStatusLimitingReasons": [],
      "displayStatus": "RUNNING",
      "deleted": false
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` ([Campaign]): The list of campaigns matching the query filters. See [`Campaign`](campaign.md). Read-only.
- `pagination` (QueryPaginationResult): Pagination metadata for the response, including `offset`, `pageSize`, and `totalCount`. See [`QueryPaginationResult`](querypaginationresult.md). Read-only.
- `error` (Error): Error information if the request encountered an error. See [`Error`](error.md). Read-only.

## See Also

- [object Campaign](campaign.md)
  The top-level container that defines a campaign’s promoted object, billing, scheduling, and targeting.
- [object CampaignCreate](campaigncreate.md)
  The request body for creating a new campaign.
- [object CampaignUpdate](campaignupdate.md)
  The request body for updating an existing Campaign object.
- [object CampaignResponse](campaignresponse.md)
  The response object for a Campaign operation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignqueryresponse)*