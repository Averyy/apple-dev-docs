# medium

**Framework**: Kernel  
**Kind**: instm

Factory method that allocates and initializes an IONetworkMedium object.

## Declaration

```c
static IONetworkMedium * medium(
 IOMediumType type, 
 UInt64 speed, 
 UInt32 flags = 0, 
 UInt32 index = 0, 
 const char *name = 0);
```

#### Return Value

Returns an IONetworkMedium instance on success, or 0 otherwise.

## Parameters

- `type`: The medium type, this value is encoded with bits defined in IONetworkMedium.h.
- `speed`: The maximum (or the only) link speed supported over this medium in units of bits per second.
- `flags`: An optional flag for the medium object. See IONetworkMedium.h for defined flags.
- `index`: An optional index number assigned by the owner. Drivers can use this to store an index to a media table in the driver, or it may map to a driver-defined media type.
- `name`: An optional name assigned to this medium object. If 0, then a name will be created based on the medium type by calling IONetworkMedium::nameForType(). Since the name of the medium is used as a key when inserted into a dictionary, the name chosen must be unique within the scope of the owner.

## See Also

### Miscellaneous
- [addMedium](./api-1810064-addmedium.md)
  Adds an IONetworkMedium object to a dictionary.
- [free](./api-1810085-free.md)
  Frees the IONetworkMedium object.
- [getFlags](./api-1810101-getflags.md)
- [getIndex](./api-1810123-getindex.md)
- [getKey](./api-1810155-getkey.md)
- [getMediumWithIndex](./api-1810208-getmediumwithindex.md)
  Finds a medium object from a dictionary with a given index.
- [getMediumWithType](./api-1810258-getmediumwithtype.md)
  Finds a medium object from a dictionary with a given type.
- [getName](./api-1810301-getname.md)
- [getSpeed](./api-1810359-getspeed.md)
- [getType](./api-1810404-gettype.md)
- [init](./api-1810453-init.md)
  Initializes an IONetworkMedium object.
- [isEqualTo(const IONetworkMedium *)](./api-1810500-isequalto.md)
  Tests for equality between two IONetworkMedium objects.
- [isEqualTo(const OSMetaClassBase *)](./api-1810544-isequalto.md)
  Tests for equality between a IONetworkMedium object and an OSObject.
- [nameForType](./api-1810627-namefortype.md)
  Creates a name that describes a medium type.
- [removeMedium](./api-1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](./api-1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810580-medium)*