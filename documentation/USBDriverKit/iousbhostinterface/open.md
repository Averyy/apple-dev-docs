# Open

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Opens a session to the host interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t Open(IOService *forClient, IOOptionBits options, uint8_t *arg);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

This method opens a session to the [`IOUSBHostInterface`](../iousbhostinterface.md), and acquires the service’s workloop lock. Only one service at a time may open a session to the interface.

## Parameters

- `forClient`: The service object that is opening the session.
- `options`: The options to use when opening the session. Specify [`kUSBHostOpenOptionSelectAlternateSetting`](../../kernel/api-3143215-anonymous/kusbhostopenoptionselectalternatesetting.md) to select an alternative setting for this interface immediately. Specify the alternative setting in the `arg` parameter.
- `arg`: Additional arguments to the function. If you specify [`kUSBHostOpenOptionSelectAlternateSetting`](../../kernel/api-3143215-anonymous/kusbhostopenoptionselectalternatesetting.md) for the `options` parameter, use this value to specify the value for the alternative setting; otherwise, specify `NULL`.

## See Also

### Managing the Device Session
- [Close](./close.md)
  Closes the session to the host interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/open)*