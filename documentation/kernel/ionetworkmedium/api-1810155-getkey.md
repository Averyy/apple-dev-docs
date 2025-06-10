# getKey

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual const OSSymbol * getKey() const;
```

#### Return_value

Returns the key to use for this medium object. This key should be used when this object is added to a dictionary. Same as getName().

## See Also

- [addMedium](ionetworkmedium/1810064-addmedium.md)
  Adds an IONetworkMedium object to a dictionary.
- [free](ionetworkmedium/1810085-free.md)
  Frees the IONetworkMedium object.
- [getFlags](ionetworkmedium/1810101-getflags.md)
- [getIndex](ionetworkmedium/1810123-getindex.md)
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
- [nameForType](ionetworkmedium/1810627-namefortype.md)
  Creates a name that describes a medium type.
- [removeMedium](ionetworkmedium/1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](ionetworkmedium/1810690-serialize.md)
  Serializes the IONetworkMedium object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium/1810155-getkey)*