# AEDeleteItem(_:_:)

**Framework**: Core Services  
**Kind**: func

Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDeleteItem(_ theAEDescList: UnsafeMutablePointer<AEDescList>!, _ index: Int) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list containing the descriptor to delete. See  .
- `index`: A one-based positive integer indicating the position of the descriptor to delete.   returns an error if you pass zero, a negative number, or a value that is out of range.

## See Also

- [func AEDeleteParam(UnsafeMutablePointer<AppleEvent>!, AEKeyword) -> OSErr](1444338-aedeleteparam.md)
  Deletes a keyword-specified parameter from an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447164-aedeleteitem)*