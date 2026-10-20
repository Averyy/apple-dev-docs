# getMediumWithIndex

**Framework**: Kernel  
**Kind**: instm

Finds a medium object from a dictionary with a given index.

## Declaration

```c
static IONetworkMedium * getMediumWithIndex(
 const OSDictionary *dict, 
 UInt32 index, 
 UInt32 mask = 0);
```

#### Return Value

Returns the first matching IONetworkMedium entry found, or 0 if no match was found.

#### Overview

This method iterates through a dictionary and returns an IONetworkMedium entry with the given index. An optional mask supplies the don't care bits.

## Parameters

- `dict`: The dictionary to look for a matching entry.
- `index`: Search for an entry with the given index.
- `mask`: The don't care bits in index. Defaults to 0, which implies that a perfect match is desired.

## See Also

### Miscellaneous
- [addMedium](./api-1810064-addmedium.md)
  Adds an IONetworkMedium object to a dictionary.
- [free](./api-1810085-free.md)
  Frees the IONetworkMedium object.
- [getFlags](./api-1810101-getflags.md)
- [getIndex](./api-1810123-getindex.md)
- [getKey](./api-1810155-getkey.md)
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
- [medium](./api-1810580-medium.md)
  Factory method that allocates and initializes an IONetworkMedium object.
- [nameForType](./api-1810627-namefortype.md)
  Creates a name that describes a medium type.
- [removeMedium](./api-1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](./api-1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810208-getmediumwithindex)*