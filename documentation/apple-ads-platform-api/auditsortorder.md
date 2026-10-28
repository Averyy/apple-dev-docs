# AuditSortOrder

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Sort direction for audit sorting entries in a change history query.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AuditSortOrder
```

## Possible Values

- `ASC`: Ascending order. Smallest or earliest values first.
- `DESC`: Descending order. Largest or most recent values first. Default when `order` is omitted from a sort directive.

## Discussion

The `AuditSortOrder` controls the direction of a sort directive in an [`AuditQuery`](./auditquery.md) request. When the `sorting` array is omitted entirely, results default to `eventTime DESC` (most recent first).

## See Also

- [type AuditEventType](./auditeventtype.md)
  Enumeration of change operation types in change history, used in audit summary objects, change detail objects, and query filters.
- [type AuditOperator](./auditoperator.md)
  Enumeration of comparison operators supported in audit filter conditions for change history queries.
- [type AuditUserType](./auditusertype.md)
  Enumeration of actor categories in change history records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsortorder)*