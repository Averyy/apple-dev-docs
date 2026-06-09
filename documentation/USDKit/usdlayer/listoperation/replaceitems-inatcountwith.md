# replaceItems(in:at:count:with:)

**Framework**: USDKit  
**Kind**: method

Replaces `count` items in `operation`’s slot starting at `index` with `newItems`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func replaceItems(in operation: USDLayer.ListOperationType, at index: Int, count: Int, with newItems: [T]) throws
```

#### Discussion

> **Note**: An error if the range is out of bounds.

## Parameters

- `operation`: The slot to update.
- `index`: The starting index of the range to replace.
- `count`: The number of items to replace.
- `newItems`: The replacement items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation/replaceitems(in:at:count:with:))*