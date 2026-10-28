# recognizedItems

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var recognizedItems: AsyncStream<[RecognizedItem]> { get }
```

## Discussion

You can use this property instead of the [`DataScannerViewControllerDelegate`](../datascannerviewcontrollerdelegate.md) protocol methods to track the recognized items in real time. To get the changes between arrays, use the [`difference(from:)`](../../Swift/array/difference%28from%29.md) method. For more information on asynchronous streams, see [Concurrency](../../Swift/concurrency.md).

Text items in this array appear in the reading order of the language and region.

## See Also

### Scanning and recognizing items
- [func startScanning() throws](./startscanning%28%29.md)
  Starts scanning the camera’s live video for data.
- [func stopScanning()](./stopscanning%28%29.md)
  Stops scanning the camera’s live video for data.
- [var isScanning: Bool](./isscanning.md)
  A Boolean value that indicates whether the data scanner is actively looking for items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeditems)*