# errors

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An array of all errors that occurred during the processing of the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var errors: [any Error] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSError *> * errors;
```

## Discussion

Provides an array of all parse-time errors for the extension, with repeat errors consolidated into a single entry for the original occurrence only. If no errors occurred, an empty array is returned.

> **Note**: Once the extension is loaded, use the [`errors`](./errors.md) property on an extension context to monitor any runtime errors, as they can occur after the extension is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/errors)*