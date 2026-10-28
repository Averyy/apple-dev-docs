# stopScanning()

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Stops scanning the camera’s live video for data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func stopScanning()
```

## Mentions

- [Scanning data with the camera](../scanning-data-with-the-camera.md)

## Discussion

This method removes all items from the [`recognizedItems`](./recognizeditems.md) property.

## See Also

### Scanning and recognizing items
- [func startScanning() throws](./startscanning%28%29.md)
  Starts scanning the camera’s live video for data.
- [var isScanning: Bool](./isscanning.md)
  A Boolean value that indicates whether the data scanner is actively looking for items.
- [var recognizedItems: AsyncStream<[RecognizedItem]>](./recognizeditems.md)
  An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/stopscanning())*