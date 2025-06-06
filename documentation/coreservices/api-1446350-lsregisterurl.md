# LSRegisterURL(_:_:)

**Framework**: Core Services  
**Kind**: func

Registers an app, using a URL, in the Launch Services database.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func LSRegisterURL(_ inURL: CFURL, _ inUpdate: Bool) -> OSStatus
```

#### Return_value

A result code; see [`Result Codes`](launch_services#1661359.md).

#### Discussion

This function adds the designated application and its document and URL claims (if any) to the Launch Services database, making the application a candidate for document and URL binding.

##### 1676155

Thread-safe since Mac OS version 10.3.

## Parameters

- `inFileURL`: A Core Foundation URL reference designating the app to be registered; see the   in the Core Foundation Reference Documentation for a description of the   data type. The URL must have scheme   and contain a valid path to an app file or app bundle.
- `inUpdate`: A Boolean value specifying whether Launch Services should update existing information registered for the app, if any. If this parameter is  , the app will not be registered if it has already been registered previously and its current modification date has not changed from when it was last registered; if the parameter is  , the app’s registered information will be updated even if its modification date has not changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446350-lsregisterurl)*