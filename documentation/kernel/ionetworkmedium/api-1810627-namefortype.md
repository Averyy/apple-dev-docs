# nameForType

**Framework**: Kernel  
**Kind**: instm

Creates a name that describes a medium type.

## Declaration

```swift
static const OSSymbol * nameForType(
 IOMediumTypetype);
```

#### Return_value

Returns an OSSymbol object is created based on the type provided.

#### Overview

Given a medium type, creates an OSymbol object that describes the medium type. There is a 1-to-1 mapping between the medium type, and the medium name created by this method. The caller is responsible for releasing the OSSymbol object returned.

## Parameters

- `type`: A medium type. See IONetworkMedium.h for type encoding.

## See Also

- [addMedium](ionetworkmedium/1810064-addmedium.md)
  Adds an IONetworkMedium object to a dictionary.
- [free](ionetworkmedium/1810085-free.md)
  Frees the IONetworkMedium object.
- [getFlags](ionetworkmedium/1810101-getflags.md)
- [getIndex](ionetworkmedium/1810123-getindex.md)
- [getKey](ionetworkmedium/1810155-getkey.md)
- [getMediumWithIndex](ionetworkmedium/1810208-getmediumwithindex.md)
  Finds a medium object from a dictionary with a given index.
- [getMediumWithType](ionetworkmedium/1810258-getmediumwithtype.md)
  Finds a medium object from a dictionary with a given type.
- [getName](ionetworkmedium/1810301-getname.md)
- [getSpeed](ionetworkmedium/1810359-getspeed.md)
- [getType](ionetworkmedium/1810404-gettype.md)
- [init](ionetworkmedium/1810453-init.md)
  Initializes an IONetworkMedium object.
- [isEqualTo(const IONetworkMedium *)](ionetworkmedium/1810500-isequalto.md)
  Tests for equality between two IONetworkMedium objects.
- [isEqualTo(const OSMetaClassBase *)](ionetworkmedium/1810544-isequalto.md)
  Tests for equality between a IONetworkMedium object and an OSObject.
- [medium](ionetworkmedium/1810580-medium.md)
  Factory method that allocates and initializes an IONetworkMedium object.
- [removeMedium](ionetworkmedium/1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](ionetworkmedium/1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810627-namefortype)*