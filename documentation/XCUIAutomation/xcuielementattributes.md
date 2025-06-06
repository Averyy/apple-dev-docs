# XCUIElementAttributes

**Framework**: Xcuiautomation  
**Kind**: protocol

Attributes exposed by UI elements.

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
protocol XCUIElementAttributes
```

#### Overview

The [`XCUIElementAttributes`](xcuielementattributes.md) protocol adds attribute-related functionality to the [`XCUIElement`](xcuielement.md) class. Access these properties on an instance of [`XCUIElement`](xcuielement.md) to query the current state of the UI element’s attributes.

> **Note**:  The attributes provided by this protocol represent data exposed to the Accessibility system, and are available during query matching.

## Topics

### Identity
- [var identifier: String](xcuielementattributes/identifier.md)
  The element’s accessibility identifier.
- [var elementType: XCUIElement.ElementType](xcuielementattributes/elementtype.md)
  The type of the element.
- [XCUIElement.ElementType](xcuielement/elementtype.md)
  The types of UI elements that you find, inspect, and interact with in a UI test.
### Value
- [var value: Any?](xcuielementattributes/value.md)
  The raw value attribute of the element.
- [var placeholderValue: String?](xcuielementattributes/placeholdervalue.md)
  The value displayed when the element has no value.
- [var title: String](xcuielementattributes/title.md)
  The title attribute of the element.
- [var label: String](xcuielementattributes/label.md)
  The label attribute of the element.
### Interaction state
- [var hasFocus: Bool](xcuielementattributes/hasfocus.md)
  The property that determines whether the element has UI focus.
- [var isEnabled: Bool](xcuielementattributes/isenabled.md)
  Whether or not the element is enabled for user interaction.
- [var isSelected: Bool](xcuielementattributes/isselected.md)
  The property that determines whether the element is selected.
### Size
- [var frame: CGRect](xcuielementattributes/frame.md)
  The frame of the element in the screen’s coordinate space.
- [var horizontalSizeClass: XCUIElement.SizeClass](xcuielementattributes/horizontalsizeclass.md)
  The horizontal size class of the element.
- [var verticalSizeClass: XCUIElement.SizeClass](xcuielementattributes/verticalsizeclass.md)
  The vertical size class of the element.
- [XCUIElement.SizeClass](xcuielement/sizeclass.md)
  The user interface size classes you can inspect in a UI test.

## Relationships

### Inherited By
- [XCUIElementSnapshot](xcuielementsnapshot.md)
### Conforming Types
- [XCUIApplication](xcuiapplication.md)
- [XCUIElement](xcuielement.md)

## See Also

- [class XCUIElement](xcuielement.md)
  A UI element in an application.
- [protocol XCUIElementSnapshot](xcuielementsnapshot.md)
  A set of attributes to express a snapshot of an element’s attributes and descendant user interface hierarchy.
- [protocol XCUIElementSnapshotProviding](xcuielementsnapshotproviding.md)
  A method to capture a snapshot of an element’s attributes and descendant user interface hierarchy.
- [class XCUICoordinate](xcuicoordinate.md)
  A location on screen relative to a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/XCUIAutomation/xcuielementattributes)*