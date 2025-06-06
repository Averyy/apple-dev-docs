# MDQueryCreateResultFunction

**Framework**: Core Services  
**Kind**: tdef

Callback function used to create the result objects stored and returned by a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias MDQueryCreateResultFunction = (MDQuery?, MDItem?, UnsafeMutableRawPointer?) -> UnsafeRawPointer?
```

#### Return_value

The function mustreturn a pointer-sized value that can be managed with the callbackswhich were set at the same time the create function was given tothe query. The value must be returned with a reference (such asif the retain callback had been called on it), as implied by theCreate name. If this function doesn't wish to create a new objectit can return the given MDItemRef, but must also return it witha new retain, and the callbacks must be able to handle an MDItemRefas an input value. If this function returns NULL, NULL will be storedfor the moment in the query, MDQueryGetResultAtIndex() may returnNULL for that result, and the next time the query wants the result,it will call this function again.

#### Discussion

The function may hold onto the given attribute name and/orvalue in some other data structure, but must retain them for themto remain valid.

## Parameters

- `query`: The query instance.
- `item`: The default MDItemRef for the result.
- `context`: The user-defined context parameter provided to the   function.

## See Also

- [typealias MDQuerySortComparatorFunction](mdquerysortcomparatorfunction.md)
  Callback function used to sort the results of a query.
- [typealias MDQueryCreateValueFunction](mdquerycreatevaluefunction.md)
  Callback function usedto create the value objects stored and returned by a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdquerycreateresultfunction)*