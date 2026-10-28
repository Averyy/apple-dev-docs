# IONetworkData

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An object that manages a fixed-size named buffer.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IONetworkData : OSObject
```

## Overview

An IONetworkData object manages a fixed-size named buffer. This object provides external access methods that can be used to access the contents of the data buffer. In addition, serialization is supported, and therefore this object can be added to a property table to publish the data object. An unique name must be assigned to the object during initialization. An OSSymbol key will be created based on the assigned name, and this key can be used when the object is added to a dictionary.

The level of access granted to the access methods can be restricted, by specifying a set of supported access types when the object is initialized, or modified later by calling setAccessTypes(). By default, each IONetworkData object created will support serialization, and will also allow its data buffer to be read through the read() access method.

An access notification handler, in the form of a 'C' function, can be registered to receive a call each time the data buffer is accessed through an access method. Arguments provided to the handler will identify the data object and the type of access that triggered the notification. The handler can therefore perform lazy update of the data buffer until an interested party tries to read or serialize the data. The notification handler can also take over the default action performed by the access methods when the buffer type is set to kIONetworkDataBufferTypeNone. This will prevent the access methods from accessing the data buffer, and allow the handler to override the access protocol.

This object is primarily used by IONetworkInterface to export interface properties to user space.

## Topics

### Miscellaneous
- [clearBuffer](./ionetworkdata/api-1812449-clearbuffer.md)
  Clears the data buffer by filling it with zeroes.
- [free](./ionetworkdata/api-1812455-free.md)
  Frees the IONetworkData object.
- [getAccessTypes](./ionetworkdata/api-1812461-getaccesstypes.md)
  Gets the types of data access supported by this object.
- [getBuffer](./ionetworkdata/api-1812470-getbuffer.md)
  Gets a pointer to the data buffer.
- [getBufferType](./ionetworkdata/api-1812479-getbuffertype.md)
  Gets the type of data buffer managed by this object.
- [getKey](./ionetworkdata/api-1812486-getkey.md)
  Gets a unique OSSymbol key associated with this object.
- [getNotificationAction](./ionetworkdata/api-1812491-getnotificationaction.md)
  Gets the C function that was registered to handle access notifications sent from this object.
- [getNotificationParameter](./ionetworkdata/api-1812494-getnotificationparameter.md)
  Gets the parameter that will be passed to the access notification handler.
- [getNotificationTarget](./ionetworkdata/api-1812497-getnotificationtarget.md)
  Gets the first parameter that will be passed to the access notification handler.
- [getSize](./ionetworkdata/api-1812500-getsize.md)
  Gets the size of the data buffer.
- [init](./ionetworkdata/api-1812508-init.md)
  Initializes an IONetworkData object.
- [read](./ionetworkdata/api-1812511-read.md)
  An access method that reads from the data buffer.
- [readBytes](./ionetworkdata/api-1812517-readbytes.md)
  Reads from the data buffer and copies the data to a destination buffer provided by the caller.
- [reset](./ionetworkdata/api-1812524-reset.md)
  An access method that resets the data buffer.
- [serialize](./ionetworkdata/api-1812531-serialize.md)
  Serializes the IONetworkData object.
- [setAccessTypes](./ionetworkdata/api-1812540-setaccesstypes.md)
  Sets the types of access that are permitted on the data buffer.
- [setNotificationTarget](./ionetworkdata/api-1812552-setnotificationtarget.md)
  Registers a C function to handle access notifications sent from this object.
- [withExternalBuffer](./ionetworkdata/api-1812563-withexternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an external data buffer.
- [withInternalBuffer](./ionetworkdata/api-1812581-withinternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an internal data buffer.
- [withNoBuffer](./ionetworkdata/api-1812601-withnobuffer.md)
  Factory method that constructs and initializes an IONetworkData object without a data buffer.
- [write](./ionetworkdata/api-1812620-write.md)
  An access method that writes to the data buffer.
- [writeBytes](./ionetworkdata/api-1812640-writebytes.md)
  Writes to the data buffer with data from a source buffer provided by the caller.
### Callbacks
- [Action](./ioworkloop/action.md)
### Instance Variables
- [_reserved](./ionetworkdata/reserved.md)
### Instance Methods
- [- clearBuffer](./ionetworkdata/api-1423489-clearbuffer.md)
- [- free](./ionetworkdata/api-1423516-free.md)
- [- getAccessTypes](./ionetworkdata/api-1423495-getaccesstypes.md)
- [- getBuffer](./ionetworkdata/api-1423536-getbuffer.md)
- [- getBufferType](./ionetworkdata/api-1423520-getbuffertype.md)
- [- getKey](./ionetworkdata/api-1423503-getkey.md)
- [- getMetaClass](./ionetworkdata/api-1423545-getmetaclass.md)
- [- getNotificationAction](./ionetworkdata/api-1423510-getnotificationaction.md)
- [- getNotificationParameter](./ionetworkdata/api-1423551-getnotificationparameter.md)
- [- getNotificationTarget](./ionetworkdata/api-1423527-getnotificationtarget.md)
- [- getSize](./ionetworkdata/api-1423554-getsize.md)
- [- init](./ionetworkdata/api-1423497-init.md)
- [- read](./ionetworkdata/api-1423529-read.md)
- [- readBytes](./ionetworkdata/api-1423512-readbytes.md)
- [- reset](./ionetworkdata/api-1423534-reset.md)
- [- serialize](./ionetworkdata/api-1423501-serialize.md)
- [- setAccessTypes](./ionetworkdata/api-1423514-setaccesstypes.md)
- [- setNotificationTarget](./ionetworkdata/api-1423532-setnotificationtarget.md)
- [- write](./ionetworkdata/api-1423522-write.md)
- [- writeBytes](./ionetworkdata/api-1423491-writebytes.md)
### Type Methods
- [+ withExternalBuffer](./ionetworkdata/api-1423542-withexternalbuffer.md)
- [+ withInternalBuffer](./ionetworkdata/api-1423526-withinternalbuffer.md)
- [+ withNoBuffer](./ionetworkdata/api-1423538-withnobuffer.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

## See Also

### Network Data
- [IONetworkMedium](./ionetworkmedium.md)
  An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).
- [IOPacketQueue](./iopacketqueue.md)
  Implements a bounded FIFO queue of mbuf packets.
- [IOPacketBufferConstraints](./iopacketbufferconstraints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkdata)*