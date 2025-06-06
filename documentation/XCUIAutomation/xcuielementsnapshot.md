# XCUIElementSnapshot

**Framework**: Xcuiautomation  
**Kind**: protocol

A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.

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
protocol XCUIElementSnapshot : XCUIElementAttributes
```

## Topics

### Inspecting attributes
- [var children: [any XCUIElementSnapshot]](xcuielementsnapshot/children.md)
  An array of descendant user interface element snapshots.
- [var dictionaryRepresentation: [XCUIElement.AttributeName : Any]](xcuielementsnapshot/dictionaryrepresentation.md)
  A hierarchical dictionary representation of an element’s attributes, and all of an element’s user interface descendants.

## Relationships

### Inherits From
- [XCUIElementAttributes](xcuielementattributes.md)

## See Also

- [class XCUIElement](xcuielement.md)
  A UI element in an application.
- [protocol XCUIElementAttributes](xcuielementattributes.md)
  Attributes exposed by UI elements.
- [protocol XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](xcuicoordinate.md)
  A location on screen relative to a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshot)*