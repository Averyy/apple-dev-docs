# default()

**Framework**: Webkit  
**Kind**: method

Returns the default content rule list store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func `default`() -> Self!
```

#### Return Value

The default rule list store.

#### Discussion

The default store contains the rules that your app created specifically for the current user.

## See Also

- [convenience init!(url: URL!)](wkcontentruleliststore/init(url:).md)
  Creates a new content rule list store in the specified directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/default())*