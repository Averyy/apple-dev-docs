# FSEventStreamRelease(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamRelease(_ streamRef: FSEventStreamRef)
```

#### Discussion

Decrements the stream's refcount. The refcount is initially one and is incremented via FSEventStreamRetain(). If the refcount reaches zero then the stream is deallocated.

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445989-fseventstreamrelease)*