# AEManagerInfo(_:_:)

**Framework**: Core Services  
**Kind**: func

Provides information about the version of the Apple Event Manager currently available or the number of processes that are currently recording Apple events.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEManagerInfo(_ keyWord: AEKeyword, _ result: UnsafeMutablePointer<Int>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

For recordable applications, the information provided by `AEManagerInfo` may be useful when the application is responding to Apple events that it sends to itself.

For information on determining whether the Apple Event Manager is available, see the Apple Event Manager Gestalt Selector, described in . 

##### 1819457

Thread safe starting in OS X v10.2.

The `AEManagerInfo` function is available only in version 1.01 and later of the Apple Event Manager.

## Parameters

- `keyWord`: See  .
- `result`: If you pass  ,   supplies version information for the Apple Event Manager, in a format that matches the   resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449373-aemanagerinfo)*