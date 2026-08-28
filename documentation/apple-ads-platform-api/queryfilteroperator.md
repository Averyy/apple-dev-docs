# QueryFilterOperator

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Enumeration of the comparison operators supported in query filters.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string QueryFilterOperator
```

#### Discussion

The `QueryFilterOperator` enumerates the comparison operators available in `QueryFilter.operator`. Not every field or endpoint supports all operators. Refer to each entity’s dictionary keys for per-field operator support.

Endpoints that accept a `QueryFilter` or `QueryRequest`:

- [`Query Campaigns`](post-campaigns-query.md)
- [`Query Ad Groups`](post-adgroups-query.md)
- [`Query Keywords`](post-keywords-query.md)
- [`Query Negative Keywords`](post-negative-keywords-query.md)
- [`Query App Locale Details`](query-default-product-page-locale-details-by-adam-id.md)
- [`Query Supported App Languages`](query-supported-app-languages.md)
- [`Check App Eligibility`](find-apps-eligibilities.md)
- [`Query Rejection Reasons`](find-rejection-reasons.md)
- [`Query Assets`](query-assets.md)
- [`Query Product Pages`](query-product-pages.md)
- [`Query Product Page Locale Details`](query-product-page-locale-details.md)
- [`Query Ad Creatives`](post-creatives-query.md)
- [`Query Brands`](query-brands.md)
- [`Query Business Categories`](query-categories.md)
- [`Query Location Groups`](query-location-groups.md)
- [`Query for Locations`](query-locations.md)
- [`Query Rejection Reasons for Brands`](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
- [`Query Budget Orders`](post-shared-budgets-query.md)

## See Also

- [type QuerySortOrder](querysortorder.md)
  Enumeration of the sort directions available when ordering query results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryfilteroperator)*