# FCPXEvent

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An object that contains details of an event in the Final Cut Pro library.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
class FCPXEvent
```

```objc
@interface FCPXEventxxx : FCPXObject
```

## Topics

### Identifying a Final Cut Pro Event
- [var uid: String](./fcpxevent/uid.md)
  An ID that uniquely identifies a Final Cut Pro event.
- [var name: String](./fcpxevent/name.md)
  The Final Cut Pro event name.

## Relationships

### Inherits From
- [FCPXObject](./fcpxobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### FCPX Timeline Proxy Objects
- [class FCPXObject](./fcpxobject.md)
  An abstract superclass for Final Cut Pro timeline proxy objects.
- [enum FCPXObjectType](./fcpxobjecttype.md)
  The Final Cut Pro timeline object types.
- [class FCPXLibrary](./fcpxlibrary.md)
  An object that contains details of a Final Cut Pro library.
- [class FCPXProject](./fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](./fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.
- [enum FCPXSequenceTimecodeFormat](./fcpxsequencetimecodeformat.md)
  The display format of the sequence timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxevent)*