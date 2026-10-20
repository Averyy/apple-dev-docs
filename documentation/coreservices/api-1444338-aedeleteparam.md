# AEDeleteParam(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Deletes a keyword-specified parameter from an Apple event record.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEDeleteParam(_ theAppleEvent: UnsafeMutablePointer<AppleEvent>!, _ theAEKeyword: AEKeyword) -> OSErr
```

```c
OSErr AEDeleteParam(AppleEvent *theAppleEvent, AEKeyword theAEKeyword);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145).

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theAppleEvent`: A pointer to the Apple event or Apple event record to delete the parameter from. See [`AppleEvent`](./appleevent.md).
- `theAEKeyword`: The keyword that specifies the parameter to delete. Some keyword constants are described in [Keyword Parameter Constants](./apple_events/api-1527206-keyword_parameter_constants.md). See [`AEKeyword`](./aekeyword.md).

## See Also

### Deleting Descriptors
- [func AEDeleteItem(UnsafeMutablePointer<AEDescList>!, Int) -> OSErr](./api-1447164-aedeleteitem.md)
  Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444338-aedeleteparam)*