# AECountItems(_:_:)

**Framework**: Core Services  
**Kind**: func

Counts the number of descriptors in a descriptor list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECountItems(_ theAEDescList: UnsafePointer<AEDescList>!, _ theCount: UnsafeMutablePointer<Int>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

Your application typically counts the descriptors in a descriptor list when it is extracting data from an Apple event. You can use the functions in “Getting Items From Descriptor Lists” to get an individual item from a descriptor list or to iterate through the items. 

##### 1770170

Thread safe starting in OS X v10.2.

## Parameters

- `theAEDescList`: A pointer to the descriptor list to count. See  .
- `theCount`: A pointer to a count variable. On return, the number of descriptors in the specified descriptor list, which can be 0, if the list is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449533-aecountitems)*