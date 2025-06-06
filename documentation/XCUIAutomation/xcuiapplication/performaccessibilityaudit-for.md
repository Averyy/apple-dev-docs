# performAccessibilityAudit(for:_:)

**Framework**: Xcuiautomation  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Xcode 16.3+

## Declaration

```swift
@MainActor
@nonobjc @preconcurrency func performAccessibilityAudit(for auditTypes: XCUIAccessibilityAuditType = .all, _ issueHandler: ((XCUIAccessibilityAuditIssue) throws -> Bool)? = nil) throws
```

## See Also

- [struct XCUIAccessibilityAuditType](xcuiaccessibilityaudittype.md)
- [class XCUIAccessibilityAuditIssue](xcuiaccessibilityauditissue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:))*