# allElementsBoundByAccessibilityElement

**Framework**: XCUIAutomation  
**Kind**: property

Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.

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
var allElementsBoundByAccessibilityElement: [XCUIElement] { get }
```

## See Also

- [var allElementsBoundByIndex: [XCUIElement]](xcuielementquery/allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](xcuielementquery/count.md)
  Evaluates the query and returns the number of elements that match.
- [var element: XCUIElement](xcuielementquery/element.md)
  The query’s single matching element.
- [func element(boundBy: Int) -> XCUIElement](xcuielementquery/element(boundby:).md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: NSPredicate) -> XCUIElement](xcuielementquery/element(matching:).md)
  Matches the predicate.
- [func element(matching: XCUIElement.ElementType, identifier: String?) -> XCUIElement](xcuielementquery/element(matching:identifier:).md)
  Matches the provided element type and identifier.
- [subscript(String) -> XCUIElement](xcuielementquery/subscript(_:).md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](xcuielementquery/element(at:).md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/allelementsboundbyaccessibilityelement)*