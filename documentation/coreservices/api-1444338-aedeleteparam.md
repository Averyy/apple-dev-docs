# AEDeleteParam(_:_:)

**Framework**: Core Services  
**Kind**: func

Deletes a keyword-specified parameter from an Apple event record.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDeleteParam(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event or Apple event record to delete the parameter from. See  .
- `theAEKeyword`: The keyword that specifies the parameter to delete. Some keyword constants are described in  . See  .

## See Also

- [func AEDeleteItem(UnsafeMutablePointer<AEDescList>!, Int) -> OSErr](1447164-aedeleteitem.md)
  Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444338-aedeleteparam)*