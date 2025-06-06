# makeKernels(source:)

**Framework**: Core Image  
**Kind**: clm

Creates and returns and array of  `CIKernel` objects.

**Availability**:
- iOS 8.0+ - Deprecated in 12.0
- iPadOS 8.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func makeKernels(source string: String) -> [CIKernel]?
```

#### Return_value

An array of  `CIKernel` objects. The array contains one `CIKernel` objects for each kernel routine in the supplied string. Each object in the array can be of class [`CIKernel`](cikernel.md), [`CIColorKernel`](cicolorkernel.md), or [`CIWarpKernel`](ciwarpkernel.md) depending on the corresponding routine specified in the Core Image Kernel Language source code string.

#### Discussion

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Parameters

- `s`: A program in the Core Image Kernel Language that contains one or more routines, each of which is marked using the   keyword.

## See Also

- [init?(source: String)](cikernel/1437796-init.md)
  Creates a single kernel object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/1437876-makekernels)*