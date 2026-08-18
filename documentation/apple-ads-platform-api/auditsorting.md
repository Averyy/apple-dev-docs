# AuditSorting

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A sort directive in an audit query request, specifying a field to sort by and the direction.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditSorting
```

#### Discussion

Include one or more `AuditSorting` entries in the `sorting` array of an [`AuditQuery`](auditquery.md) request to control the order of results. When you omit this array, the API returns results sorted by `eventTime` descending (most recent first).

```json
"sorting": [
  { "field": "eventTime", "order": "DESC" }
]
```

The API applies multiple sort directives in order. The first directive is the primary sort. Subsequent entries break ties.

##### Example

```json
{
  "field": "eventTime",
  "order": "DESC"
}
```

## Properties

- `field` (string): The name of the field to sort by. Common values: `eventTime`, `entityType`, `eventType`, `userType`.
- `order` (AuditSortOrder): The sort direction. See [`AuditSortOrder`](auditsortorder.md). Defaults to `DESC`.

## See Also

- [object AuditQuery](auditquery.md)
  Request body for the Query Change History endpoint.
- [object AuditFilter](auditfilter.md)
  A single filter condition in an audit query request, specifying the field to filter on, the comparison operator, and one or more values to match against.
- [object Pagination](pagination.md)
  Pagination state in change history list responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsorting)*