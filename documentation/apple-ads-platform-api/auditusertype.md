# AuditUserType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Enumeration of actor categories in change history records.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AuditUserType
```

#### Discussion

`AuditUserType` appears in the `userType` field of [`AuditSummary`](auditsummary.md) and [`ChangeDetails`](changedetails.md) records. Use it to distinguish manual advertiser-initiated changes from API-driven automation or Apple-initiated actions.

Filter by `userType` in an [`AuditQuery`](auditquery.md) to scope results to a specific actor category:

```json
{
  "field": "userType",
  "operator": "IN",
  "value": [
    "CUSTOMER_API"
  ]
}
```

This is especially useful when auditing API-driven changes independently of UI actions.

## See Also

- [type AuditEventType](auditeventtype.md)
  Enumeration of change operation types in change history, used in audit summary objects, change detail objects, and query filters.
- [type AuditOperator](auditoperator.md)
  Enumeration of comparison operators supported in audit filter conditions for change history queries.
- [type AuditSortOrder](auditsortorder.md)
  Sort direction for audit sorting entries in a change history query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditusertype)*