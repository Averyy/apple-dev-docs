# init(prependedItems:appendedItems:deletedItems:)

**Framework**: USDKit  
**Kind**: init

Creates a list operation with the given prepended/appended/deleted items. Pass no arguments for an empty operation with no slots authored.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(prependedItems: [T] = [], appendedItems: [T] = [], deletedItems: [T] = [])
```

## Parameters

- `prependedItems`: Items to add to the front during composition.
- `appendedItems`: Items to add to the back during composition.
- `deletedItems`: Items to remove during composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation/init(prependeditems:appendeditems:deleteditems:))*