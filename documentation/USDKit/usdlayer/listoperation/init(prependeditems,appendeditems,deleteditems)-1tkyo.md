# init(prependedItems:appendedItems:deletedItems:)

**Framework**: USDKit  
**Kind**: init

Creates a list operation with the given prepended/appended/deleted items. Pass no arguments for an empty operation with no slots authored.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(prependedItems: [T] = [], appendedItems: [T] = [], deletedItems: [T] = [])
```

## Parameters

- `prependedItems`: Items to add to the front during composition.
- `appendedItems`: Items to add to the back during composition.
- `deletedItems`: Items to remove during composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation/init(prependeditems:appendeditems:deleteditems:)-1tkyo)*