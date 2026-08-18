# AuditSortOrder

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Sort direction for audit sorting entries in a change history query.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AuditSortOrder
```

#### Discussion

`AuditSortOrder` controls the direction of a sort directive in an [`AuditQuery`](auditquery.md) request. When the `sorting` array is omitted entirely, results default to `eventTime DESC` (most recent first).

## See Also

- [type AuditEventType](auditeventtype.md)
  Enumeration of change operation types in change history, used in audit summary objects, change detail objects, and query filters.
- [type AuditOperator](auditoperator.md)
  Enumeration of comparison operators supported in audit filter conditions for change history queries.
- [type AuditUserType](auditusertype.md)
  Enumeration of actor categories in change history records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditsortorder)*