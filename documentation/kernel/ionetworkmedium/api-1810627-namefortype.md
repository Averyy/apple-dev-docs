# nameForType

**Framework**: Kernel  
**Kind**: instm

Creates a name that describes a medium type.

## Declaration

```c
static const OSSymbol * nameForType(
 IOMediumTypetype);
```

## Return Value

Returns an OSSymbol object is created based on the type provided.

## Overview

Given a medium type, creates an OSymbol object that describes the medium type. There is a 1-to-1 mapping between the medium type, and the medium name created by this method. The caller is responsible for releasing the OSSymbol object returned.

## Parameters

- `type`: A medium type. See IONetworkMedium.h for type encoding.

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
- [medium](./api-1810580-medium.md)
  Factory method that allocates and initializes an IONetworkMedium object.
- [removeMedium](./api-1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](./api-1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810627-namefortype)*