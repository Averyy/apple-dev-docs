# performAccessibilityAuditWithAuditTypes:issueHandler:error:

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Xcode 16.3+

## Declaration

```objc
- (BOOL) performAccessibilityAuditWithAuditTypes:(XCUIAccessibilityAuditType) auditTypes issueHandler:(BOOL (^)(XCUIAccessibilityAuditIssue *issue)) block error:(NSError **) outError;
```

## See Also

### Performing an accessibility audit
- [struct XCUIAccessibilityAuditType](../xcuiaccessibilityaudittype.md)
- [class XCUIAccessibilityAuditIssue](../xcuiaccessibilityauditissue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityauditwithaudittypes:issuehandler:error:)*