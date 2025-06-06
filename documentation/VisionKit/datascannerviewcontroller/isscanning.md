# isScanning

**Framework**: Visionkit  
**Kind**: property

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

- [func startScanning() throws](datascannerviewcontroller/startscanning.md)
  Starts scanning the camera’s live video for data.
- [func stopScanning()](datascannerviewcontroller/stopscanning.md)
  Stops scanning the camera’s live video for data.
- [var recognizedItems: AsyncStream<[RecognizedItem]>](datascannerviewcontroller/recognizeditems.md)
  An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/isscanning)*