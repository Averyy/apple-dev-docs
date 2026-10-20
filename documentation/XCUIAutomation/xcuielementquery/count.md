# count

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

Evaluates the query and returns the number of elements that match.

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
var count: Int { get }
```

```objc
@property (readonly) NSUInteger count;
```

## See Also

### Accessing matched elements
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](./allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](./allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var element: XCUIElement](./element.md)
  The query’s single matching element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/count)*