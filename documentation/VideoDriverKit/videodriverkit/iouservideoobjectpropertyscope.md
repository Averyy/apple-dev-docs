# IOUserVideoObjectPropertyScope

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoObjectPropertyScope : uint32_t;
```

#### Overview

An IOUserVideoObjectPropertyScope is a four char code that identifies, along with the IOUserVideoObjectPropertySelector and IOUserVideoObjectPropertyElement, a specific piece of information about an IOUserVideoObject.

The scope specifies the section of the object in which to look for the property, such as input, output, global, etc. Note that each class has a different set of scopes. A subclass inherits its superclass’s set of scopes.

The IOUserVideoObjectPropertyScope for properties that apply to the object as a whole. All objects have a global scope and for most it is their only scope.

The IOUserVideoObjectPropertyScope for properties that apply to the input side of an object.

The IOUserVideoObjectPropertyScope for properties that apply to the output side of an object.

The IOUserVideoObjectPropertyScope for properties that apply to the play through side of an object.

## Topics

### Property scopes
- [Global](videodriverkit/iouservideoobjectpropertyscope/global.md)
- [Input](videodriverkit/iouservideoobjectpropertyscope/input.md)
- [Output](videodriverkit/iouservideoobjectpropertyscope/output.md)
- [PlayThrough](videodriverkit/iouservideoobjectpropertyscope/playthrough.md)

## See Also

- [Create](iouservideobooleancontrol/create.md)
- [init](iouservideobooleancontrol/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyscope)*