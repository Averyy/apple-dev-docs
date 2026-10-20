# SKSearch

**Framework**: Core Services  
**Kind**: cl  
**Role**: Class

Defines an opaque data type representing an asynchronous search.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
class SKSearch
```

#### Overview

A search object is created when you call the [`SKSearchCreate(_:_:_:)`](./api-1443079-sksearchcreate.md) function.

##### Special Considerations

You cannot use [`CFMakeCollectable`](../CoreFoundation/cfmakecollectable.md) with SKSearch objects. In a garbage-collected environment, you must use [`CFRelease`](../CoreFoundation/cfrelease.md) to dispose of an SKSearch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearch)*