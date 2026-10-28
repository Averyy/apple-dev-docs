# element

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The query’s single matching element.

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
var element: XCUIElement { get }
```

```objc
@property (readonly) XCUIElement * element;
```

## Discussion

Use the [`element`](./element.md) property to access a query’s result when you expect a single matching element for the query, but want to check for multiple ambiguous matches before accessing the result. The [`element`](./element.md) property traverses your app’s accessibility tree to check for multiple matching elements before returning, and fails the current test if there isn’t a single matching element.

In cases where you know categorically that there’s a single matching element, use the [`XCUIElementTypeQueryProvider`](../xcuielementtypequeryprovider.md) [`firstMatch`](../xcuielementtypequeryprovider/firstmatch.md) property instead. The [`firstMatch`](../xcuielementtypequeryprovider/firstmatch.md) property stops traversing your app’s accessibility hierarchy as soon as it finds a matching element, speeding up element query resolution.

## See Also

### Related Documentation
- [var firstMatch: XCUIElement](../xcuielementtypequeryprovider/firstmatch.md)
  The first element that matches the query.
### Accessing matched elements
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](./allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](./allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](./count.md)
  Evaluates the query and returns the number of elements that match.
- [func element(boundBy: Int) -> XCUIElement](./element%28boundby%29.md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: NSPredicate) -> XCUIElement](./element%28matching%29.md)
  Matches the predicate.
- [func element(matching: XCUIElement.ElementType, identifier: String?) -> XCUIElement](./element%28matching,identifier%29.md)
  Matches the provided element type and identifier.
- [subscript(String) -> XCUIElement](./subscript%28_%29.md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](./element%28at%29.md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element)*