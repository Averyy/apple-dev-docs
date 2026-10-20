# Sorting

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The order of grouped results.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object Sorting
```

## Properties

- `field` (string): The name of a field.
- `ignoreCase` (boolean)
- `sortOrder` (string): The order of grouped results.

  **Allowed Values**: `ASCENDING`, `DESCENDING`

## See Also

### API Usability
- [object Condition](./condition.md)
  The list of condition objects that allow users to filter a list of records.
- [object PageDetail](./pagedetail.md)
  The number of items that return in the page.
- [object Pagination](./pagination.md)
  The procedure to refine returned results using limit and offset parameters.
- [object Selector](./selector.md)
  The selector objects available to filter returned data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/sorting)*