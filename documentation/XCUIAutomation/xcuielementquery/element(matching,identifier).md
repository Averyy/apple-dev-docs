# element(matching:identifier:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Matches the provided element type and identifier.

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
func element(matching elementType: XCUIElement.ElementType, identifier: String?) -> XCUIElement
```

```objc
- (XCUIElement *) elementMatchingType:(XCUIElementType) elementType identifier:(NSString *) identifier;
```

## Parameters

- `elementType`: The element type to match.
- `identifier`: An optional identifier string to match against any one of each element’s identifying properties: [`identifier`](../xcuielementattributes/identifier.md), [`title`](../xcuielementattributes/title.md), [`label`](../xcuielementattributes/label.md), [`value`](../xcuielementattributes/value.md), or [`placeholderValue`](../xcuielementattributes/placeholdervalue.md).

## See Also

### Accessing matched elements
- [var allElementsBoundByAccessibilityElement: [XCUIElement]](./allelementsboundbyaccessibilityelement.md)
  Immediately evaluates the query and returns an array of elements bound to the resulting accessibility elements.
- [var allElementsBoundByIndex: [XCUIElement]](./allelementsboundbyindex.md)
  Immediately evaluates the query and returns an array of elements bound by the index of each result.
- [var count: Int](./count.md)
  Evaluates the query and returns the number of elements that match.
- [var element: XCUIElement](./element.md)
  The query’s single matching element.
- [func element(boundBy: Int) -> XCUIElement](./element%28boundby%29.md)
  Uses an index into the query’s results to determine which underlying accessibility element to use.
- [func element(matching: NSPredicate) -> XCUIElement](./element%28matching%29.md)
  Matches the predicate.
- [subscript(String) -> XCUIElement](./subscript%28_%29.md)
  Returns a descendant element that matches a provided identifier.
- [func element(at: Int) -> XCUIElement](./element%28at%29.md)
  Returns an element that resolves to the index into the query’s result set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:identifier:))*