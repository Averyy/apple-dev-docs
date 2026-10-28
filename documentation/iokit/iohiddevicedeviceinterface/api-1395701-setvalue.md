# setValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the value for an element.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setValue)(void *self, IOHIDElementRef element, IOHIDValueRef value, uint32_t timeout, IOHIDValueCallback callback, void *context, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

If setting multiple element values, please consider using an IOHIDDeviceTransactionInterface with the kIOHIDTransactionDirectionTypeOutput direction.

**Note:** In order to make use of asynchronous behavior, the event source obtained using getAsyncEventSource must be added to a run loop.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `element`: IOHIDElementRef referencing the element of interest.
- `value`: IOHIDValueRef containing element value to be set.
- `timeout`: Time in milliseconds to wait before aborting request.
- `callback`: Callback of type IOHIDValueCallback to be used after report data has been sent to the device. If null, this method will behave synchronously.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395701-setvalue)*