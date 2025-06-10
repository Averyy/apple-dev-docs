# element(matching:identifier:)

**Framework**: XCUIAutomation  
**Kind**: method

Matches the provided element type and identifier.

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
func element(matching elementType: XCUIElement.ElementType, identifier: String?) -> XCUIElement
```

## Parameters

- `elementType`: The element type to match.
- `identifier`: An optional identifier string to match against any one of each element’s identifying properties:  ,  ,  ,  , or  .

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
- [func element(matching: NSPredicate) -> XCUIElement](xcuielementquery/element(matching:).md)
  Matches the predicate.
- [subscript(String) -> XCUIElement](xcuielementquery/subscript(_:).md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](xcuielementquery/element(at:).md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:identifier:))*