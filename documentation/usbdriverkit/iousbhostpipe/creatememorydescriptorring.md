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

The ring must only be created once, and will be freed by the kernel driver when the pipe is destroyed.

## Parameters

- `size`: Size of the ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/creatememorydescriptorring)*