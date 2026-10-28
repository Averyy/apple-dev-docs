# getValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the transaction value for an element in this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getValue)(void *self, IOHIDElementRef element, IOHIDValueRef *pValue, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

Use the kIOHIDTransactionOptionDefaultOutputValue option to get the default element value.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `element`: IOHIDElementRef referencing the element of interest.
- `pValue`: Pointer to an IOHIDValueRef to return the element value of the transaction.
- `options`: See IOHIDTransactionOption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395697-getvalue)*