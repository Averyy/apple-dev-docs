# setDepth

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the depth for this IOHIDDeviceQueueInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setDepth)(void *self, uint32_t depth, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

Regardless of element value size, queue will guarantee n=depth elements will be serviced.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `depth`: The maximum number of elements in the queue before the oldest elements in the queue begin to be lost.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395677-setdepth)*