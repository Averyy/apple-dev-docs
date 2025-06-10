# element(matching:)

**Framework**: XCUIAutomation  
**Kind**: method

Matches the predicate.

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
func element(matching predicate: NSPredicate) -> XCUIElement
```

#### Discussion

The predicate evaluates against objects that conform to the [`XCUIElementAttributes`](xcuielementattributes.md) protocol.

> **Note**:  Where possible, use [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression)-based or format-string-based predicates with this method in preference to block-based predicates. This enables the framework to optimize the query’s performance.

## Parameters

- `predicate`: The predicate to match.

## See Also

- [var allElementsBoundByAccessibilityElement: [XCUIElement]](xcuielementquery/allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](xcuielementquery/allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](xcuielementquery/count.md)
  Evaluates the query and returns the number of elements that match.
- [var element: XCUIElement](xcuielementquery/element.md)
  The query’s single matching element.
- [func element(boundBy: Int) -> XCUIElement](xcuielementquery/element(boundby:).md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: XCUIElement.ElementType, identifier: String?) -> XCUIElement](xcuielementquery/element(matching:identifier:).md)
  Matches the provided element type and identifier.
- [subscript(String) -> XCUIElement](xcuielementquery/subscript(_:).md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](xcuielementquery/element(at:).md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:))*