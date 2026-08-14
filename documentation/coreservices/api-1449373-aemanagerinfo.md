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

For information on determining whether the Apple Event Manager is available, see the Apple Event Manager Gestalt Selector, described in *Inside macOS: Gestalt Manager Reference*. 

##### 1819457

Thread safe starting in OS X v10.2.

The `AEManagerInfo` function is available only in version 1.01 and later of the Apple Event Manager.

## Parameters

- `keyWord`: A value that determines the kind of information the function supplies in the `result` parameter. Pass the value `keyAERecorderCount` to obtain the number of processes that are currently recording Apple events. Pass the value `keyAEVersion` to obtain version information for the Apple Event Manager, in `NumVersion` format. Some keyword constants are defined in [`Keyword Parameter Constants`](apple_events/1527206-keyword_parameter_constants.md). See [`AEKeyword`](aekeyword.md).
- `result`: A pointer to a long value. On return, provides information that depends on what you pass in the `keyword` parameter. If you pass `keyAERecorderCount`, `result` specifies the number of processes that are currently recording Apple events. If you pass `keyAEVersion`, `result` supplies version information for the Apple Event Manager, in a format that matches the `'vers'` resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449373-aemanagerinfo)*