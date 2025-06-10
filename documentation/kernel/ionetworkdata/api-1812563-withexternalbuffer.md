# withExternalBuffer

**Framework**: Kernel  
**Kind**: instm

Factory method that constructs and initializes an IONetworkData object with an external data buffer.

## Declaration

```swift
static IONetworkData * withExternalBuffer(
 const char *name, 
 UInt32 bufferSize, 
 void *externalBuffer, 
 UInt32 accessTypes = (
 kIONetworkDataAccessTypeRead | kIONetworkDataAccessTypeSerialize), 
 void *target = 0, 
 Action action = 0, 
 void *param = 0);
```

#### Return_value

Returns an IONetworkData object on success, or 0 otherwise.

## Parameters

- `name`: A name to assign to this object.
- `bufferSize`: The size of the external data buffer.
- `externalBuffer`: Pointer to the external data buffer.
- `accessTypes`: The initial supported access types.
- `target`: The notification target.
- `action`: The notification action.
- `param`: A parameter to pass to the notification action.

## See Also

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
- [withInternalBuffer](ionetworkdata/1812581-withinternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an internal data buffer.
- [withNoBuffer](ionetworkdata/1812601-withnobuffer.md)
  Factory method that constructs and initializes an IONetworkData object without a data buffer.
- [write](ionetworkdata/1812620-write.md)
  An access method that writes to the data buffer.
- [writeBytes](ionetworkdata/1812640-writebytes.md)
  Writes to the data buffer with data from a source buffer provided by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkdata/1812563-withexternalbuffer)*