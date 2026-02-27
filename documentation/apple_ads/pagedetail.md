# PageDetail

**Framework**: Apple Ads  
**Kind**: dictionary

The number of items that return in the page.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object PageDetail
```

#### Discussion

The `PageDetail` object contains the pagination response for returned multiple records.

```json
{
   "data":[
     { },
     ...
   ],
   "pagination"{
     "totalResults": 10,
     "startIndex": 1,
     "itemsPerPage": 10
   },
}

```

## Properties

- `itemsPerPage` (int32): The maximum number of entries that return for this operation, which is the value of `count` in the GET operation. The actual number of entries that return can be less than the maximum `itemsPerPage`.
- `startIndex` (int32): The offset of the first entry that returns. Use `offset` in the request query string or [`Selector`](selector.md) to override the default value of `0`. For example, if the request is `offset=5`, the response `startIndex` is also `5`. A value of `0` retrieves the first `itemsPerPage` results from the full result set.
- `totalResults` (int64): The total number of entries that return for the operation.

## See Also

- [object Condition](condition.md)
  The list of condition objects that allow users to filter a list of records.
- [object Pagination](pagination.md)
  The procedure to refine returned results using limit and offset parameters.
- [object Selector](selector.md)
  The selector objects available to filter returned data.
- [object Sorting](sorting.md)
  The order of grouped results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/pagedetail)*