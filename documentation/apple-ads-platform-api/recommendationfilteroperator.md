# FilterOperator

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The comparison operator applied in a recommendation filter condition.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string RecommendationFilterOperator
```

## Possible Values

- `EQUALS`: Exact match. The field value must equal the single filter value.
- `NOT_EQUALS`: Inverse of `EQUALS`. Excludes records where the field matches the filter value.
- `IN`: Set membership. The field value must match one of the values in the filter array.
- `CONTAINS_ANY`: For list-type fields. The field list must contain at least one value from the filter array.
- `CONTAINS_ALL`: For list-type fields. The field list must contain every value in the filter array.
- `LESS_THAN`: Numeric or date comparison. The field value must be less than the filter value.
- `LESS_THAN_OR_EQUAL_TO`: Numeric or date comparison. The field value must be less than or equal to the filter value.
- `GREATER_THAN`: Numeric or date comparison. The field value must be greater than the filter value.
- `GREATER_THAN_OR_EQUAL_TO`: Numeric or date comparison. The field value must be greater than or equal to the filter value.
- `BETWEEN`: Range comparison. The field value must fall between the two values in the filter array (inclusive). Supply exactly two values.
- `STARTS_WITH`: String prefix match. The field value must begin with the filter value.
- `ENDS_WITH`: String suffix match. The field value must end with the filter value.
- `LIKE`: Pattern match. Supports `%` as a wildcard character.

## Discussion

Use these operators in the `operator` field of a [`FilterCondition`](./recommendationfiltercondition.md). Not all operators are valid for all field types. Applying an incompatible operator returns a 400 error with a validation detail identifying the invalid condition.

For example, here’s a `BETWEEN` filter on a campaign ID range:

```json
{
  "field": "campaignId",
  "operator": "BETWEEN",
  "value": [
    "10000",
    "20000"
  ]
}
```

Endpoints that accept a `RecommendationFilterCondition` are [`Query Daily Budget Recommendations`](./query-daily-budget-recommendations.md), [`Query Target CPA Recommendations`](./query-target-cpa-recommendations.md), [`Query Target CPA Suggestion`](./query-target-cpa-suggestion.md), [`Query Category Suggestions`](./query-category-suggestions.md), [`Query Keyword Suggestions`](./query-keyword-suggestions.md), and [`Query Phrase Suggestions`](./query-phrase-suggestions.md).

## See Also

- [object RecommendationQueryRequest](./recommendationqueryrequest.md)
  The structured request body for all recommendation query endpoints.
- [object RecommendationQueryRequestPagination](./recommendationqueryrequestpagination.md)
  Pagination parameters for a recommendation query request.
- [object RecommendationSorting](./recommendationsorting.md)
  A sort specification used in a recommendation query request to order results.
- [type RecommendationSortingOrder](./recommendationsortingorder.md)
  The sort direction used in a recommendation sorting specification.
- [object RecommendationFilterCondition](./recommendationfiltercondition.md)
  A single filter condition used in a recommendation query request to narrow results.
- [type RecommendationState](./recommendationstate.md)
  The lifecycle state of a recommendation, indicating whether it’s available to act on or has already been accepted or rejected.
- [type RecommendationStatus](./recommendationstatus.md)
  The operational status of a recommendation record, independent of its lifecycle state.
- [type RecommendationCategory](./recommendationcategory.md)
  Enumeration that categorizes a recommendation by optimization area and origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationfilteroperator)*