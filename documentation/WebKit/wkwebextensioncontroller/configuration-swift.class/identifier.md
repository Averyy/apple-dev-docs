# identifier

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier used for persistent configuration storage, or `nil` when it is the default or not persistent.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var identifier: UUID? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSUUID * identifier;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class/identifier)*