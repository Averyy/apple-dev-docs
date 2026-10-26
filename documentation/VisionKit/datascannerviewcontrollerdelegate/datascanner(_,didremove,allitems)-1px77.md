# dataScanner(_:didRemove:allItems:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default, blank implementation for when the data scanner stops recognizing an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, didRemove removedItems: [RecognizedItem], allItems: [RecognizedItem])
```

## Parameters

- `dataScanner`: The data scanner that recognizes the item.
- `removedItems`: The items that the data scanner removes from the [`recognizedItems`](../datascannerviewcontroller/recognizeditems.md) property.
- `allItems`: The current items that the data scanner tracks. Text items appear in the reading order of the language and region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:didremove:allitems:)-1px77)*