# AEDesc

**Framework**: Core Services  
**Kind**: struct

Stores data and an accompanying descriptor type to formthe basic building block of all Apple Events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AEDesc
```

#### Overview

The Apple Event Manager uses one or more descriptors to constructApple event attributes and parameters, object specifiers, tokens,and many other types of data it works with. (Token is defined in [`AEDisposeToken(_:)`](1446783-aedisposetoken.md).) Adescriptor consists of an opaque data storage container and a descriptortype that identifies the type of the data stored in the descriptor.

The descriptor type is a structure of type `DescType`,which in turn is of data type `ResType`—thatis, a four-character code. [`Descriptor Type Constants`](apple_events/1542788-descriptor_type_constants.md) lists the constants for the basic descriptortypes used by the Apple Event Manager. For information about descriptortypes used with object specifiers, see [`Key Form and Descriptor Type Object Specifier Constants`](apple_events/1572731-key_form_and_descriptor_type_obj.md). 

##### 1770263

Prior to Carbon, the [`AEDataStorage`](aedatastorage.md) datatype was defined as follows:

```occ
typedef Handle AEDataStorage;
```

## Topics

### Initializers
- [init()](aedesc/1450256-init.md)
- [init(descriptorType: DescType, dataHandle: AEDataStorage!)](aedesc/1690318-init.md)
### Instance Properties
- [var dataHandle: AEDataStorage!](aedesc/1444550-datahandle.md)
  An opaque storage type that points to the storagefor the descriptor data. Your application doesn’t access thisdata directly—rather, it calls one of the functions [`AEGetDescDataSize(_:)`](1450119-aegetdescdatasize.md), [`AEGetDescData(_:_:_:)`](1444427-aegetdescdata.md), or [`AEReplaceDescData(_:_:_:_:)`](1446695-aereplacedescdata.md).See [`AEDataStorage`](aedatastorage.md).
- [var descriptorType: DescType](aedesc/1445749-descriptortype.md)
  A four-character code of type [`DescType`](desctype.md) that indicates the type ofdata in the structure. See [`DescType`](desctype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aedesc)*