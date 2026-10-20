# isEqualTo(const OSMetaClassBase *)

**Framework**: Kernel  
**Kind**: instm

Tests for equality between a IONetworkMedium object and an OSObject.

## Declaration

```cpp
virtual bool isEqualTo(
 const OSMetaClassBase *obj) const;
```

#### Return Value

Returns true if equal, false otherwise.

#### Overview

The OSObject is considered equal to the IONetworkMedium object if the OSObject is an IONetworkMedium, and they have similar properties assigned to them during initialization.

## Parameters

- `obj`: An OSObject to test against an IONetworkMedium object.

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
- [medium](./api-1810580-medium.md)
  Factory method that allocates and initializes an IONetworkMedium object.
- [nameForType](./api-1810627-namefortype.md)
  Creates a name that describes a medium type.
- [removeMedium](./api-1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](./api-1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810544-isequalto)*