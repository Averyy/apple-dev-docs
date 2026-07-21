# IOUserVideoObjectPropertyElement

**Framework**: VideoDriverKit  
**Kind**: typealias

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
typedef uint32_t IOUserVideoObjectPropertyElement;
```

#### Discussion

An IOUserVideoObjectPropertyElement is an integer that identifies, along with the IOUserVideoObjectPropertySelector and IOUserVideoObjectPropertyScope, a specific piece of information about an IOUserVideoObject.

The element selects one of possibly many items in the section of the object in which to look for the property. Elements are number sequentially where 0 represents the main element. Elements are particular to an instance of a class, meaning that two instances can have different numbers of elements in the same scope. There is no inheritance of elements.

## See Also

- [Create](iouservideobooleancontrol/create.md)
- [init](iouservideobooleancontrol/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyelement)*