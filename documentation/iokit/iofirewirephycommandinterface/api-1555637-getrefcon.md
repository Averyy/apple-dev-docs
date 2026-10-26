# GetRefCon

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the refcon associated with this command

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
void *(*GetRefCon)(IOFireWireLibCommandRef self);
```

#### Return Value

void

## Parameters

- `self`: A reference to the command

## See Also

### Miscellaneous
- [Cancel](./api-1555963-cancel.md)
  Cancel command execution
- [GetAckCode](./api-1555837-getackcode.md)
  Gets the most recently received ack code for this transaction.
- [GetBuffer](./api-1556113-getbuffer.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.
- [GetResponseCode](./api-1556006-getresponsecode.md)
  Gets the most recently received response code for this transaction.
- [GetStatus](./api-1556008-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555945-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1555665-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1555868-isexecuting.md)
  Is this command object currently executing?
- [SetBuffer](./api-1555906-setbuffer.md)
  Set the buffer where read data should be stored.
- [SetCallback](./api-1555788-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetDataQuads](./api-1555600-setdataquads.md)
  Set the 2 quadlets of data to be sent in a PHY packet.
- [SetFlags](./api-1555693-setflags.md)
  Set flags governing this command's execution.
- [SetGeneration](./api-1555822-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetMaxPacket](./api-1555974-setmaxpacket.md)
  Set the maximum size in bytes of packets transferred by this command.
- [SetMaxPacketSpeed](./api-1556048-setmaxpacketspeed.md)
  Gets the most recently received ack code for this transaction.
- [SetMaxRetryCount](./api-1556057-setmaxretrycount.md)
  Sets the maximum number of retries for this command.
- [SetRefCon](./api-1555770-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1555696-settarget.md)
  Set command target address
- [SetTimeoutDuration](./api-1555754-settimeoutduration.md)
  Sets the duration of the timeout for this command.
- [Submit](./api-1555655-submit.md)
- [SubmitWithRefconAndCallback](./api-1555620-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirephycommandinterface/1555637-getrefcon)*