# ATSUDirectLayoutOperationOverrideProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
typealias ATSUDirectLayoutOperationOverrideProcPtr = (ATSULayoutOperationSelector, ATSULineRef?, URefCon?, UnsafeMutableRawPointer?, UnsafeMutablePointer<ATSULayoutOperationCallbackStatus>?) -> OSStatus
```

```c
typedef OSStatus (*ATSUDirectLayoutOperationOverrideProcPtr)(ATSULayoutOperationSelector iCurrentOperation, ATSULineRef iLineRef, URefCon iRefCon, void *iOperationCallbackParameterPtr, ATSULayoutOperationCallbackStatus *oCallbackStatus);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsudirectlayoutoperationoverrideprocptr)*