# QueryFilterOperator

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Enumeration of the comparison operators supported in query filters.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string QueryFilterOperator
```

## Possible Values

- `EQUALS`: Exact match.
- `NOT_EQUALS`: Matches records where the field value is not equal to the specified value.
- `IN`: Matches any of the specified values.
- `NOT_IN`: Matches records where the field value is not in the specified set.
- `CONTAINS_ANY`: Matches records where the field contains any of the specified values.
- `NOT_CONTAINS_ANY`: Matches records where the field does not contain any of the specified values.
- `CONTAINS_ALL`: Matches records where the field contains all of the specified values.
- `NOT_CONTAINS_ALL`: Matches records where the field does not contain all of the specified values.
- `LIKE`: Pattern match, case-sensitive. Use `%` as a wildcard to match any sequence of characters. Set `ignoreCase` to `true` on the `QueryFilter` for a case-insensitive pattern match.
- `NOT_LIKE`: Matches records where the field does not match the pattern. Use `%` as a wildcard to match any sequence of characters.
- `STARTS_WITH`: Matches records where the field value starts with the specified string.
- `ENDS_WITH`: Matches records where the field value ends with the specified string.
- `GREATER_THAN`: Matches records where the field value is greater than the specified value.
- `GREATER_THAN_OR_EQUAL_TO`: Matches records where the field value is greater than or equal to the specified value.
- `LESS_THAN`: Matches records where the field value is less than the specified value.
- `LESS_THAN_OR_EQUAL_TO`: Matches records where the field value is less than or equal to the specified value.
- `BETWEEN`: Matches values within an inclusive range. Requires exactly two values, ordered as `[minimum, maximum]`.
- `IS_NULL`: Matches records where the field has no value.
- `IS_NOT_NULL`: Matches records where the field has a value.

## Discussion

The `QueryFilterOperator` enumerates the comparison operators available in `QueryFilter.operator`. Not every field or endpoint supports all operators. Refer to each entity’s dictionary keys for per-field operator support.

Endpoints that accept a `QueryFilter` or `QueryRequest`:

- [`Query Campaigns`](./post-campaigns-query.md)
- [`Query Ad Groups`](./post-adgroups-query.md)
- [`Query Keywords`](./post-keywords-query.md)
- [`Query Negative Keywords`](./post-negative-keywords-query.md)
- [`Query App Locale Details`](./query-default-product-page-locale-details-by-adam-id.md)
- [`Query Supported App Languages`](./query-supported-app-languages.md)
- [`Check App Eligibility`](./find-apps-eligibilities.md)
- [`Query Rejection Reasons`](./find-rejection-reasons.md)
- [`Query Assets`](./query-assets.md)
- [`Query Product Pages`](./query-product-pages.md)
- [`Query Product Page Locale Details`](./query-product-page-locale-details.md)
- [`Query Ad Creatives`](./post-creatives-query.md)
- [`Query Brands`](./query-brands.md)
- [`Query Business Categories`](./query-categories.md)
- [`Query Location Groups`](./query-location-groups.md)
- [`Query for Locations`](./query-locations.md)
- [`Query Rejection Reasons for Brands`](./query-policy-assignments-%28rejection-reasons%29-for-external-consumers.md)
- [`Query Budget Orders`](./post-shared-budgets-query.md)

## See Also

### Type Aliases
- [type QuerySortOrder](./querysortorder.md)
  Enumeration of the sort directions available when ordering query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryfilteroperator)*