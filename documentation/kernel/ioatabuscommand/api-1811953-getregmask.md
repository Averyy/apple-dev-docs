# getRegMask

**Framework**: Kernel  
**Kind**: instm

get the register mask for desired regs

## Declaration

```cpp
virtual ataRegMask getRegMask(
 void );
```

## See Also

### Miscellaneous
- [allocateCmd](./api-1811850-allocatecmd.md)
  factory method to create an instance of this class used by subclasses of IOATADevice
- [executeCallback](./api-1811860-executecallback.md)
  call the completion callback function
- [getBuffer](./api-1811872-getbuffer.md)
  get pointer to the memory descriptor for this transaction
- [getByteCount](./api-1811883-getbytecount.md)
  return the byte count for this transaction to transfer.
- [getCallbackPtr](./api-1811895-getcallbackptr.md)
  return the callback pointer
- [getFlags](./api-1811906-getflags.md)
  return the flags for this command.
- [getOpcode](./api-1811919-getopcode.md)
  return the command opcode
- [getPacketData](./api-1811925-getpacketdata.md)
  return pointer to the array of packet data.
- [getPacketSize](./api-1811935-getpacketsize.md)
  return the size of atapi packet if any.
- [getPosition](./api-1811945-getposition.md)
  the position within the memory buffer for the transaction.
- [getTaskFilePtr](./api-1811963-gettaskfileptr.md)
  return the taskfile structure pointer.
- [getTimeoutMS](./api-1811972-gettimeoutms.md)
  return the timeout value for this command
- [getTransferChunkSize](./api-1811979-gettransferchunksize.md)
  number of bytes between interrupts.
- [getUnit](./api-1811986-getunit.md)
  return the unit id (0 primary, 1 secondary)
- [init](./api-1811993-init.md)
  Zeroes all data, returns false if allocation fails. protected.
- [setActualTransfer](./api-1811997-setactualtransfer.md)
  set the byte count of bytes actually transferred.
- [setCommandInUse](./api-1812002-setcommandinuse.md)
  mark the command as being in progress.
- [setResult](./api-1812006-setresult.md)
  set the result code
- [zeroCommand](./api-1812011-zerocommand.md)
  set to blank state, call prior to re-use of this object


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabuscommand/1811953-getregmask)*