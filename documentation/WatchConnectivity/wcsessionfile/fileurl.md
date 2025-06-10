# fileURL

**Framework**: Watch Connectivity  
**Kind**: property

The URL of the file that was received.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fileURL: URL { get }
```

#### Discussion

The system places downloaded files inside a temporary directory. If you intend to keep the file, it is your responsibility to move the file to a more permanent location inside your extension’s container directory. You must move the file before your session delegate’s [`session(_:didReceive:)`](wcsessiondelegate/session(_:didreceive:).md) method returns.

## See Also

- [var metadata: [String : Any]?](wcsessionfile/metadata.md)
  A dictionary of additional information that was sent with the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/fileurl)*