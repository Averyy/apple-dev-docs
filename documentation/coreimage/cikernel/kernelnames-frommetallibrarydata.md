# kernelNames(fromMetalLibraryData:)

**Framework**: Core Image  
**Kind**: method

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

#### Return Value

An Array of strings containing the names of the kernels.

## Parameters

- `data`: Contents of the Metal library.

## See Also

- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](cikernel/init(functionname:frommetallibrarydata:).md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [convenience init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat) throws](cikernel/init(functionname:frommetallibrarydata:outputpixelformat:).md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernels(withMetalString: String) throws -> [CIKernel]](cikernel/kernels(withmetalstring:).md)
  Load kernels from a Metal language string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/kernelnames(frommetallibrarydata:))*