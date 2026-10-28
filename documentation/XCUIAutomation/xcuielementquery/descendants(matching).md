# descendants(matching:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Returns a new query that matches all descendants of the requested type.

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
func descendants(matching type: XCUIElement.ElementType) -> XCUIElementQuery
```

```objc
- (XCUIElementQuery *) descendantsMatchingType:(XCUIElementType) type;
```

## Return Value

A new query that defines a search that extends the search criteria of the receiver. The new search finds all decendant of elements that match the original search and are of the requested type. For a list of the types, see [`XCUIElement.ElementType`](../xcuielement/elementtype.md).

## Discussion

Because [`XCUIElementQuery`](../xcuielementquery.md) conforms to the [`XCUIElementTypeQueryProvider`](../xcuielementtypequeryprovider.md) protocol, you can use the protocol’s properties as shorthand for calling [`descendants(matching:)`](./descendants%28matching%29.md) for different element types. For example, rather than calling `query.descendants(matching: .button)`, you can use the [`buttons`](../xcuielementtypequeryprovider/buttons.md) property from the protocol to retrieve `query.buttons`.

## Parameters

- `type`: The element type to match.

## See Also

### Creating new queries
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./children%28matching%29.md)
  Returns a new query that matches all direct children of the requested type.
- [func containing(NSPredicate) -> XCUIElementQuery](./containing%28_%29.md)
  Returns a new query that matches elements containing a descendant that meets the logical conditions of the provided predicate.
- [func containing(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./containing%28_,identifier%29.md)
  Returns a new query that matches elements that contain a descendant of the requested type and an identifying property that matches a provided identifier.
- [func matching(identifier: String) -> XCUIElementQuery](./matching%28identifier%29.md)
  Returns a new query that matches elements that have an identifying property that matches a provided identifier.
- [func matching(NSPredicate) -> XCUIElementQuery](./matching%28_%29.md)
  Returns a new query that matches elements that meet the logical conditions of the provided predicate.
- [func matching(XCUIElement.ElementType, identifier: String?) -> XCUIElementQuery](./matching%28_,identifier%29.md)
  Returns a new query that matches elements of the requested type and have an identifying property that matches a provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/descendants(matching:))*