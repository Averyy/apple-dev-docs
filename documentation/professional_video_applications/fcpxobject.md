# FCPXObject

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An abstract superclass for Final Cut Pro timeline proxy objects.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
class FCPXObject
```

```objc
@interface FCPXObject : NSObject
```

#### Overview

The ProExtensionHost framework provides a few object classes that act as proxies to certain aspects of the Final Cut Pro timeline. These proxy objects include a currently active sequence in the Final Cut Pro timeline as well as its containers, such as project, event, and library.

A `FCPXObject` provides common properties of timeline proxy objects, such as the container, name, and object type. Subclasses of `FCPXObject` hold additional information specific to the timeline proxy object they represent. A workflow extension can use these properties to identify the details of the current timeline sequence opened in Final Cut Pro.

## Topics

### Getting the Final Cut Pro Object Details
- [var container: FCPXObject?](./fcpxobject/container.md)
  The container of a Final Cut Pro timeline object.
- [var objectType: FCPXObjectType](./fcpxobject/objecttype.md)
  The type of a Final Cut Pro timeline proxy object, such as a sequence or project.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [FCPXEvent](./fcpxevent.md)
- [FCPXLibrary](./fcpxlibrary.md)
- [FCPXProject](./fcpxproject.md)
- [FCPXSequence](./fcpxsequence.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### FCPX Timeline Proxy Objects
- [enum FCPXObjectType](./fcpxobjecttype.md)
  The Final Cut Pro timeline object types.
- [class FCPXLibrary](./fcpxlibrary.md)
  An object that contains details of a Final Cut Pro library.
- [class FCPXEvent](./fcpxevent.md)
  An object that contains details of an event in the Final Cut Pro library.
- [class FCPXProject](./fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](./fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.
- [enum FCPXSequenceTimecodeFormat](./fcpxsequencetimecodeformat.md)
  The display format of the sequence timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxobject)*