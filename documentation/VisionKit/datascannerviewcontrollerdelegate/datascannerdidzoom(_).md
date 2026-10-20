# dataScannerDidZoom(_:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
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

The data scanner invokes this method when the [`zoomFactor`](../datascannerviewcontroller/zoomfactor.md) property changes.

## Parameters

- `dataScanner`: The data scanner whose zoom factor changes.

## Default Implementations

### DataScannerViewControllerDelegate Implementations
- [func dataScannerDidZoom(DataScannerViewController)](./datascannerdidzoom%28_%29-5lq2p.md)
  A default, blank implementation for when a person or your code changes the zoom factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascannerdidzoom(_:))*