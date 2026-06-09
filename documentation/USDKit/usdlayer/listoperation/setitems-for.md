# setItems(_:for:)

**Framework**: USDKit  
**Kind**: method

Sets the items in the given operation’s slot.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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