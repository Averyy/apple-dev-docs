# AuditOperator

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Enumeration of comparison operators supported in audit filter conditions for change history queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AuditOperator
```

#### Discussion

`AuditOperator` determines how the system applies the filter `values` against the target field. Use `GREATER_THAN` or `LESS_THAN` with a single timestamp for an open-ended `eventTime` filter.

Every valid `AuditQuery` must include at least one filter on `eventTime` using `BETWEEN`, `GREATER_THAN`, or `LESS_THAN`. All other filters use `IN`.

## See Also

- [type AuditEventType](auditeventtype.md)
  Enumeration of change operation types in change history, used in audit summary objects, change detail objects, and query filters.
- [type AuditSortOrder](auditsortorder.md)
  Sort direction for audit sorting entries in a change history query.
- [type AuditUserType](auditusertype.md)
  Enumeration of actor categories in change history records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditoperator)*