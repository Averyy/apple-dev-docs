# matching(_:identifier:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.

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
func matching(_ elementType: XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery
```

```objc
- (XCUIElementQuery *) matchingType:(XCUIElementType) elementType identifier:(NSString *) identifier;
```

#### Return Value

A new query that defines a search that extends the search criteria of the receiver. The new search matches elements that match the original search of the requested type that have an identifying property matching a provided identifier. For the list of the types, see [`XCUIElement.ElementType`](../xcuielement/elementtype.md).

## Parameters

- `elementType`: The element type to match.
- `identifier`: An optional string to match against any one of each element’s identifying properties: [`identifier`](../xcuielementattributes/identifier.md), [`title`](../xcuielementattributes/title.md), [`label`](../xcuielementattributes/label.md), [`value`](../xcuielementattributes/value.md), or [`placeholderValue`](../xcuielementattributes/placeholdervalue.md).

## See Also

### Creating new queries
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./children%28matching%29.md)
  Returns a new query that matches all direct children of the requested type.
- [func descendants(matching: XCUIElement.ElementType) -> XCUIElementQuery](./descendants%28matching%29.md)
  Returns a new query that matches all descendants of the requested type.
- [func containing(NSPredicate) -> XCUIElementQuery](./containing%28_%29.md)
  Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.
- [func containing(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./containing%28_,identifier%29.md)
  Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.
- [func matching(identifier: String) -> XCUIElementQuery](./matching%28identifier%29.md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](./matching%28_%29.md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/matching(_:identifier:))*