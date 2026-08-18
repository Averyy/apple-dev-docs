# AuditEventType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Enumeration of change operation types in change history, used in audit summary objects, change detail objects, and query filters.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AuditEventType
```

#### Discussion

Use `AuditEventType` values in the `eventType` filter of an [`AuditQuery`](auditquery.md) request to narrow results to specific change operations:

```json
{
  "field": "eventType",
  "operator": "IN",
  "value": [
    "CREATE",
    "DELETE"
  ]
}
```

## See Also

- [type AuditOperator](auditoperator.md)
  Enumeration of comparison operators supported in audit filter conditions for change history queries.
- [type AuditSortOrder](auditsortorder.md)
  Sort direction for audit sorting entries in a change history query.
- [type AuditUserType](auditusertype.md)
  Enumeration of actor categories in change history records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditeventtype)*