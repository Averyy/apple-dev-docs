# CreateMemoryDescriptorRing

**Framework**: USBDriverKit  
**Kind**: method

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CreateMemoryDescriptorRing(uint32_t size);
```

#### Return Value

KERN_SUCCESS is successful see IOReturn.h for error codes.

#### Discussion

The ring size should be large enough to hold all the memory descriptors to be used with the pipe. The ring must only be created once, and will be freed by the kernel driver when the pipe is destroyed.

## Parameters

- `size`: Size of the ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/creatememorydescriptorring)*