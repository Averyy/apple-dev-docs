# copyNextValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Dequeues a retained copy of an element value from the head of an IOHIDDeviceQueueInterface.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*copyNextValue)(void *self, IOHIDValueRef *pValue, uint32_t timeout, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnUnderrun if data is unavailble, or a kern_return_t if unsuccessful.

## Discussion

Because the value is a retained copy, it is up to the caller to release the value using CFRelease. Use with setValueCallback to avoid polling the queue for data.

## Parameters

- `self`: Pointer to the IOHIDDeviceQueueInterface.
- `pValue`: Pointer to a IOHIDValueRef to return the value at the head of the queue.
- `timeout`: Timeout in milliseconds before aborting an attempt to dequeue a value from the head of a queue.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395765-copynextvalue)*