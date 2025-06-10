# init(functionName:fromMetalLibraryData:outputPixelFormat:)

**Framework**: Core Image  
**Kind**: init

Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(functionName name: String, fromMetalLibraryData data: Data, outputPixelFormat format: CIFormat) throws
```

#### Discussion

This method allows you to use MSL as the shader language for a Core Image kernel. Since MSL based kernels are precompiled, initializing them is faster than their than Core Image Kernel Language (CIKL) counterparts and Xcode can provide error diagnostics during development rather than at runtime. MSL is a more modern language than CIKL, and you can write shader code that uses arrays, structs and matrices.

MSL based kernels still support concatenation and tiling and can work in the same filter graph as traditional CIKL kernels.

## Parameters

- `name`: The name of the function in the Metal shading language.
- `data`: A metallib file compiled with the Core Image Standard Library.
- `format`: The pixel format of the output kernel.

## See Also

- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](cikernel/init(functionname:frommetallibrarydata:).md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [class func kernelNames(fromMetalLibraryData: Data) -> [String]](cikernel/kernelnames(frommetallibrarydata:).md)
  Return an array of strings containing the names of all of the kernels contained in the Metal library.
- [class func kernels(withMetalString: String) throws -> [CIKernel]](cikernel/kernels(withmetalstring:).md)
  Load kernels from a Metal language string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/init(functionname:frommetallibrarydata:outputpixelformat:))*