# AERemoteProcessResolverContext

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Supplied as a parameter when performing asynchronous resolutionof remote processes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
struct AERemoteProcessResolverContext
```

```c
typedef struct AERemoteProcessResolverContext {
    ...
} AERemoteProcessResolverContext;
```

#### Overview

When you call [`AERemoteProcessResolverScheduleWithRunLoop(_:_:_:_:_:)`](./api-1447259-aeremoteprocessresolverschedulew.md) forasynchronous resolution, you supply a reference to a structure ofthis type, along with a reference to a callback routine, definedby [`AERemoteProcessResolverCallback`](./aeremoteprocessresolvercallback.md).The context is copied and the info pointer retained. When the callbackis made, the info pointer is passed to the callback.

## Topics

### Initializers
- [init()](./aeremoteprocessresolvercontext/api-1449429-init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CFAllocatorRetainCallBack!, release: CFAllocatorReleaseCallBack!, copyDescription: CFAllocatorCopyDescriptionCallBack!)](./aeremoteprocessresolvercontext/api-1792092-init.md)
### Instance Properties
- [var copyDescription: CFAllocatorCopyDescriptionCallBack!](./aeremoteprocessresolvercontext/api-1442771-copydescription.md)
  A prototype for a function callback that providesa description of the specified data. Called on the info pointer.This field may be `NULL`.
- [var info: UnsafeMutableRawPointer!](./aeremoteprocessresolvercontext/api-1449518-info.md)
  A pointer to arbitrary information. The pointeris retained and passed to the callback, allowing you to provideinformation to that routine.
- [var release: CFAllocatorReleaseCallBack!](./aeremoteprocessresolvercontext/api-1444738-release.md)
  A prototype for a function callback that releasesthe specified data. Called on the info pointer. This field may be `NULL`.
- [var retain: CFAllocatorRetainCallBack!](./aeremoteprocessresolvercontext/api-1450097-retain.md)
  A prototype for a function callback that retainsthe specified data. Called on the info pointer. This field may be `NULL`.
- [var version: CFIndex](./aeremoteprocessresolvercontext/api-1445231-version.md)
  This should be set to zero (0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolvercontext)*