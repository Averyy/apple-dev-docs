# kernels(withMetalString:)

**Framework**: Core Image  
**Kind**: method

Load kernels from a Metal language string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func kernels(withMetalString source: String) throws -> [CIKernel]
```

#### Return Value

An array of [`CIKernel`](cikernel.md) objects.

## Parameters

- `source`: A string containing the progam in Metal language.

## See Also

- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](cikernel/init(functionname:frommetallibrarydata:).md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [convenience init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat) throws](cikernel/init(functionname:frommetallibrarydata:outputpixelformat:).md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernelNames(fromMetalLibraryData: Data) -> [String]](cikernel/kernelnames(frommetallibrarydata:).md)
  Return an array of strings containing the names of all of the kernels contained in the Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/kernels(withmetalstring:))*