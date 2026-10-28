# replyTransactionType

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Specifies one of four possible reply transaction types. 

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOOptionBits replyTransactionType;
```

## Discussion

The following types of transaction are defined for the reply part of the request:

| `kIOI2CNoTransactionType` | No reply transaction to perform. |
| --- | --- |
| `kIOI2CSimpleTransactionType` | Simple I2C message. |
| `kIOI2CDDCciReplyTransactionType` | DDC/ci message (with embedded length). See VESA DDC/ci specification. |
| `kIOI2CCombinedTransactionType` | Combined format I2C R/~W transaction. |

## See Also

### Fields
- [__reservedA](../ioi2cinterface_h_user-space/ioi2crequest/api-1812650-_reserveda.md)
  Set to zero.
- [result](./api-1410361-result.md)
  The result of the transaction. Common errors are kIOReturnNoDevice if there is no device responding at the given address, kIOReturnUnsupportedMode if the type of transaction is unsupported on the requested bus.
- [completion](./api-1410371-completion.md)
  A completion routine to be executed when the request completes. If NULL is passed, the request is synchronous, otherwise it may execute asynchronously.
- [commFlags](./api-1410364-commflags.md)
  Flags that modify the I2C transaction type. 
- [minReplyDelay](./api-1410394-minreplydelay.md)
  Minimum delay as absolute time between send and reply transactions.
- [sendAddress](./api-1410312-sendaddress.md)
  I2C address to write.
- [sendSubAddress](./api-1410339-sendsubaddress.md)
  I2C subaddress to write.
- [__reservedB](../ioi2cinterface_h_user-space/ioi2crequest/api-1812670-_reservedb.md)
  Set to zero.
- [sendTransactionType](./api-1410320-sendtransactiontype.md)
  Specifies one of three possible transaction types. 
- [sendBuffer](./api-1410343-sendbuffer.md)
  Pointer to the send buffer.
- [sendBytes](./api-1410347-sendbytes.md)
  Number of bytes to send. Set to actual bytes sent on completion of the request.
- [replyAddress](./api-1410325-replyaddress.md)
  I2C Address from which to read.
- [replySubAddress](./api-1410358-replysubaddress.md)
  I2C Address from which to read.
- [__reservedC](../ioi2cinterface_h_user-space/ioi2crequest/api-1812697-_reservedc.md)
  Set to zero.
- [replyBuffer](./api-1410352-replybuffer.md)
  Pointer to the reply buffer.
- [replyBytes](./api-1410355-replybytes.md)
  Max bytes to reply (size of replyBuffer). Set to actual bytes received on completion of the request.
- [__reservedD](../ioi2cinterface_h_user-space/ioi2crequest/api-1812723-_reservedd.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioi2crequest/1410310-replytransactiontype)*