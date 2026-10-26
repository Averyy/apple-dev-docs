# contentsRect(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default unit rectangle that represents the full size of the interaction view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentsRect(for interaction: ImageAnalysisInteraction) -> CGRect
```

#### Return Value

A unit rectangle with origin `(0, 0)` and the same width and height as the interaction view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/contentsrect(for:)-90dek)*