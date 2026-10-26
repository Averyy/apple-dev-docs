# computeDevice(for:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the compute device for a compute stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
func computeDevice(for computeStage: ComputeStage) -> MLComputeDevice?
```

#### Return Value

The current compute device; otherwise, `nil` if one isn’t assigned.

#### Discussion

- `computeStage: `The compute stage to inspect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionrequest/computedevice(for:)-52l0g)*