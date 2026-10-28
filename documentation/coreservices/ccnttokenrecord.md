# ccntTokenRecord

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Stores token information used by the AEResolve functionwhile locating a range of objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct ccntTokenRecord
```

```c
typedef struct ccntTokenRecord {
    ...
} ccntTokenRecord;
```

## Overview

When the [`AEResolve(_:_:_:)`](./api-1449720-aeresolve.md) functioncalls an object accessor function to locate a range of objects, theApple Event Manager replaces the descriptor of type `typeCurrentContainer` witha token for the container of each boundary object. When using `AEResolve` toresolve the object specifier, your application doesn’t need toexamine the contents of this token, because the Apple Event Managerkeeps track of it.

If your application attempts to resolve some or all of theobject specifier without calling `AEResolve`,the application may need to examine the token before it can locatethe boundary objects. The token provided by the Apple Event Managerfor a boundary object’s container is a descriptor of type `typeToken` whosedata storage pointer refers to a structure of type `ccntTokenRecord`. 

## Topics

### Initializers
- [init()](./ccnttokenrecord/api-1442803-init.md)
- [init(tokenClass: DescType, token: AEDesc)](./ccnttokenrecord/api-1443203-init.md)
### Instance Properties
- [var token: AEDesc](./ccnttokenrecord/api-1445534-token.md)
  A token for the current container. (Token is definedin [`AEDisposeToken(_:)`](./api-1446783-aedisposetoken.md). See [`AEDesc`](./aedesc.md).
- [var tokenClass: DescType](./ccnttokenrecord/api-1444917-tokenclass.md)
  The class ID of the container represented by the `token` parameter.See [`DescType`](./desctype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/ccnttokenrecord)*