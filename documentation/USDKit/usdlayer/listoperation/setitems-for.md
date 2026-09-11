# setItems(_:for:)

**Framework**: USDKit  
**Kind**: method

Sets the items in the given operation’s slot.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func setItems(_ items: [T], for operation: USDLayer.ListOperationType) throws
```

#### Discussion

> **Note**: An error if any item fails validation.

## Parameters

- `items`: The new items.
- `operation`: The slot to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation/setitems(_:for:))*