# kernelNames(fromMetalLibraryData:)

**Framework**: Core Image  
**Kind**: clm

Return an array of strings containing the names of all of the kernels contained in the Metal library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func kernelNames(fromMetalLibraryData data: Data) -> [String]
```

#### Return_value

An Array of strings containing the names of the kernels.

## Parameters

- `data`: Contents of the Metal library.

## See Also

- [init(functionName: String, fromMetalLibraryData: Data)](cikernel/2880194-init.md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat)](cikernel/2880195-init.md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernels(withMetalString: String) -> [CIKernel]](cikernel/3857565-kernels.md)
  Load kernels from a Metal language string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/3577535-kernelnames)*