# SKSearch

**Framework**: Core Services  
**Kind**: cl

Defines an opaque data type representing an asynchronous search.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
class SKSearch
```

#### Overview

A search object is created when you call the [`SKSearchCreate(_:_:_:)`](1443079-sksearchcreate.md) function.

##### 1681574

You cannot use [`CFMakeCollectable`](https://developer.apple.com/documentation/corefoundation/1521163-cfmakecollectable) with SKSearch objects. In a garbage-collected environment, you must use [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to dispose of an SKSearch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearch)*