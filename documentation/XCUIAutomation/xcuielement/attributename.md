# XCUIElement.AttributeName

**Framework**: XCUIAutomation  
**Kind**: struct  
**Role**: Structure

A set of string constants that serve as keys for storing element attributes in a dictionary.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
struct AttributeName
```

```c
typedef NSString * XCUIElementAttributeName;
```

## Topics

### Keys
- [static let children: XCUIElement.AttributeName](./attributename/children.md)
  A string constant that serves as a dictionary key identifying an element’s children.
- [static let elementType: XCUIElement.AttributeName](./attributename/elementtype.md)
  A string constant that serves as a dictionary key identifying an element’s type.
- [static let enabled: XCUIElement.AttributeName](./attributename/enabled.md)
  A string constant that serves as a dictionary key identifying whether an element is enabled.
- [static let frame: XCUIElement.AttributeName](./attributename/frame.md)
  A string constant that serves as a dictionary key identifying an element’s frame.
- [static let hasFocus: XCUIElement.AttributeName](./attributename/hasfocus.md)
  A string constant that serves as a dictionary key identifying whether an element has focus.
- [static let horizontalSizeClass: XCUIElement.AttributeName](./attributename/horizontalsizeclass.md)
  A string constant that serves as a dictionary key identifying an element’s horizontal size class.
- [static let identifier: XCUIElement.AttributeName](./attributename/identifier.md)
  A string constant that serves as a dictionary key identifying an element’s identifier.
- [static let label: XCUIElement.AttributeName](./attributename/label.md)
  A string constant that serves as a dictionary key identifying an element’s label.
- [static let placeholderValue: XCUIElement.AttributeName](./attributename/placeholdervalue.md)
  A string constant that serves as a dictionary key identifying an element’s placeholder value.
- [static let selected: XCUIElement.AttributeName](./attributename/selected.md)
  A string constant that serves as a dictionary key identifying whether an element is selected.
- [static let title: XCUIElement.AttributeName](./attributename/title.md)
  A string constant that serves as a dictionary key identifying an element’s title.
- [static let value: XCUIElement.AttributeName](./attributename/value.md)
  A string constant that serves as a dictionary key identifying an element’s value.
- [static let verticalSizeClass: XCUIElement.AttributeName](./attributename/verticalsizeclass.md)
  A string constant that serves as a dictionary key identifying an element’s vertical size class.
### Initializers
- [init(rawValue: String)](./attributename/init%28rawvalue%29.md)
  Creates an attribute name dictionary key from a string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [XCUIElement.ElementType](./elementtype.md)
  The types of UI elements that you find, inspect, and interact with in a UI test.
- [XCUIElement.SizeClass](./sizeclass.md)
  The user interface size classes you can inspect in a UI test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/attributename)*