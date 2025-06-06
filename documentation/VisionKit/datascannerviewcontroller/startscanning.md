# startScanning()

**Framework**: Visionkit  
**Kind**: method

Starts scanning the camera’s live video for data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func startScanning() throws
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

## See Also

- [func stopScanning()](datascannerviewcontroller/stopscanning.md)
  Stops scanning the camera’s live video for data.
- [var isScanning: Bool](datascannerviewcontroller/isscanning.md)
  A Boolean value that indicates whether the data scanner is actively looking for items.
- [var recognizedItems: AsyncStream<[RecognizedItem]>](datascannerviewcontroller/recognizeditems.md)
  An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/startscanning())*