# element

**Framework**: Xcuiautomation  
**Kind**: property

The query’s single matching element.

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
var element: XCUIElement { get }
```

#### Discussion

Use the [`element`](xcuielementquery/element.md) property to access a query’s result when you expect a single matching element for the query, but want to check for multiple ambiguous matches before accessing the result. The [`element`](xcuielementquery/element.md) property traverses your app’s accessibility tree to check for multiple matching elements before returning, and fails the current test if there isn’t a single matching element.

In cases where you know categorically that there’s a single matching element, use the [`XCUIElementTypeQueryProvider`](xcuielementtypequeryprovider.md) [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md) property instead. The [`firstMatch`](xcuielementtypequeryprovider/firstmatch.md) property stops traversing your app’s accessibility hierarchy as soon as it finds a matching element, speeding up element query resolution.

## See Also

- [var firstMatch: XCUIElement](xcuielementtypequeryprovider/firstmatch.md)
  The first element that matches the query.
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](xcuielementquery/allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](xcuielementquery/allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](xcuielementquery/count.md)
  Evaluates the query and returns the number of elements that match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element)*