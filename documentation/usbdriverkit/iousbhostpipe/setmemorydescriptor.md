# SetMemoryDescriptor

**Framework**: USBDriverKit  
**Kind**: method

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t SetMemoryDescriptor(IOMemoryDescriptor * memoryDescriptor, uint32_t index);
```

#### Return Value

KERN_SUCCESS is successful see IOReturn.h for error codes.

#### Discussion

Add a memory descriptor to the ring.

Caller must fill the ring starting at index 0. The entire ring must be populated up to index size-1

## Parameters

- `memoryDescriptor`: The memory descriptor associated with the ring index. Must not be NULL.
- `index`: Ring index to be populated


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/setmemorydescriptor)*