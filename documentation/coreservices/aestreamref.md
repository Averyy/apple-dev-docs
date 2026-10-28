# AEStreamRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

An opaque data structure for storing stream-based descriptor data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEStreamRef = OpaquePointer
```

```c
typedef struct OpaqueAEStreamRef *AEStreamRef;
```

## Discussion

You create `AEStreamRef` objects and manipulate their contents using the stream routines found in the section [Apple Event Manager](../applicationservices/apple_event_manager.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aestreamref)*