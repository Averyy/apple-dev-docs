# kernelHeight

**Framework**: Metal Performance Shaders  
**Kind**: instp

The height of the kernel window.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var kernelHeight: Int { get set }
```

#### Discussion

The default value is `3`.

Any positive non-zero value is valid, including even values. The position of the top edge of the kernel window is given by `offset.y - (kernelHeight>>1)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648904-kernelheight)*