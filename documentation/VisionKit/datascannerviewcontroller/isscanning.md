# isScanning

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the data scanner is actively looking for items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isScanning: Bool { get }
```

## See Also

### Scanning and recognizing items
- [func startScanning() throws](./startscanning%28%29.md)
  Starts scanning the camera’s live video for data.
- [func stopScanning()](./stopscanning%28%29.md)
  Stops scanning the camera’s live video for data.
- [var recognizedItems: AsyncStream<[RecognizedItem]>](./recognizeditems.md)
  An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/isscanning)*