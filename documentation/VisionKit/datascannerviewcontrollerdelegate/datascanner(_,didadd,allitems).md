# dataScanner(_:didAdd:allItems:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Responds when the data scanner starts recognizing an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, didAdd addedItems: [RecognizedItem], allItems: [RecognizedItem])
```

## Mentions

- [Scanning data with the camera](../scanning-data-with-the-camera.md)

#### Discussion

To identify an item in the `addedItems` and `allItems` parameters, use the item’s `id` property.

## Parameters

- `dataScanner`: The data scanner that recognizes the item.
- `addedItems`: The items that the data scanner starts tracking.
- `allItems`: The current items that the data scanner tracks. Text items appear in the reading order of the language and region.

## Default Implementations

### DataScannerViewControllerDelegate Implementations
- [func dataScanner(DataScannerViewController, didAdd: [RecognizedItem], allItems: [RecognizedItem])](./datascanner%28_,didadd,allitems%29-1go79.md)
  A default, blank implementation for when the data scanner starts recognizing an item.

## See Also

### Customizing highlighting
- [func dataScanner(DataScannerViewController, didUpdate: [RecognizedItem], allItems: [RecognizedItem])](./datascanner%28_,didupdate,allitems%29.md)
  Responds when the data scanner updates the geometry of an item it recognizes.
- [func dataScanner(DataScannerViewController, didRemove: [RecognizedItem], allItems: [RecognizedItem])](./datascanner%28_,didremove,allitems%29.md)
  Responds when the data scanner stops recognizing an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:didadd:allitems:))*