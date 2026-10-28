# commit

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Commits element transaction to an IOHIDDevice in this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*commit)(void *self, uint32_t timeout, IOHIDCallback callback, void *context, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

In regards to kIOHIDTransactionDirectionTypeOutput direction, default element values will be used if element values are not set. If neither are set, that element will be omitted from the commit. After a transaction is committed, transaction element values will be cleared and default values preserved.

**Note:** It is possible for elements from different reports to be present in a given transaction causing a commit to transcend multiple reports. Keep this in mind when setting a timeout.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `timeout`: Timeout in milliseconds for issuing the transaction.
- `callback`: Callback of type IOHIDCallback to be used when transaction has been completed. If null, this method will behave synchronously.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395785-commit)*