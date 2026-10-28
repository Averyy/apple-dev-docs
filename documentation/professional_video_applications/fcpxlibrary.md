# FCPXLibrary

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An object that contains details of a Final Cut Pro library.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
class FCPXLibrary
```

```objc
@interface FCPXLibrary : FCPXObject
```

## Overview

An FCPXLibrary object contains a reference to a library that has the current project open in the Final Cut Pro timeline.

## Topics

### Identifying a Final Cut Pro Library
- [var url: URL](./fcpxlibrary/url.md)
  The location of the library in the file system.
- [var name: String](./fcpxlibrary/name.md)
  The Final Cut Pro library name.

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
- [class FCPXEvent](./fcpxevent.md)
  An object that contains details of an event in the Final Cut Pro library.
- [class FCPXProject](./fcpxproject.md)
  An object that contains details of a project with the sequence open in the Final Cut Pro timeline.
- [class FCPXSequence](./fcpxsequence.md)
  An object that contains details of a sequence that’s open in the Final Cut Pro timeline.
- [enum FCPXSequenceTimecodeFormat](./fcpxsequencetimecodeformat.md)
  The display format of the sequence timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxlibrary)*