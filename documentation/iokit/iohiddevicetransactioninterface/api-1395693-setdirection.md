# setDirection

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the direction for this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setDirection)(void *self, IOHIDTransactionDirectionType direction, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

Direction constants are declared in IOHIDTransactionDirectionType. Changing directions is useful when dealing with elements of type kIOHIDElementTypeFeature as you use the transaction to both set and get element values.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `direction`: Transaction direction of type IOHIDTransactionDirectionType.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395693-setdirection)*