# subscript(_:)

**Framework**: WebKit  
**Kind**: subscript

Accesses the item at the relative offset from the current item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
subscript(index: Int) -> WebPage.BackForwardList.Item? { get }
```

#### Return Value

The item at the specified offset from the current item, or `nil` if the index exceeds the limits of the list.

## Parameters

- `index`: The offset of the desired item from the current item. Specify   for the current item,    for the immediately preceding item,   for the immediately following item, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/subscript(_:))*