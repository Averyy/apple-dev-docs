# item(at:)

**Framework**: Webkit  
**Kind**: method

Returns the item at the relative offset from the current item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func item(at index: Int) -> WKBackForwardListItem?
```

#### Return Value

The item at the specified offset from the current item, or `nil` if the `index` exceeds the limits of the list.

## Parameters

- `index`: The offset of the desired item from the current item. Specify   for the current item,   for the immediately preceding item,   for the immediately following item, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist/item(at:))*