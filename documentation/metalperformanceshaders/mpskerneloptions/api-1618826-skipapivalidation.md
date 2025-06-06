# skipAPIValidation

**Framework**: Metal Performance Shaders  
**Kind**: structdata

A property that directs the kernel to perform or skip argument validation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var skipAPIValidation: MPSKernelOptions { get }
```

#### Discussion

Most kernels double-check their arguments. This has a small but nonzero CPU cost. Setting this option, however, does not skip checks for memory allocation failure. Turning on this option can result in undefined behavior if the requested operation cannot be completed for some reason. Most error states will be passed through to Metal, which may do nothing or abort the program if Metal API validation is turned on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1618826-skipapivalidation)*