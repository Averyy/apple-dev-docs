# IONetworkMedium

**Framework**: Kernel  
**Kind**: cl

An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IONetworkMedium : OSObject
```

#### Overview

The main purpose of this object is for a network driver to advertise its media capability, through a collection of IONetworkMedium objects stored in a dictionary in its property table. IONetworkMedium supports serialization, and will encode its properties in the form of a dictionary to the serialization stream when instructed. This will allow a user-space application to browse the set of media types supported by the controller.

## Topics

### Miscellaneous
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
- [nameForType](ionetworkmedium/1810627-namefortype.md)
  Creates a name that describes a medium type.
- [removeMedium](ionetworkmedium/1810658-removemedium.md)
  Removes an IONetworkMedium object from a dictionary.
- [serialize](ionetworkmedium/1810690-serialize.md)
  Serializes the IONetworkMedium object.
### Instance Variables
- [_reserved](ionetworkmedium/reserved.md)
### Instance Methods
- [- getKey](1534574-getkey.md)
- [- free](ionetworkmedium/1534639-free.md)
- [- getFlags](ionetworkmedium/1534590-getflags.md)
- [- getIndex](ionetworkmedium/1534682-getindex.md)
- [- getMetaClass](ionetworkmedium/1534597-getmetaclass.md)
- [- getName](ionetworkmedium/1534678-getname.md)
- [- getSpeed](ionetworkmedium/1534617-getspeed.md)
- [- getType](ionetworkmedium/1534641-gettype.md)
- [- init](ionetworkmedium/1534606-init.md)
- [- isEqualTo](ionetworkmedium/1534577-isequalto.md)
- [- isEqualTo](ionetworkmedium/3516616-isequalto.md)
- [- serialize](ionetworkmedium/1534647-serialize.md)
### Type Methods
- [+ addMedium](ionetworkmedium/1534619-addmedium.md)
- [+ getMediumWithIndex](ionetworkmedium/1534655-getmediumwithindex.md)
- [+ getMediumWithType](ionetworkmedium/1534652-getmediumwithtype.md)
- [+ medium](ionetworkmedium/1534687-medium.md)
- [+ nameForType](ionetworkmedium/1534630-namefortype.md)
- [+ removeMedium](ionetworkmedium/1534692-removemedium.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IONetworkData](ionetworkdata.md)
  An object that manages a fixed-size named buffer.
- [IOPacketQueue](iopacketqueue.md)
  Implements a bounded FIFO queue of mbuf packets.
- [IOPacketBufferConstraints](iopacketbufferconstraints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkmedium)*