# maxKernelDiameter()

**Framework**: Metal Performance Shaders  
**Kind**: method

Queries the maximum diameter, in pixels, of the filter window supported by the median filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func maxKernelDiameter() -> Int
```

#### Return Value

Returns the maximum diameter, in pixels, of the filter window supported by the median filter.

## See Also

- [init(device: any MTLDevice, kernelDiameter: Int)](mpsimagemedian/init(device:kerneldiameter:).md)
  Initializes a filter for a particular kernel size and device.
- [class func minKernelDiameter() -> Int](mpsimagemedian/minkerneldiameter.md)
  Queries the minimum diameter, in pixels, of the filter window supported by the median filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/maxkerneldiameter())*