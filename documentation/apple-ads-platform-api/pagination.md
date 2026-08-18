# Pagination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Pagination state in change history list responses.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Pagination
```

#### Discussion

`Pagination` is returned in the `pagination` field of [`BaseAuditResponse`](baseauditresponse.md) (and its subtypes [`AuditSummaryResponse`](auditsummaryresponse.md) and [`ChangeDetailsResponse`](changedetailsresponse.md)).

To page through results, increment `offset` by `pageSize` on each subsequent request until `offset >= totalCount`. When `needTotals` is `"false"` in the [`AuditQuery`](auditquery.md) options, page forward instead until the response `result` array is empty.

##### Example

```json
{
  "offset": 0,
  "pageSize": 50,
  "totalCount": 137
}
```

## Properties

- `offset` (integer): Zero-based index of the first record on the current page.
- `pageSize` (integer): The number of records returned on this page.
- `totalCount` (integer): The total number of records matching the query across all pages. Returns `0` when `needTotals` is set to `"false"` in the request options. Read-only.

## See Also

- [object AuditQuery](auditquery.md)
  Request body for the Query Change History endpoint.
- [object AuditFilter](auditfilter.md)
  A single filter condition in an audit query request, specifying the field to filter on, the comparison operator, and one or more values to match against.
- [object AuditSorting](auditsorting.md)
  A sort directive in an audit query request, specifying a field to sort by and the direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/pagination)*