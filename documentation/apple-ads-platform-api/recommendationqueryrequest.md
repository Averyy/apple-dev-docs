# RecommendationQueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The structured request body for all recommendation query endpoints.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationQueryRequest
```

#### Discussion

`QueryRequest` is the request body for all `POST .../query` endpoints in the Recommendations API. Two filter conditions are mandatory on every request:

```json
[
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
  }
]
```

Omitting either required filter returns a 400 error with a `MISSING_REQUIRED_FILTER` detail in the response. Additional optional filters narrow the result set. For example, `state` or `campaignId`. The API combines all filter conditions with AND logic.

##### Example

```json
{
  "filters": [
    {
      "field": "promotedObjectId",
      "operator": "EQUALS",
      "value": [
        "123456789"
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
      ],
      "ignoreCase": false
    }
  ],
  "sorting": [
    {
      "field": "creationTime",
      "order": "DESC"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `filters` ([RecommendationFilterCondition]): Array of filter conditions. `promotedObjectId` and `promotedObjectType` filters are required on every request. See [`FilterCondition`](recommendationfiltercondition.md).
- `sorting` ([RecommendationSorting]): Array of sort specifications. Multiple entries are applied in order (primary sort first). See [`Sorting`](sorting.md).
- `pagination` (RecommendationQueryRequestPagination): Pagination parameters controlling offset and page size. Defaults: `offset` 0, `pageSize` 20. See [`QueryRequestPagination`](recommendationqueryrequestpagination.md).

## See Also

- [object RecommendationQueryRequestPagination](recommendationqueryrequestpagination.md)
  Pagination parameters for a recommendation query request.
- [object RecommendationSorting](recommendationsorting.md)
  A sort specification used in a recommendation query request to order results.
- [type RecommendationSortingOrder](recommendationsortingorder.md)
  The sort direction used in a recommendation sorting specification.
- [object RecommendationFilterCondition](recommendationfiltercondition.md)
  A single filter condition used in a recommendation query request to narrow results.
- [type RecommendationFilterOperator](recommendationfilteroperator.md)
  The comparison operator applied in a recommendation filter condition.
- [type RecommendationState](recommendationstate.md)
  The lifecycle state of a recommendation, indicating whether it is available to act on or has already been accepted or rejected.
- [type RecommendationStatus](recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationqueryrequest)*