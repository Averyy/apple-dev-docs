# MPSState

**Framework**: Metal Performance Shaders  
**Kind**: cl

An opaque data container for large storage in MPS CNN filters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSState : NSObject
```

#### Overview

Some MPS CNN kernels produce additional information beyond an [`MPSImage`](mpsimage.md). These may be pooling indices where the result came from, convolution weights, or other information not contained in the usual [`MPSImage`](mpsimage.md) result from a [`MPSCNNKernel`](mpscnnkernel.md). An [`MPSState`](mpsstate.md) object typically contains one or more expensive [`MTLResource`](https://developer.apple.com/documentation/metal/mtlresource) objects such as textures or buffers to store this information. It provides a base class with interfaces for managing this storage. Child classes may add additional functionality specific to their contents. 

Some [`MPSState`](mpsstate.md) objects are temporary. Temporary state objects, for example, [`MPSTemporaryImage`](mpstemporaryimage.md) and [`MPSTemporaryMatrix`](mpstemporarymatrix.md), are for very short lived storage, perhaps just a few lines of code within the scope of a single [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer). They are very efficient for storage, as several temporary objects can share the same memory over the course of a command buffer. This can improve both memory usage and time spent in the kernel wiring down memory and such. You may find that some large CNN tasks can not be computed without them, as nontemporary storage would simply take up too much memory. 

In exchange, the lifetime of the underlying storage in temporary [`MPSState`](mpsstate.md) objects needs to be carefully managed. ARC often waits until the end of scope to release objects. Temporary storage often needs to be released sooner than that. Consequently the lifetime of the data in the underlying Metal resources is managed by a [`readCount`](mpsstate/2867042-readcount.md) property. Each time a [`MPSCNNKernel`](mpscnnkernel.md) reads a temporary [`MPSState`](mpsstate.md) object the [`readCount`](mpsstate/2867042-readcount.md) is automatically decremented. When it reaches 0, the underlying storage is recycled for use by other MPS temporary objects, and the data is becomes undefined. If you need to consume the data multiple times, you should set the [`readCount`](mpsstate/2867042-readcount.md) to a larger number to prevent the data from becoming undefined. You may set the [`readCount`](mpsstate/2867042-readcount.md) to 0 yourself to return the storage to MPS, if for any reason, you realize that the [`MPSState`](mpsstate.md) object will no longer be used. 

The contents of a temporary [`MPSState`](mpsstate.md) object are only valid from creation to the time the [`readCount`](mpsstate/2867042-readcount.md) reaches 0. The data is only valid for the [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) on which it was created. Nontemporary [`MPSState`](mpsstate.md) objects are valid on any [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) on the same device until they are released. 

## Topics

### Instance Properties
- [var isTemporary: Bool](mpsstate/2867114-istemporary.md)
- [var label: String?](mpsstate/2867179-label.md)
- [var readCount: Int](mpsstate/2867042-readcount.md)
- [var resource: (any MTLResource)?](mpsstate/2942398-resource.md)
- [var resourceCount: Int](mpsstate/2947900-resourcecount.md)
### Initializers
- [init(device: any MTLDevice, bufferSize: Int)](mpsstate/2942392-init.md)
- [init(device: any MTLDevice, resourceList: MPSStateResourceList)](mpsstate/2947908-init.md)
- [init(device: any MTLDevice, textureDescriptor: MTLTextureDescriptor)](mpsstate/2942400-init.md)
- [init(resource: (any MTLResource)?)](mpsstate/2942390-init.md)
- [init(resources: [any MTLResource]?)](mpsstate/2947895-init.md)
### Instance Methods
- [func bufferSize(at: Int) -> Int](mpsstate/2947913-buffersize.md)
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?, for: MPSKernel, suggestedDescriptor: MPSImageDescriptor) -> MPSImageDescriptor](mpsstate/2942394-destinationimagedescriptor.md)
- [func resource(at: Int, allocateMemory: Bool) -> (any MTLResource)?](mpsstate/2947916-resource.md)
- [func resourceSize() -> Int](mpsstate/2942397-resourcesize.md)
- [func resourceType(at: Int) -> MPSStateResourceType](mpsstate/2947902-resourcetype.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsstate/2942396-synchronize.md)
- [func textureInfo(at: Int) -> MPSStateTextureInfo](mpsstate/2947899-textureinfo.md)
### Type Methods
- [class func temporaryState(with: any MTLCommandBuffer) -> Self](mpsstate/2942393-temporarystate.md)
- [class func temporaryState(with: any MTLCommandBuffer, bufferSize: Int) -> Self](mpsstate/2942391-temporarystate.md)
- [class func temporaryState(with: any MTLCommandBuffer, resourceList: MPSStateResourceList) -> Self](mpsstate/2947915-temporarystate.md)
- [class func temporaryState(with: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor) -> Self](mpsstate/2942395-temporarystate.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsstate)*