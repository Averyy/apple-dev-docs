# IOATABusCommand

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOATABusCommand : IOATACommand
```

#### Overview

ATA Device (disk) drivers should use the superclass, IOATACommand and may not derive or use any subclass of IOATACommand.

IOATABusCommand is the subclass of IOATACommand used by IOATAControllers. Controller classes may override this class to provide additional fields as their needs dictate or may use this as a concrete class if it is sufficient.

IOATAControllers are always paired with specific IOATADevices and each specific subclass of IOATADevice is in turn the factory method for IOATACommands for use by disk drivers.

In this manner, mass-storage device drivers (disk drivers, clients of ATA bus controllers) see only the generalized interface of IOATADevice and the generalized interface of IOATACommand. This provides isolation from specific bus details for disk drivers and offers flexibility to controllers to add per-command fields and state variables for their own internal use.

## Topics

### Miscellaneous
- [allocateCmd](ioatabuscommand/1811850-allocatecmd.md)
  factory method to create an instance of this class used by subclasses of IOATADevice
- [executeCallback](ioatabuscommand/1811860-executecallback.md)
  call the completion callback function
- [getBuffer](ioatabuscommand/1811872-getbuffer.md)
  get pointer to the memory descriptor for this transaction
- [getByteCount](ioatabuscommand/1811883-getbytecount.md)
  return the byte count for this transaction to transfer.
- [getCallbackPtr](ioatabuscommand/1811895-getcallbackptr.md)
  return the callback pointer
- [getFlags](ioatabuscommand/1811906-getflags.md)
  return the flags for this command.
- [getOpcode](ioatabuscommand/1811919-getopcode.md)
  return the command opcode
- [getPacketData](ioatabuscommand/1811925-getpacketdata.md)
  return pointer to the array of packet data.
- [getPacketSize](ioatabuscommand/1811935-getpacketsize.md)
  return the size of atapi packet if any.
- [getPosition](ioatabuscommand/1811945-getposition.md)
  the position within the memory buffer for the transaction.
- [getRegMask](ioatabuscommand/1811953-getregmask.md)
  get the register mask for desired regs
- [getTaskFilePtr](ioatabuscommand/1811963-gettaskfileptr.md)
  return the taskfile structure pointer.
- [getTimeoutMS](ioatabuscommand/1811972-gettimeoutms.md)
  return the timeout value for this command
- [getTransferChunkSize](ioatabuscommand/1811979-gettransferchunksize.md)
  number of bytes between interrupts.
- [getUnit](ioatabuscommand/1811986-getunit.md)
  return the unit id (0 primary, 1 secondary)
- [init](ioatabuscommand/1811993-init.md)
  Zeroes all data, returns false if allocation fails. protected.
- [setActualTransfer](ioatabuscommand/1811997-setactualtransfer.md)
  set the byte count of bytes actually transferred.
- [setCommandInUse](ioatabuscommand/1812002-setcommandinuse.md)
  mark the command as being in progress.
- [setResult](ioatabuscommand/1812006-setresult.md)
  set the result code
- [zeroCommand](ioatabuscommand/1812011-zerocommand.md)
  set to blank state, call prior to re-use of this object
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [syncer](ioatabuscommand/syncer.md)
- [state](ioatabuscommand/state.md)
- [reserved](ioatabuscommand/reserved.md)
- [queueChain](ioatabuscommand/queuechain.md)
### Instance Methods
- [- executeCallback](ioatabuscommand/1580390-executecallback.md)
- [- getBuffer](ioatabuscommand/1580381-getbuffer.md)
- [- getByteCount](ioatabuscommand/1580392-getbytecount.md)
- [- getCallbackPtr](ioatabuscommand/1580383-getcallbackptr.md)
- [- getFlags](ioatabuscommand/1580380-getflags.md)
- [- getMetaClass](ioatabuscommand/1580394-getmetaclass.md)
- [- getOpcode](ioatabuscommand/1580399-getopcode.md)
- [- getPacketData](ioatabuscommand/1580409-getpacketdata.md)
- [- getPacketSize](ioatabuscommand/1580407-getpacketsize.md)
- [- getPosition](ioatabuscommand/1580410-getposition.md)
- [- getRegMask](ioatabuscommand/1580405-getregmask.md)
- [- getTaskFilePtr](ioatabuscommand/1580401-gettaskfileptr.md)
- [- getTimeoutMS](ioatabuscommand/1580389-gettimeoutms.md)
- [- getTransferChunkSize](ioatabuscommand/1580382-gettransferchunksize.md)
- [- getUnit](ioatabuscommand/1580408-getunit.md)
- [- init](ioatabuscommand/1580395-init.md)
- [- setActualTransfer](ioatabuscommand/1580387-setactualtransfer.md)
- [- setCommandInUse](ioatabuscommand/1580385-setcommandinuse.md)
- [- setResult](ioatabuscommand/1580393-setresult.md)
- [- zeroCommand](ioatabuscommand/1580404-zerocommand.md)
### Type Methods
- [+ allocateCmd](ioatabuscommand/1580386-allocatecmd.md)

## Relationships

### Inherits From
- [IOATACommand](ioatacommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabuscommand)*