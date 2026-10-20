# AEArrayDataPointer

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

A pointer to a union of type `AEArrayData`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEArrayDataPointer = UnsafeMutablePointer<AEArrayData>
```

```c
typedef AEArrayData *AEArrayDataPointer;
```

#### Discussion

This data type merely defines a pointer to an [`AEArrayData`](./aearraydata.md) union.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aearraydatapointer)*