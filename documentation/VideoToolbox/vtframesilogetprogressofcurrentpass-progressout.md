# VTFrameSiloGetProgressOfCurrentPass(_:progressOut:)

**Framework**: Videotoolbox  
**Kind**: func

Gets the progress of the current pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTFrameSiloGetProgressOfCurrentPass(_ silo: VTFrameSilo, progressOut: UnsafeMutablePointer<Float32>) -> OSStatus
```

#### Return Value

`kVTFrameSiloInvalidTimeRangeErr` if any time ranges are non-numeric, overlap or are not in ascending order.

#### Discussion

Calculates the current progress based on the most recent sample buffer added and the current pass time ranges.

## Parameters

- `silo`: The frame silo object.
- `progressOut`: Upon return, contains the progress of the current pass.

## See Also

- [func VTFrameSiloGetTypeID() -> CFTypeID](vtframesilogettypeid().md)
  Retrieves the Core Foundation type identifier for the frame silo object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesilogetprogressofcurrentpass(_:progressout:))*