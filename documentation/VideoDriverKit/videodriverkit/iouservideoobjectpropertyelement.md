# IOUserVideoObjectPropertyElement

**Framework**: VideoDriverKit  
**Kind**: typealias

An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
typedef uint32_t IOUserVideoObjectPropertyElement;
```

#### Discussion

The element selects one of possibly many items in the section of the object in which to look for the property. Elements are number sequentially where 0 represents the main element. Elements are particular to an instance of a class, meaning that two instances can have different numbers of elements in the same scope. There is no inheritance of elements.

## See Also

- [Create](iouservideobooleancontrol/create.md)
  A static factory method that allocates and initializes a video Boolean control.
- [init](iouservideobooleancontrol/init.md)
  Initializes an IOUserVideoBooleanControl.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyelement)*