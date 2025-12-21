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