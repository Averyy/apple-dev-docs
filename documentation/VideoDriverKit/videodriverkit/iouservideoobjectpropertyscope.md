# IOUserVideoObjectPropertyScope

**Framework**: VideoDriverKit  
**Kind**: enum

A four character code which, along with the selector and element, identifies a specific piece of information about a video object.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoObjectPropertyScope : uint32_t;
```

#### Overview

The scope specifies the section of the object in which to look for the property, such as input, output, or global. Note that each class has a different set of scopes. A subclass inherits its superclass’s set of scopes.

## Topics

### Property scopes
- [Global](videodriverkit/iouservideoobjectpropertyscope/global.md)
  The scope for properties that apply to the object as a whole.
- [Input](videodriverkit/iouservideoobjectpropertyscope/input.md)
  The scope for properties that apply to the input side of an object.
- [Output](videodriverkit/iouservideoobjectpropertyscope/output.md)
  The scope for properties that apply to the output side of an object.
- [PlayThrough](videodriverkit/iouservideoobjectpropertyscope/playthrough.md)
  The scope for properties that apply to the play-through side of an object.

## See Also

- [Create](iouservideobooleancontrol/create.md)
  A static factory method that allocates and initializes a video Boolean control.
- [init](iouservideobooleancontrol/init.md)
  Initializes an IOUserVideoBooleanControl.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyscope)*