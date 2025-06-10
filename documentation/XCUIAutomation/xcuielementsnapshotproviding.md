# XCUIElementSnapshotProviding

**Framework**: XCUIAutomation  
**Kind**: protocol

A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
protocol XCUIElementSnapshotProviding : NSObjectProtocol
```

## Topics

### Providing snapshots
- [func snapshot() throws -> any XCUIElementSnapshot](xcuielementsnapshotproviding/snapshot.md)
  Returns a snapshot of an element’s attributes and descendant user interface hierarchy.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [XCUIApplication](xcuiapplication.md)
- [XCUIElement](xcuielement.md)

## See Also

- [class XCUIElement](xcuielement.md)
  A UI element in an application.
- [protocol XCUIElementAttributes](xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshot](xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](xcuicoordinate.md)
  A location on screen relative to a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshotproviding)*