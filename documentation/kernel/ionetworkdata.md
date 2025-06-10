# IONetworkData

**Framework**: Kernel  
**Kind**: cl

An object that manages a fixed-size named buffer.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IONetworkData : OSObject
```

#### Overview

An IONetworkData object manages a fixed-size named buffer. This object provides external access methods that can be used to access the contents of the data buffer. In addition, serialization is supported, and therefore this object can be added to a property table to publish the data object. An unique name must be assigned to the object during initialization. An OSSymbol key will be created based on the assigned name, and this key can be used when the object is added to a dictionary.

The level of access granted to the access methods can be restricted, by specifying a set of supported access types when the object is initialized, or modified later by calling setAccessTypes(). By default, each IONetworkData object created will support serialization, and will also allow its data buffer to be read through the read() access method.

An access notification handler, in the form of a 'C' function, can be registered to receive a call each time the data buffer is accessed through an access method. Arguments provided to the handler will identify the data object and the type of access that triggered the notification. The handler can therefore perform lazy update of the data buffer until an interested party tries to read or serialize the data. The notification handler can also take over the default action performed by the access methods when the buffer type is set to kIONetworkDataBufferTypeNone. This will prevent the access methods from accessing the data buffer, and allow the handler to override the access protocol.

This object is primarily used by IONetworkInterface to export interface properties to user space.

## Topics

### Miscellaneous
- [clearBuffer](ionetworkdata/1812449-clearbuffer.md)
  Clears the data buffer by filling it with zeroes.
- [free](ionetworkdata/1812455-free.md)
  Frees the IONetworkData object.
- [getAccessTypes](ionetworkdata/1812461-getaccesstypes.md)
  Gets the types of data access supported by this object.
- [getBuffer](ionetworkdata/1812470-getbuffer.md)
  Gets a pointer to the data buffer.
- [getBufferType](ionetworkdata/1812479-getbuffertype.md)
  Gets the type of data buffer managed by this object.
- [getKey](ionetworkdata/1812486-getkey.md)
  Gets a unique OSSymbol key associated with this object.
- [getNotificationAction](ionetworkdata/1812491-getnotificationaction.md)
  Gets the C function that was registered to handle access notifications sent from this object.
- [getNotificationParameter](ionetworkdata/1812494-getnotificationparameter.md)
  Gets the parameter that will be passed to the access notification handler.
- [getNotificationTarget](ionetworkdata/1812497-getnotificationtarget.md)
  Gets the first parameter that will be passed to the access notification handler.
- [getSize](ionetworkdata/1812500-getsize.md)
  Gets the size of the data buffer.
- [init](ionetworkdata/1812508-init.md)
  Initializes an IONetworkData object.
- [read](ionetworkdata/1812511-read.md)
  An access method that reads from the data buffer.
- [readBytes](ionetworkdata/1812517-readbytes.md)
  Reads from the data buffer and copies the data to a destination buffer provided by the caller.
- [reset](ionetworkdata/1812524-reset.md)
  An access method that resets the data buffer.
- [serialize](ionetworkdata/1812531-serialize.md)
  Serializes the IONetworkData object.
- [setAccessTypes](ionetworkdata/1812540-setaccesstypes.md)
  Sets the types of access that are permitted on the data buffer.
- [setNotificationTarget](ionetworkdata/1812552-setnotificationtarget.md)
  Registers a C function to handle access notifications sent from this object.
- [withExternalBuffer](ionetworkdata/1812563-withexternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an external data buffer.
- [withInternalBuffer](ionetworkdata/1812581-withinternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an internal data buffer.
- [withNoBuffer](ionetworkdata/1812601-withnobuffer.md)
  Factory method that constructs and initializes an IONetworkData object without a data buffer.
- [write](ionetworkdata/1812620-write.md)
  An access method that writes to the data buffer.
- [writeBytes](ionetworkdata/1812640-writebytes.md)
  Writes to the data buffer with data from a source buffer provided by the caller.
### Callbacks
- [Action](ioworkloop/action.md)
### Instance Variables
- [_reserved](ionetworkdata/reserved.md)
### Instance Methods
- [- clearBuffer](ionetworkdata/1423489-clearbuffer.md)
- [- free](ionetworkdata/1423516-free.md)
- [- getAccessTypes](ionetworkdata/1423495-getaccesstypes.md)
- [- getBuffer](ionetworkdata/1423536-getbuffer.md)
- [- getBufferType](ionetworkdata/1423520-getbuffertype.md)
- [- getKey](ionetworkdata/1423503-getkey.md)
- [- getMetaClass](ionetworkdata/1423545-getmetaclass.md)
- [- getNotificationAction](ionetworkdata/1423510-getnotificationaction.md)
- [- getNotificationParameter](ionetworkdata/1423551-getnotificationparameter.md)
- [- getNotificationTarget](ionetworkdata/1423527-getnotificationtarget.md)
- [- getSize](ionetworkdata/1423554-getsize.md)
- [- init](ionetworkdata/1423497-init.md)
- [- read](ionetworkdata/1423529-read.md)
- [- readBytes](ionetworkdata/1423512-readbytes.md)
- [- reset](ionetworkdata/1423534-reset.md)
- [- serialize](ionetworkdata/1423501-serialize.md)
- [- setAccessTypes](ionetworkdata/1423514-setaccesstypes.md)
- [- setNotificationTarget](ionetworkdata/1423532-setnotificationtarget.md)
- [- write](ionetworkdata/1423522-write.md)
- [- writeBytes](ionetworkdata/1423491-writebytes.md)
### Type Methods
- [+ withExternalBuffer](ionetworkdata/1423542-withexternalbuffer.md)
- [+ withInternalBuffer](ionetworkdata/1423526-withinternalbuffer.md)
- [+ withNoBuffer](ionetworkdata/1423538-withnobuffer.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IONetworkMedium](ionetworkmedium.md)
  An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).
- [IOPacketQueue](iopacketqueue.md)
  Implements a bounded FIFO queue of mbuf packets.
- [IOPacketBufferConstraints](iopacketbufferconstraints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkdata)*