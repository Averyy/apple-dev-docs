# descendants(matching:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Returns a query for all descendants of the element matching the type you specify.

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

## Discussion

Because [`XCUIElement`](../xcuielement.md) conforms to the [`XCUIElementTypeQueryProvider`](../xcuielementtypequeryprovider.md) protocol, you can use the protocol’s properties as shorthand for calling [`descendants(matching:)`](./descendants%28matching%29.md) for different element types. For example, rather than calling `table.descendants(matching: .cell)`, you can use the [`cells`](../xcuielementtypequeryprovider/cells.md) property from the protocol to retrieve `table.cells`.

## See Also

### Querying descendant elements
- [func children(matching: XCUIElement.ElementType) -> XCUIElementQuery](./children%28matching%29.md)
  Returns a query for all direct children of the element matching the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/descendants(matching:))*