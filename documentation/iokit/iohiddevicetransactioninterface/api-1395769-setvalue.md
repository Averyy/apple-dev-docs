# setValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the transaction value for an element in this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setValue)(void *self, IOHIDElementRef element, IOHIDValueRef value, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

This method is intended for use with transaction of direction kIOHIDTransactionDirectionTypeOutput. Use the kIOHIDTransactionOptionDefaultOutputValue option to set the default element value.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `element`: IOHIDElementRef referencing the element of interest.
- `value`: IOHIDValueRef referencing element value to be used in the transaction.
- `options`: See IOHIDTransactionOption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395769-setvalue)*