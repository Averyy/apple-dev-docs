# kernels(withMetalString:)

**Framework**: Core Image  
**Kind**: clm

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

#### Return_value

An array of [`CIKernel`](cikernel.md) objects.

## Parameters

- `source`: A string containing the progam in Metal language.

## See Also

- [init(functionName: String, fromMetalLibraryData: Data)](cikernel/2880194-init.md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat)](cikernel/2880195-init.md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernelNames(fromMetalLibraryData: Data) -> [String]](cikernel/3577535-kernelnames.md)
  Return an array of strings containing the names of all of the kernels contained in the Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/3857565-kernels)*