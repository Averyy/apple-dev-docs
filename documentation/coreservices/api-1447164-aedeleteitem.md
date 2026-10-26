# AEDeleteItem(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDeleteItem(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int) -> OSErr
```

```c
OSErr AEDeleteItem(AEDescList *theAEDescList, long index);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list containing the descriptor to delete. See [`AEDescList`](./aedesclist.md).
- `index`: A one-based positive integer indicating the position of the descriptor to delete. `AEDeleteItem` returns an error if you pass zero, a negative number, or a value that is out of range.

## See Also

### Deleting Descriptors
- [func AEDeleteParam(UnsafeMutablePointer<AppleEvent>!, AEKeyword) -> OSErr](./api-1444338-aedeleteparam.md)
  Deletes a keyword-specified parameter from an Apple event record.
- [AEDeleteKeyDesc](../applicationservices/apple_event_manager/api-1806085-aedeletekeydesc.md)
  Deletes a keyword-specified parameter from an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447164-aedeleteitem)*