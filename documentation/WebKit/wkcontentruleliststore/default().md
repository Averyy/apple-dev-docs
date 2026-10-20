# default()

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns the default content rule list store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> Self!
```

```objc
+ (instancetype) defaultStore;
```

#### Return Value

The default rule list store.

#### Discussion

The default store contains the rules that your app created specifically for the current user.

## See Also

### Creating a Content Rule List Store
- [convenience init!(url: URL!)](./init%28url%29-dile.md)
  Creates a new content rule list store in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/default())*