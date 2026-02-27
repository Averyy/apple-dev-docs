# Condition

**Framework**: Apple Ads  
**Kind**: dictionary

The list of condition objects that allow users to filter a list of records.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object Condition
```

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

The `Condition` object functionality is similar to the `WHERE` clause in SQL.

## Properties

- `field` (string): The name of a field.
- `ignoreCase` (boolean)
- `operator` (string): The operator values compare attributes to a list of specified values. - **BETWEEN**: The attribute matches the values within a specified range. The values can be numbers, text, or dates.
- **CONTAINS**: The attribute matches the value in the specified list.
- **CONTAINS_ALL**: The attribute has all of the values in the specified list. The attribute must be a collection type.
- **CONTAINS_ANY**: The attribute contains any of the values in the specified list. The attribute must be a collection type.
- **ENDSWITH**: The attribute matches the suffix of a string.
- **EQUALS**: The attribute contains exact values.
- **GREATER_THAN**: The value is greater than the specified value. You can use this attribute with time parameters.
- **IN**: The attribute matches any value in a list of specified values.
- **LESS_THAN**: The value is less than the specified value. You can use this attribute with time parameters.
- **STARTSWITH**: The attribute matches the prefix of a string.
- `values` ([string]): A list of matching values.

## See Also

- [object PageDetail](pagedetail.md)
  The number of items that return in the page.
- [object Pagination](pagination.md)
  The procedure to refine returned results using limit and offset parameters.
- [object Selector](selector.md)
  The selector objects available to filter returned data.
- [object Sorting](sorting.md)
  The order of grouped results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/condition)*