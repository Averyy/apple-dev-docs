# readCount

**Framework**: Metal Performance Shaders  
**Kind**: instp

The number of times a temporary image may be read by a CNN kernel before its contents become undefined.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var readCount: Int { get set }
```

#### Discussion

Temporary images must release their underlying textures for reuse immediately after last use. In order to facilitate  and convenient memory recycling, each time a [`MPSTemporaryImage`](mpstemporaryimage.md) object is read by an `encode` method of an [`MPSCNNKernel`](https://developer.apple.comhttps://developer.apple.com/reference/metalperformanceshaders/mpscnnkernel) object, the value of its [`readCount`](mpstemporaryimage/2097546-readcount.md) property is automatically decremented. When the value of [`readCount`](mpstemporaryimage/2097546-readcount.md) reaches 0, the underlying texture is automatically made available and reusable to the framework for its own needs (and for other [`MPSTemporaryImage`](mpstemporaryimage.md) objects prior to return from the `encode` method). The contents of the underlying texture become undefined at this time. 

By default, the value of [`readCount`](mpstemporaryimage/2097546-readcount.md) is initialized to 1, indicating a temporary image that may be overwritten any number of times, but read only once.

You may change the value of [`readCount`](mpstemporaryimage/2097546-readcount.md) as desired to allow [`MPSCNNKernel`](https://developer.apple.comhttps://developer.apple.com/reference/metalperformanceshaders/mpscnnkernel) objects to read the [`MPSTemporaryImage`](mpstemporaryimage.md) object additional times. However, it is an error to change the value of [`readCount`](mpstemporaryimage/2097546-readcount.md) once it reaches 0 (it is also an error to read or write to a temporary image with a [`readCount`](mpstemporaryimage/2097546-readcount.md) value of 0). You may set the value of  [`readCount`](mpstemporaryimage/2097546-readcount.md) to 0 yourself to cause the underlying texture to be returned to the framework. Writing to a temporary image does not adjust the value of [`readCount`](mpstemporaryimage/2097546-readcount.md).

The Metal API Validation layer will assert if a temporary image is deallocated with a non-zero [`readCount`](mpstemporaryimage/2097546-readcount.md) value to help identify cases when resources are not returned promptly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097546-readcount)*