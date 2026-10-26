# dataScanner(_:didUpdate:allItems:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default, blank implementation for when the data scanner updates the geometry of an item it recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, didUpdate updatedItems: [RecognizedItem], allItems: [RecognizedItem])
```

## Parameters

- `dataScanner`: The data scanner that recognizes the item.
- `updatedItems`: The items with geometry that the data scanner changes.
- `allItems`: The current items that the data scanner tracks. Text items appear in the reading order of the language and region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:didupdate:allitems:)-9qhkj)*