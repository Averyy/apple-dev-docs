# XCUIAccessibilityAuditType

**Framework**: XCUIAutomation  
**Kind**: struct

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
struct XCUIAccessibilityAuditType
```

## Topics

### Accessibility audit type creation
- [init(rawValue: UInt64)](xcuiaccessibilityaudittype/init(rawvalue:).md)
### Accessibility audit types
- [static var action: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/action.md)
- [static var all: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/all.md)
- [static var contrast: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/contrast.md)
- [static var dynamicType: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/dynamictype.md)
- [static var elementDetection: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/elementdetection.md)
- [static var hitRegion: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/hitregion.md)
- [static var parentChild: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/parentchild.md)
- [static var sufficientElementDescription: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/sufficientelementdescription.md)
- [static var textClipped: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/textclipped.md)
- [static var trait: XCUIAccessibilityAuditType](xcuiaccessibilityaudittype/trait.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func performAccessibilityAudit(for: XCUIAccessibilityAuditType, ((XCUIAccessibilityAuditIssue) throws -> Bool)?) throws](xcuiapplication/performaccessibilityaudit(for:_:).md)
- [class XCUIAccessibilityAuditIssue](xcuiaccessibilityauditissue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityaudittype)*