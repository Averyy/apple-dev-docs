# dataScannerDidZoom(_:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Responds when a person or your code changes the zoom factor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScannerDidZoom(_ dataScanner: DataScannerViewController)
```

#### Discussion

The data scanner invokes this method when the [`zoomFactor`](datascannerviewcontroller/zoomfactor.md) property changes.

## Parameters

- `dataScanner`: The data scanner whose zoom factor changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascannerdidzoom(_:))*