# MDQuerySortComparatorFunction

**Framework**: Core Services  
**Kind**: tdef

Callback function used to sort the results of a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias MDQuerySortComparatorFunction = (UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafeMutableRawPointer?) -> CFComparisonResult
```

#### Return_value

The function must return one of the CFComparisonResults `kCFCompareLessThan`, `kCFCompareEqualTo`, or `kCFCompareGreaterThan`. There is no provision for unordered results. The comparison should be a total order relation and produce the same results for the same inputs.

## Parameters

- `query`: The query instance.
- `attrs1`: A C array of attribute values for a result. The values occur in the array in the same order and position that the attribute names were passed in the   array when the query was created. The values of the attributes will be   if the attribute doesn't exist for a result or if read access to that attribute is not allowed.
- `attrs2`: A C array of attribute values for a result. The values occur in the array in the same order and position that the attribute names were passed in the   array when the query was created. The values of the attributes will be   if the attribute doesn't exist for a result or if read access to that attribute is not allowed.
- `context`: The user-defined context parameter provided in the function  .

## See Also

- [typealias MDQueryCreateResultFunction](mdquerycreateresultfunction.md)
  Callback function used to create the result objects stored and returned by a query.
- [typealias MDQueryCreateValueFunction](mdquerycreatevaluefunction.md)
  Callback function usedto create the value objects stored and returned by a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdquerysortcomparatorfunction)*