# FSEventStreamShow(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamShow(_ streamRef: ConstFSEventStreamRef)
```

```c
void FSEventStreamShow(ConstFSEventStreamRef streamRef);
```

#### Discussion

Prints a description of the supplied stream to stderr. For debugging only.

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444302-fseventstreamshow)*