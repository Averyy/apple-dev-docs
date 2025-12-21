# Pagination

**Framework**: Apple Ads  
**Kind**: dictionary

The procedure to refine returned results using limit and offset parameters.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object Pagination
```

#### Discussion

In the following example, the two optional parameters limit the number of campaigns that return. You specify `offset` and `limit` as query string parameters.

```console
GET https://api.searchads.apple.com/api/v5/campaigns?limit=<LIMIT>&offset=<OFFSET>
```

## See Also

- [object Condition](condition.md)
  The list of condition objects that allow users to filter a list of records.
- [object PageDetail](pagedetail.md)
  The number of items that return in the page.
- [object Selector](selector.md)
  The selector objects available to filter returned data.
- [object Sorting](sorting.md)
  The order of grouped results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/pagination)*