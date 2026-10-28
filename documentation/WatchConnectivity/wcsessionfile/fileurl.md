# fileURL

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSURL * fileURL;
```

## Discussion

The system places downloaded files inside a temporary directory. If you intend to keep the file, it is your responsibility to move the file to a more permanent location inside your extension’s container directory. You must move the file before your session delegate’s [`session(_:didReceive:)`](../wcsessiondelegate/session%28_,didreceive%29.md) method returns.

## See Also

### Getting the File Information
- [var metadata: [String : Any]?](./metadata.md)
  A dictionary of additional information that was sent with the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/fileurl)*