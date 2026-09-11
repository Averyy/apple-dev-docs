# IOUserVideoObject

**Framework**: VideoDriverKit  
**Kind**: class

The base class for all video objects.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
class IOUserVideoObject;
```

#### Overview

Don’t subclass `IOUserVideoObject` or allocate it directly.

## Topics

### Creating a video object
- [init](iouservideoobject/init-853a8.md)
- [init](iouservideoobject/init-5dkv4.md)
### Freeing a video object
- [free](iouservideoobject/free.md)
  Frees the video object.
### Getting information about the class
- [GetClassID](iouservideoobject/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideoobject/getbaseclassid.md)
  Gets the class identifier of the object’s base class.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Working with object names
- [GetName](iouservideoobject/getname.md)
  Gets the name of the video object.
- [SetName](iouservideoobject/setname.md)
  Sets the name of the video object.
### Working with object identifiers
- [GetObjectID](iouservideoobject/getobjectid.md)
  Gets the video object identifier of the object.
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
### Working with elements
- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
  Gets the category name for the given element and scope of the video object.
- [SetElementCategoryName](iouservideoobject/setelementcategoryname.md)
  Sets the category name for the given element and scope of the video object.
- [GetElementName](iouservideoobject/getelementname.md)
  Gets the name for the given element and scope of the video object.
- [SetElementName](iouservideoobject/setelementname.md)
  Sets the name for the given element and scope of the video object.
- [GetElementNumberName](iouservideoobject/getelementnumbername.md)
  Gets the number name for the given element and scope of the video object.
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)
  Sets the number name for the given element of the video object.
### Using custom properties
- [AddCustomProperty](iouservideoobject/addcustomproperty.md)
  Adds an custom property object to this object.
- [RemoveCustomProperty](iouservideoobject/removecustomproperty.md)
  Removes a custom property from the video object.
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.
### Working with queues
- [GetWorkQueue](iouservideoobject/getworkqueue.md)
  Gets the work queue created by the video object.

## Relationships

### Inherits From
- [OSObject](../driverkit/osobject.md)
### Inherited By
- [IOUserVideoBox](iouservideobox.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
- [IOUserVideoControl](iouservideocontrol.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
- [IOUserVideoStream](iouservideostream.md)

## See Also

- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject)*