# IOUserVideoObject

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoObject;
```

#### Overview

Base class for all IOUserVideo* based objects.

IOUserVideoObject should not be subclassed or allocated directly.

## Topics

### Creating a video object
- [init](iouservideoobject/init-853a8.md)
- [init](iouservideoobject/init-5dkv4.md)
### Freeing a video object
- [free](iouservideoobject/free.md)
### Getting information about the class
- [GetClassID](iouservideoobject/getclassid.md)
- [GetBaseClassID](iouservideoobject/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Working with object names
- [GetName](iouservideoobject/getname.md)
- [SetName](iouservideoobject/setname.md)
### Working with object identifiers
- [GetObjectID](iouservideoobject/getobjectid.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
### Working with elements
- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
- [SetElementCategoryName](iouservideoobject/setelementcategoryname.md)
- [GetElementName](iouservideoobject/getelementname.md)
- [SetElementName](iouservideoobject/setelementname.md)
- [GetElementNumberName](iouservideoobject/getelementnumbername.md)
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)
### Using custom properties
- [AddCustomProperty](iouservideoobject/addcustomproperty.md)
- [RemoveCustomProperty](iouservideoobject/removecustomproperty.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
### Working with queues
- [GetWorkQueue](iouservideoobject/getworkqueue.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)
### Inherited By
- [IOUserVideoBox](iouservideobox.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
- [IOUserVideoControl](iouservideocontrol.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
- [IOUserVideoStream](iouservideostream.md)

## See Also

- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject)*