# XCUIAccessibilityAuditIssue

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

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

```swift
class XCUIAccessibilityAuditIssue
```

```objc
@interface XCUIAccessibilityAuditIssue : NSObject
```

## Topics

### Type and description
- [var auditType: XCUIAccessibilityAuditType](./xcuiaccessibilityauditissue/audittype.md)
- [var compactDescription: String](./xcuiaccessibilityauditissue/compactdescription.md)
- [var detailedDescription: String](./xcuiaccessibilityauditissue/detaileddescription.md)
### UI element
- [var element: XCUIElement?](./xcuiaccessibilityauditissue/element.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing an accessibility audit
- [func performAccessibilityAudit(for: XCUIAccessibilityAuditType, ((XCUIAccessibilityAuditIssue) throws -> Bool)?) throws](./xcuiapplication/performaccessibilityaudit%28for,_%29.md)
- [struct XCUIAccessibilityAuditType](./xcuiaccessibilityaudittype.md)
- [- performAccessibilityAuditWithAuditTypes:issueHandler:error:](./xcuiapplication/performaccessibilityauditwithaudittypes_issuehandler_error_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue)*