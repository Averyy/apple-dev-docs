# FSEventStreamContext

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
struct FSEventStreamContext
```

```c
typedef struct FSEventStreamContext {
    ...
} FSEventStreamContext;
```

## Topics

### Initializers
- [init()](./fseventstreamcontext/api-1445021-init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: CFAllocatorRetainCallBack?, release: CFAllocatorReleaseCallBack?, copyDescription: CFAllocatorCopyDescriptionCallBack?)](./fseventstreamcontext/api-1792099-init.md)
### Instance Properties
- [var copyDescription: CFAllocatorCopyDescriptionCallBack?](./fseventstreamcontext/api-1445178-copydescription.md)
  The callback used to create a descriptive string representation of the info pointer (or the data pointed to by the info pointer) for debugging purposes. This can be NULL.
- [var info: UnsafeMutableRawPointer?](./fseventstreamcontext/api-1446169-info.md)
  An arbitrary client-defined value (for instance, a pointer) to be associated with the stream and passed to the callback when it is invoked. If a non-NULL value is supplied for the retain callback the framework will use it to retain this value. If a non-NULL value is supplied for the release callback then when the stream is deallocated it will be used to release this value. This can be NULL.
- [var release: CFAllocatorReleaseCallBack?](./fseventstreamcontext/api-1450554-release.md)
  The callback used release a retain on the info pointer. This can be NULL.
- [var retain: CFAllocatorRetainCallBack?](./fseventstreamcontext/api-1450539-retain.md)
  The callback used retain the info pointer. This can be NULL.
- [var version: CFIndex](./fseventstreamcontext/api-1444474-version.md)
  Currently the only valid value is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fseventstreamcontext)*